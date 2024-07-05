# 参考文档：https://sdkcenter.developer.huaweicloud.cn/?language=Python
# 参考文档：https://support.huaweicloud.com/sdkreference-as/as_sdk_0101.html
# coding: utf-8

import json,time
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkecs.v2 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkims.v2.region.ims_region import ImsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkims.v2 import *

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkims.v2.region.ims_region import ImsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkims.v2 import *


ak = "DIQLKEMVNX0FFVZHLJYQ"
sk = "xfomx0u63X5Eb4QjbgWRyKZOvGY4mMmxC2jh178W"

credentials = BasicCredentials(ak, sk)

client = EcsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EcsRegion.value_of("cn-east-2")) \
        .build()
    
imsclient = ImsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(ImsRegion.value_of("cn-east-2")) \
        .build()

def get(ServerName = None):
    request = ListServersDetailsRequest()
    request.name = ServerName
    response = client.list_servers_details(request)
    return response

def delete(ServerName = None):
    request = NovaDeleteServerRequest()
    server_id = get(ServerName)
    server_id = json.loads(str(server_id))
    request.server_id =  server_id['servers'][0]['id']
    response = client.nova_delete_server(request)
    print(response)

def create(server_name, imagename = "CentOS 7.9 64bit"):
    # 获取镜像id
    request = ListImagesRequest()
    request.name = imagename
    response = imsclient.list_images(request)
    ImageId = json.loads(str(response))['images'][0]['id']
    
    request = CreatePostPaidServersRequest()
    # 系统盘相关配置
    rootVolumeServer = PostPaidServerRootVolume(
        volumetype="SAS"
    )
    # 子网
    listNicsServer = [
        PostPaidServerNic(
            subnet_id="847ec176-866f-46fe-86c3-a461f8318d3d"
        )
    ]
    # 弹性网卡
    # bandwidthEip = PostPaidServerEipBandwidth(
    #     size=100,
    #     sharetype="PER",
    #     chargemode="traffic"
    # )
    # eipPublicip = PostPaidServerEip(
    #     iptype="5_bgp",
    #     bandwidth=bandwidthEip
    # )
    # publicipServer = PostPaidServerPublicip(
    #     eip=eipPublicip
    # )
    # ecs 信息
    serverbody = PostPaidServer(
        flavor_ref="s3.xlarge.2",
        image_ref=ImageId,
        name=server_name,
        nics=listNicsServer,
        # publicip=publicipServer,
        root_volume=rootVolumeServer,
        vpcid="1068d27e-56cb-45a6-8099-0fb0cc8337c0"
    )
    # 创建 ecs
    request.body = CreatePostPaidServersRequestBody(
        server=serverbody
    )
    # 在华东-上海二创建 ecs
    response = client.create_post_paid_servers(request)
    print("create response type：", type(response))
    print("create response：", response)
    # 获取 serverid
    # return image_get(ServerName=ServerName)
    
