import requests,json
controller = '172.129.78.179'

# 获取 toekn
try:
    data = {"auth":{"scope":{"project":{"domain":{"name":"demo"},"name":"admin"}},"identity":{"password":{"user":{"domain":{"name":"demo"},"password":"000000","name":"admin"}},"methods":["password"]}}}
    url = 'http://172.129.78.179:5000/v3/auth/tokens'
    res = requests.post(url,json=data)
    headers = {'X-Auth-Token': res.headers['X-Subject-Token'],
            "User-Agent": "python-cinderclient",
            "Accept": "application/json",
            "Content-Type": "application/json"}
except:
    print('获取token错误')

# 获取 volume 
volume_url = 'http://172.129.78.179:8776/v3/9782bee03b514511abf53f0aef94f90c/volumes/detail'
volume_res = requests.get(volume_url,headers=headers)
volume_list_json = volume_res.json()
for i in volume_list_json['volumes']:
    # 删除 volume
    if i['name'] == 'test-volume03':
        delete_id = i['id']
        # print(delete_id)
        delete_url = f'http://{controller}:8776/v3/9782bee03b514511abf53f0aef94f90c/volumes/{delete_id}'
        requests.delete(delete_url,headers=headers)

    else:
        # 创建 volume
        try:
            create_volume_url = f'http://{controller}:8776/v3/9782bee03b514511abf53f0aef94f90c/volumes'
            create_volume_data = {
            "volume": {
                "backup_id": None,
                "description": None,
                "availability_zone": None,
                "source_volid": None,
                "consistencygroup_id": None,
                "snapshot_id": None,
                "size": "5",
                "name": "test-volume03",
                "imageRef": None,
                "volume_type": None,
                "metadata": {}}
            }
            res = requests.post(create_volume_url,json=create_volume_data,headers=headers)
        except:
            print('创建volume的状态码：',res.status_code)
    print(i['id'],i['name'])
    # 获取指定volume的详细信息
    disk_id = None
    if disk_id == i['id']:
        volume_detail_url = f'http://172.129.78.179:8776/v3/9782bee03b514511abf53f0aef94f90c/volumes/{disk_id}'
        new_volume_res = requests.get(volume_detail_url,headers=headers)
        print(new_volume_res.json())

# 实例上添加上volume
# add_server_url = f'http://{controller}:8774/v2.1/servers/bc9d8506-801b-4426-b4f2-b500eedc024e/os-volume_attachments'
# volume_data = {
#     "volumeAttachment": {
#         "volumeId": "9809eb1d-ed84-4c65-98de-a53ec905d5f8"
#     }
# }
# res = requests.post(add_server_url,json=volume_data,headers=headers)
# print(res.json())