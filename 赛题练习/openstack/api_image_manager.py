#encoding:utf-8
'''
在 controller 节点的/root 目录下创建 api_image_manager.py 脚本，编写 python 代码对接 OpenStack API，完成镜像的创建与上传。创建之前查询是否存在“同名镜像”，如果存在先删除该镜像。
创建镜像：要求在 OpenStack 私有云平台中上传镜像 cirros-0.3.4-x86_64-disk.img， 名字为 cirros001，disk_format 为 qcow2，container_format 为bare。
查询镜像：查询 cirros001 的详细信息，并以 json 格式文本输出到控制台。 完成后提交 OpenStack Python 运维开发环境 Controller 节点的 IP 地址，用户名和密码提交。
'''
import requests,json

controller = '172.129.78.57'
class Image:
    def __init__(self) -> None:
        url = f'http://{controller}:5000/v3/auth/tokens'
        body = {"auth": {"scope": {"project": {"domain": {"name": "demo"}, "name": "admin"}}, "identity": {"password": {"user": {"domain": {"name": "demo"}, "password": "000000", "name": "admin"}}, "methods": ["password"]}}}
        res = requests.post(url,json=body)
        self.headers  = {'Content-Type': 'application/json','X-Auth-Token': res.headers["X-Subject-Token"]}
        # print(self.headers)
    
    def create(self,image_name,file_path:str):
        if self.get(image_name):
            self.delete(image_name)
        url = f'http://{controller}:9292/v2/images'
        body = {"container_format": "bare", "disk_format": "qcow2", "name": image_name}
        requests.post(url,json=body,headers=self.headers)
        
        
        image_id = self.get(image_name)
        put_url = f'http://{controller}:9292/v2/images/{image_id}/file'
        self.headers['Content-Type'] = 'application/octet-stream'
        res = requests.put(put_url,headers=self.headers,data=open(file_path,'rb').read())
        if res.status_code == 200:
            print('创建成功')
        if res.status_code == 201:
            print('创建成功')
    
    def delete(self,image_name):
        image_id = self.get(image_name=image_name)
        url = f'http://{controller}:9292/v2/images/{image_id}'
        res = requests.delete(url,headers=self.headers)
        if res.status_code == 204:
            print('删除成功')
        if res.status_code == 201:
            print('删除成功')
        
        
    def get(self,image_name = None):
        url = f'http://{controller}:9292/v2/images'
        result_json = json.loads(requests.get(url,headers=self.headers).text)
        # print(result_json)
        for i in result_json["images"]:
            print(i['id'],'     ',i["name"], '    ',i['status'])
            if image_name == i['name']:
                return i['id']
        
        
if __name__ == "__main__":
    image = Image()
    # image.create('ws',file_path='cirros-0.6.2-aarch64-disk.img')
    # image.delete('cirros')
    print(image.get())
