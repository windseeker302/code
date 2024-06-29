# 参考文档：https://sdkcenter.developer.huaweicloud.cn/?language=Python
# 参考文档：https://support.huaweicloud.com/sdkreference-as/as_sdk_0101.html
# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcce.v3.region.cce_region import CceRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcce.v3 import *

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = "DIQLKEMVNX0FFVZHLJYQ"
    sk = "xfomx0u63X5Eb4QjbgWRyKZOvGY4mMmxC2jh178W"

    credentials = BasicCredentials(ak, sk)

    client = CceClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(CceRegion.value_of("cn-north-1")) \
        .build()

    try:
        request = CreateClusterRequest()
        listCidrsContainerNetwork = [
            ContainerCIDR(
                cidr="10.0.0.0/12"
            )
        ]
        containerNetworkSpec = ContainerNetwork(
            mode="vpc-router",
            cidrs=listCidrsContainerNetwork
        )
        hostNetworkSpec = HostNetwork(
            vpc="f57fb6fb-6984-4fc7-b4ad-45c2c6455dee",
            subnet="0e141181-02a8-46f1-9faa-e05399b3fd66"
        )
        specbody = ClusterSpec(
            category="CCE",
            type="VirtualMachine",
            flavor="cce.s1.small",
            host_network=hostNetworkSpec,
            container_network=containerNetworkSpec,
            billing_mode=0
        )
        metadatabody = ClusterMetadata(
            name="chinaskillcce2022"
        )
        request.body = Cluster(
            spec=specbody,
            metadata=metadatabody,
            api_version="v3",
            kind="Cluster"
        )
        response = client.create_cluster(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)