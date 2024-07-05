import argparse,json
import main as ecs

# 定义子命令处理函数


def create(args):
    print("正在创建 ecs")
    ecs.create(server_name=args.name)


def get(args):
    print("正在查找")
    ecs.get(args.name)


def getall(args):
    print("正在查找所有")
    ecs.get()

def delete(args):
    print("正在删除")
    ecs.delete(args.delete)
    

# 
parser = argparse.ArgumentParser(description='我是程序帮助，会显示在 -h 或 --help 中')


# 添加子命令
subparsers = parser.add_subparsers(dest='subcommand', required=True)


# 添加位置参数的选项之一
parser_create = subparsers.add_parser('create', help='创建ecs')

# 位置参数下所需的参数
parser_create.add_argument('-i',"--input", required=True, help='json格式ecs配置',type=str)
parser_create.set_defaults(func=create)


# 添加位置参数的选项之一
parser_get = subparsers.add_parser('get', help='选项ces的配置')
parser_get.add_argument('-n','--name', help='指定查询名称')
parser_get.add_argument('-o','--output', help='将输出信息保存到文件')
parser_get.set_defaults(func=get)


# 添加位置参数的选项之一
parser_getall = subparsers.add_parser('getall', help='获取所有ecs配置')
parser_getall.add_argument('-o','--output', help='将输出信息保存到文件')
parser_getall.set_defaults(func=getall)


# 添加位置参数的选项之一
parser_delete = subparsers.add_parser('delete', help='删除指定ecs')
parser_delete.set_defaults(func=delete)

args = parser.parse_args()
args.func(args)
