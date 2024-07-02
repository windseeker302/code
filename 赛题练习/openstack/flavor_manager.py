from openstack import connection
import json,argparse

conn = connection.Connection(
    auth_url = 'http://172.129.78.57:5000/v3/',
    project_name = 'admin',
    domain_name = 'demo',
    username = 'admin',
    password = '000000'
)

def create():
    print(json.dumps(conn.create_flavor(args.name,args.ram,args.vcpus,args.disk,flavorid=args.id)))

def getall():
    result = conn.list_flavors()
    for i in result:
        print(json.dumps(i))

def get():
    print(json.dumps(conn.get_flavor(args.id)))
def delete():
    print(json.dumps(conn.delete_flavor(args.id)))


if __name__ == "__main__":
    parses = argparse.ArgumentParser(description='openstack flavor 管理')
    subparse = parses.add_subparsers(required=True,help='子命令帮助信息')
    create_flavor = subparse.add_parser('create',help='创建 flavor')
    create_flavor.add_argument('-n','--name',help='指定flavor名称',required=True,type=str)
    create_flavor.add_argument('-m', '--ram', help='指定内存大小,单位M', required=True, type=int)
    create_flavor.add_argument('-v', '--vcpus', help='指定cpu个数', required=True, type=int)
    create_flavor.add_argument('-d', '--disk', help='指定磁盘大小，单位G', required=True, type=int)
    create_flavor.add_argument('-id', '--id', help='指定flavor id', required=True, type=str)
    create_flavor.set_defaults(func=create)

    getall_flavor = subparse.add_parser('getall',help='查询所有flavor')
    getall_flavor.set_defaults(func=getall)

    get_flavor = subparse.add_parser('get',help='根据id查询flavor')
    get_flavor.add_argument('-id',required=True,type=str)
    get_flavor.set_defaults(func=get)

    delete_flavor = subparse.add_parser('delete',help='根据id删除flavor')
    delete_flavor.add_argument('-id',required=True,type=str)
    delete_flavor.set_defaults(func=delete)

    args = parses.parse_args()
    args.func()
