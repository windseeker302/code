import yaml
from kubernetes import client, config


config.load_kube_config(config_file="./config.yaml")
v1 = client.BatchV1Api()

with open("test2.yaml",encoding='utf-8') as f:
    crondata = yaml.safe_load(f)
v1.create_namespaced_job(namespace="default",body=crondata)
v1.read_namespaced_job(name="pi",namespace="default")



if __name__ == "__main__":
    pass


