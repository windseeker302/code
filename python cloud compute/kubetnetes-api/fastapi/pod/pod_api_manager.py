import requests,yaml,json,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class Pod():
    def __init__(self):
        with open("token.txt",encoding='utf-8') as f:
            token = 'bearer ' + f.read()

        self.headers = {
            'Authorization': token
        }

    def create(self,yamlFile,namespace):
        with open(yamlFile) as f:
            body = yaml.safe_load(f.read())
        url = 'https://10.0.31.48:6443/api/v1/namespaces/{namespace}/pods'.format(namespace=namespace)
        res = requests.post(url=url,headers=self.headers,json=body,verify=False)
        print(res.status_code)

    def get(self,pod_name,namespace):
        url = 'https://10.0.31.48:6443/api/v1/namespaces/{namespace}/pods/{pod_name}'.format(namespace=namespace,pod_name=pod_name)
        res = requests.get(url,headers=self.headers,verify=False)
        return yaml.dump(res.json())


if __name__ == '__main__':
    pod = Pod()
    pod.create(yamlFile='./test.yaml',namespace='default')
    pod.get(pod_name='pod-nginx2',namespace='default')



