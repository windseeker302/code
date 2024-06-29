from http.server import HTTPServer,BaseHTTPRequestHandler
import yaml
import pod_api_manager,json,urllib.request

pod = pod_api_manager.Pod()

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # request
        self.path.startswith('/pod/')
        serviceName = self.path[5:]
        result = pod.get(pod_name=serviceName,namespace="default")

        # response
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode(encoding='utf-8'))

    def do_POST(self):
        self.path.startswith('/pod/')
        podYamlFile = self.path[5:]
        result = pod.create(yamlFile=podYamlFile,namespace='default')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode(encoding='utf-8'))


server_address = ('',8000)
httpd = HTTPServer(server_address,ProxyHandler)
httpd.serve_forever()