from openstack import connection
import json,argparse,yaml

conn = connection.Connection(
    auth_url = 'http://172.129.78.57:5000/v3/',
    project_name='admin',
    domain_name='demo',
    username='admin',
    password='000000'
)

def create():
    args_input = args.input
    print(json.dumps(conn.create_user(name = args_input["name"],password = args_input["password"],domain_id="c21040ff81da4e6686421f54d82e9b30",description=args_input["description"])))

def get():
    print(json.dumps(conn.get_user(name_or_id=args.name)))
    if args.output:
        with open(args.output, 'w') as f:
            f.write(json.dumps(conn.get_user(name_or_id=args.name)))
def getall():
    with open(args.output, 'w') as f:
        for i in conn.list_users():
            print(json.dumps(i))
            if args.output:
                f.write(yaml.dump(dict(i)))
def delete():
    print(json.dumps(conn.delete_user(name_or_id=args.name)))

if __name__ == '__main__':
    parsers = argparse.ArgumentParser(description='用户帮助信息')
    subparser = parsers.add_subparsers(help='子命令帮助')

    create_user = subparser.add_parser('create',help='创建用户')
    create_user.add_argument('-i','--input',type=json.loads,required=True,help='json 格式用户数据')
    create_user.set_defaults(func=create)

    get_user = subparser.add_parser('get',help='根据id查询用户')
    get_user.add_argument('-n','--name',type=str,help='指定名称')
    get_user.add_argument('-o','--output',help='用户信息输出到文件，格式为json')
    get_user.set_defaults(func=get)

    getall_user = subparser.add_parser('getall',help='查询所有用户')
    getall_user.add_argument('-o','--output',help='输出用户信息到文件中，格式为yaml')
    getall_user.set_defaults(func=getall)

    delete_user = subparser.add_parser('delete',help='根据id删除用户')
    delete_user.add_argument('-n','--name',type=str,help='指定名称查询')
    delete_user.set_defaults(func=delete)
    args = parsers.parse_args()
    args.func()

