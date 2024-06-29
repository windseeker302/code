# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkecs.v2 import *

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = os.environ["CLOUD_SDK_AK"]
    sk = os.environ["CLOUD_SDK_SK"]

    credentials = BasicCredentials(ak, sk)

    client = EcsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EcsRegion.value_of("cn-east-2")) \
        .build()

    try:
        request = CreatePostPaidServersRequest()
        rootVolumeServer = PostPaidServerRootVolume(
            volumetype="SAS"
        )
        listNicsServer = [
            PostPaidServerNic(
                subnet_id="847ec176-866f-46fe-86c3-a461f8318d3d"
            )
        ]
        serverbody = PostPaidServer(
            flavor_ref="s3.xlarge.2",
            image_ref="c493bc51-1f1b-482d-82fb-d2ecf445af9d",
            name="test-api",
            nics=listNicsServer,
            root_volume=rootVolumeServer,
            vpcid="1068d27e-56cb-45a6-8099-0fb0cc8337c0"
        )
        request.body = CreatePostPaidServersRequestBody(
            server=serverbody
        )
        response = client.create_post_paid_servers(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)