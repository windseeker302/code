
# 参考文档：https://kubernetes.io/zh-cn/docs/tasks/administer-cluster/access-cluster-api/#%E7%9B%B4%E6%8E%A5%E8%AE%BF%E9%97%AE-rest-api
import requests,yaml,urllib3,json
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://10.0.31.48:6443/apis/apps/v1/namespaces/default/deployments'
with open('./token.txt') as f:
    token = "bearer " + f.read()

headers = {
    "Content-Type": "application/json",
    'Authorization': token
}
with open("test.yaml",encoding="utf-8") as f:
    body = yaml.safe_load(f)


if __name__ == '__main__':
    # 创建 deploy
    response = requests.post(url, headers=headers, json=body, verify=False)
    print(response.json())

    # 删除 deploy
    # delete_deploy_name = "test"
    # delete_url = url + f"/{delete_deploy_name}"
    # requests.delete(delete_url,headers=headers,verify=False)

    # 查看 deploy
    get_res = requests.get(url, headers=headers,verify=False)
    dict_name = get_res.json()
    dict_name = yaml.dump(dict_name)
    print(dict_name)