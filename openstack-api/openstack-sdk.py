# 1.执行 sdk_server_manager.py 脚本,成功创建云主机，计 0.5 分
# 2.检查创建的云主机状态正确，计 0.5 分

import json
from openstack import connection

conn = connection.Connection(
    auth_url='http://172.129.78.94:5000/v3/',
    project_name="admin",
    domain_name="demo",
    username='admin',
    password='000000')

if __name__ == '__main__':
    # 创建 flavor
    conn.create_flavor(name="ws1",ram=1024,vcpus=2,disk=10)
    # 创建镜像
    conn.create_image(name="cirros",filename='./cirros-0.6.2-aarch64-disk.img',container_format='bare',disk_format='qcow2')
    # 创建网络
    conn.create_network(external=True,name='ext1')
    conn.create_subnet('ext1',subnet_name='ext1-subnet',cidr='192.168.150.0/24')
    # 创建实例
    conn.create_server(name='ws',image='cirros',flavor='ws1',network='ext1')
    # 遍历查看实例
    for i in conn.list_servers():
        print(i)
