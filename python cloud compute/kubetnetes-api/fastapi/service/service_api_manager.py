"""
在/root 目录下创建 service_server.py 程序，实现 Service 的增删查改等 Web 访问操作。
http.server 的 host 为 localhost，端口 8888；程序内部实现 Kubernetes 认证。
提示说明：Python 标准库 http.server 模块，提供了 HTTP Server 请求封装。
需要实现的 Restful API 接口如下：
  GET /services/{name}，查询指定名称{name}的 Service；Response 的 Body 以 json 格式 输出。
  POST /services/{yamlfilename} 创建 yaml 文件名称为{yamlfilename}的 Service； Response 的 Body 以 json 格式，（手工将文件服务器主目录所有*.yaml 文件下载到 root 目录下）。
  DELETE /services/{name}；删除指定名称的 Service；Response 的 Body 以 json 格式。
编码完成后，自己手动执行提供 Web HTTP 服务的service_server.py 程序，提交答案进行检测。
"""
from http.server import HTTPServer,BaseHTTPRequestHandler
import requests,json,yaml,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token = "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImlzMkNRMWhqOENHbV9xZlNOU1JEdnlkcG5xMnYyQV80SHJ5YWlUTXpkQUUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbjEtdG9rZW4tcDRtYjgiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiYWRtaW4xIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiNWNlYjZlYWQtMTkwOC00ODQ5LWI0NmMtNmI1OTk2YmQ1ZTYxIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmFkbWluMSJ9.DgrlfShFgki-QUEOjmtEYmaSkUOvVvEz9wH3fwA-B6aUqYbjKMm0oHp8BZxlN-i6dxd36f70Y4bY-iodzDAhZa5CqHLOZEn9lElNXjPQlzePJzZ3JUoCX29TnVdviCSjvreSTZTOpdyTHtPaW01FCOhIKP6ATTdJM9OFx6F69rkWGg35ZCcgsvNSd5Rzf2RTmcWPAeHvesKkDsgI79ZTFZwS4BkFO0lqsQ1z-T75uqouk7CiQU1C46dolDdaqH2dvkINS3o1d9GHbTH_iI0v772dy0dhllKL8WibO5ZfMzirf3JkAaH1NLbCBmTQv65tMWyAUZYRLhtvBEh_59NHFg"
headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path.startswith('/service/')
        service_name = self.path[9:]
        
        url = f'https://172.129.78.158:6443/api/v1/namespaces/default/services/{service_name}'
        res_json = requests.get(url,headers=headers,verify=False).json()
        print(res_json)
        
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(res_json).encode(encoding='utf-8'))
        

    def do_POST(self):
        self.path.startswith('/service/')
        serviceyaml = self.path[10:]
        print(serviceyaml)
        try:
            with open(serviceyaml,encoding='utf-8') as f:
                serviceyaml = yaml.safe_load(f)
            url = 'https://172.129.78.158:6443/api/v1/namespaces/default/services/'
            res_json = requests.post(url,headers=headers,verify=False,json=serviceyaml).json()
            print(res_json)
        
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res_json).encode(encoding='utf-8'))
        except:
            print('创建失败')
    def do_DELETE(self):
        if self.path.startswith('/service/'):
            servicename = self.path[9:]
            print(servicename)
            try:
                url = f'https://172.129.78.158:6443/api/v1/namespaces/default/services/{servicename}'
                res_json = requests.delete(url,headers=headers,verify=False).json()
                print(res_json)
            except:
                print('删除失败')
            
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res_json).encode(encoding='utf-8'))

if __name__ == "__main__":
    address = ('0.0.0.0',8000)
    httpd = HTTPServer(address,MyHandler)
    httpd.serve_forever()