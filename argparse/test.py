import argparse

# # 创建解释器
# parser = argparse.ArgumentParser()


# # 添加子命令
# subpareser = parser.add_subparsers(help='子命令帮助信息')
# parser_create = subpareser.add_parser('create',help="创建实力规格")
# parser_create.add_argument('-n','--name',help="指定flavor名称",required=True,type=str)



# # 添加参数
# parser.add_argument('create',type=str,help='create')
# parser.add_argument('--a',type=int,help='operator A')
# parser.add_argument('--b',type=int,help='operator B')

# # 解析命令行
# args = parser.parse_args()
# print(args.a * args.b)


parser = argparse.ArgumentParser(description="Openstack flavor管理")
# parser.add_argument('-n','--name',help='名称')
# 子命令
subparsers = parser.add_subparsers(help='子命令帮助信息')
# create：创建实例规格
parser_create = subparsers.add_parser("create", help="创建实例规格")
parser_create.add_argument("-n", "--name", help="指定flavor名称", required=True, type=str)
parser_create.add_argument("-m", "--ram", help="指定内存大小，单位M", required=True, type=int)
parser_create.add_argument("-v", "--vcpus", help="指定虚拟cpu个数", required=True, type=int)
parser_create.add_argument("-d", "--disk", help="磁盘大小单位G", required=True, type=int)
parser_create.add_argument("-id", help="指定ID", required=True, type=str)


# get：根据id获取flavor
parser_get = subparsers.add_parser("get", help="根据id获取flavor信息")
parser_get.add_argument("-id", help="指定flavorID", required=True, type=str)


args = parser.parse_args()
