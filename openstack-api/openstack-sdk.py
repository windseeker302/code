import argparse,json
from openstack import connection

conn = connection.Connection(
            auth_url = 'http://172.129.78.57:5000/v3/',
            project_name = 'admin',
            domain_name = 'demo',
            username = 'admin',
            password = '000000'
        )
def createFlavor():
    print(json.dumps(conn.create_flavor(args.n,args.m,args.v,args.d,flavorid=args.id)))

def getFlavor():
    # conn.get_flavor_by_id(args.id)
    print(json.dumps(conn.get_flavor_by_id(id=args.id)))

def getallflavor():
    for i in conn.list_flavors():
        print(json.dumps(i))

def deleteFlavor():
    conn.delete_flavor(args.id)


# 解析命令行参数和选项
parser = argparse.ArgumentParser(description='我是程序帮助，会显示在 -h 或 --help 中')

subpareser = parser.add_subparsers(help='子命令帮助信息',required=True)

# 位置参数 create
create_flavor = subpareser.add_parser('create',help='创建实例规格')
create_flavor.add_argument('-n',help='指定 flavor 名称',type=str,required=True)
create_flavor.add_argument('-m',help='指定内存大小，单位M',type=int,required=True)
create_flavor.add_argument('-v',help='指定虚拟cpu个数',type=int,required=True)
create_flavor.add_argument('-d',help='指定磁盘大小，单位G',type=int,required=True)
create_flavor.add_argument('-id',help='指定ID',type=str)
create_flavor.set_defaults(func=createFlavor)

# 位置参数 getall
getall_flavor = subpareser.add_parser('getall',help='获取实例规格')
getall_flavor.set_defaults(func=getallflavor)

# 位置参数 get
get_flavor = subpareser.add_parser('get',help='获取实例规格')
get_flavor.add_argument('-id',type=str,help='指定ID查询')
get_flavor.set_defaults(func=getFlavor)

# # 位置参数 delete
delete_flavor = subpareser.add_parser('delete',help='删除实例规格')
delete_flavor.add_argument('-id',type=str,help='指定ID删除')
delete_flavor.set_defaults(func=deleteFlavor)


args = parser.parse_args()
# 根据不同的子命令执行不同的函数，传入args参数
args.func()