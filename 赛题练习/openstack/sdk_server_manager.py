from openstack import connection
import json
'''
使用已建好的OpenStackPython运维开发环境，在/root目录下创建sdk_server_manager.py脚本，使用 python-openstack sdk Python 模块，完成云主机的创建和查询。创建之前查询是否存在“同名云主机”，如果存在先删除该云主机。
创建 1 台云主机：云主机信息如下：
云主机名称如下：server001
镜像文件：cirros-0.3.4-x86_64-disk.img
云主机类型：m1.tiny
网络等必要信息自己补充。
查询云主机：查询云主机 server001 的详细信息，并以 json 格式文本输出到控制台。
'''

conn = connection.Connection(
    auth_url = 'http://172.129.78.57:5000/v3/',
    project_name = 'admin',
    domain_name = 'demo',
    username = 'admin',
    password = '000000'
)

s1 = {
    "servername": 'ws1',
    "imagename": 'cirros001',
    "flavorname": 'm1.small',
    'networkname': 'vlan31'
}

conn.create_server(name=s1['servername'],image=s1['imagename'],flavor=s1['flavorname'],network=s1['networkname'])
print(json.dumps(str(conn.get_server('server001'))))