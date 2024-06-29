import requests
import json

# 获得token
def token():
    data =  {"auth": {"identity": {"methods": ["password"], "password": {
                "user": {"password": "000000", "name": "admin",
                "domain": {"name": "demo"}}}},
                "scope": {"project": {"name": "admin", "domain": {"name":"demo"}}}}}
    token_url = "http://172.129.78.179:5000/v3/auth/tokens"
    try:
        res = requests.post(token_url,data=json.dumps(data))
        headers = {"X-Auth-Token": res.headers['X-Subject-Token']}
        return headers
    except:
        print("出现异常")

# 创建镜像
def create():
    headers = token()
    url = 'http://172.129.78.179:9292/v2/images'
    data = {
        "container_format": "bare",
        "disk_format": "qcow2",
        "name": "py-test-cirros"
    }
    print(headers)
    data = json.dumps(data)
    res = requests.post(url,data=data,headers=headers)
    res_json = res.json()

    update_api = 'http://172.129.78.179:9292/v2/images/' + res_json['id'] + '/file'
    headers['Content-Type'] = 'application/octet-stream'
    requests.put(update_api,headers=headers,data=open('./cirros-0.3.4-x86_64-disk.img', "rb").read())

# 查看镜像
def select(image_name: str = None):
    headers = token()
    url = 'http://172.129.78.179:9292/v2/images'
    res = requests.get(url,headers=headers)
    a = res.json()
    images = a['images']
    for i in images:
        if i['name'] == image_name:
            new_url = url + '/' + i['id']
            res = requests.get(new_url,headers=headers)
            print(res.json())
        else:
            print(a)


# 删除镜像
def delete(image_id):
    headers = token()
    url = 'http://172.129.78.179:9292/v2/images/' + image_id
    requests.delete(url,headers=headers)


if __name__ == '__main__':
    select()
    # delete('ac071af8-86d6-4ccb-b63c-6e27c32260b4')
    # pass