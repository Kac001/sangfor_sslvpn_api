#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (C) 2021 All rights reserved.
#
# @Author Kaco
# @Version 1.0
from .utils import http_call


def data_sync_cloud():
    '''
    数据备份与生效接口
    注意事项:
    接口调用时使用了 delay_flush 字段后，都需要调用数据备份与生效接口，否则之前的
    操作无效，例如:
    调用新建用户的接口新建了用户 user1，如果没有调用数据备份与生效接口，将出现如下两种情况:
    1)user1 信息无法备份，在集群或单台 VPN 设备环境下数据同步会出现差异。
    2)user1 无法成功登录到 VPN。
    :return:
    '''
    url = 'controler=Updater&action=DataSyncCloud'
    responce = http_call(url)
    return responce


'''
用户接口
调用新建、编辑接口的时候会填入相关参数，但是在获取用户信息的时候并不一定返回
新建、编辑接口时的参数字段。
'''


def get_user_info(username):
    '''
    用户接口-查询用户
    :param usernme:用户名
    :return:
    '''
    url = 'controler=User&action=ExGetUserInfo'
    params = {'username': username}
    responce = http_call(url, params)
    return responce


def set_user_enable(username, enable):
    '''
    用户接口-用户启用和禁用接口
    :param username: 用户名(必填字段)
    :param enable:  启用或禁用(1:启用，0: 禁用)
    :return:
    '''
    url = 'controler=User&action=ExtSetUserEnable'
    params = {'username': username,
              'enable': enable}
    responce = http_call(url, params)
    return responce


def update_user_cloud(old_name, new_name, parent_group, delay_flush=0, **kwargs):
    '''
    用户接口-编辑用户
    :param old_name:旧用户名，最大长度 48 字节 不能以“,”开头
    :param new_name:新用户名，最大长度 48 字节 不能以“,”开头
    :param parent_group:用户所属组全路径，(如: /aa/bb)
    :param delay_flush: 延迟立即生效、延迟刷新数据库(1:延迟;0:不延迟) 默认为0，
                        如需使用，调用本接口后需要调用数据备份与生效接口，否则之前的操作无效
    :param kwargs: 其他可选参数，详见api文档
    :return:
    '''
    url = 'controler=User&action=UpdateUserCloud'
    params = {'old_name': old_name,
              'new_name': new_name,
              'parent_group': parent_group,
              "delay_flush": delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


def add_user_cloud(name, parent_group='/默认用户组', note="", phone="", delay_flush=0, **kwargs):
    '''
    用户接口-添加用户
    :param name: 用户名，最大长度 48 字节不 能以“,”开头
    :param parent_group:用户所属组全路径
    :param note:描述，长度 48 字节
    :param phone:手机号码，最大长度 30 个字 节，多个手机号使用英文分 号隔开
    :param delay_flush: 延迟立即生效、延迟刷新数据库(1:延迟;0:不延迟) 默认为0，
                        如需使用，调用本接口后需要调用数据备份与生效接口，否则之前的操作无效
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = 'controler=User&action=AddUserCloud'
    params = {'name': name,
              'parent_group': parent_group,
              'note': note,
              'phone': phone,
              "delay_flush": delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


def del_user_by_name_cloud(names, delay_flush=0):
    '''
    用户接口-删除用户
    注意事项:
    1. names 参数可多个，需使用数组格式传参如:user1 或者 user1,user2。
    :param names:       用户名
    :param delay_flush: 延迟立即生效、延迟刷新数据库(1:延迟;0:不延迟) 默认为0，
                        如需使用，调用本接口后需要调用数据备份与生效接口，否则之前的操作无效
    :return:
    '''
    url = "controler=User&action=DelUserByNameCloud"
    params = {'names': names,
              "delay_flush": delay_flush}
    responce = http_call(url, params)
    return responce


def get_search_data(**kwargs):
    '''
    用户接口-获取用户列表
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=User&action=GetSearchData"
    responce = http_call(url, kwargs)
    return responce


def kill_online_user_cloud(users):
    '''
    用户接口-断开用户连接(单个或批量)
    注意事项:
    1. users 参数必须使用数据格式，多个用户必须要用逗号分隔，如:user1 或者 user1,user2。
    :param users: 用户名
    :return:
    '''
    url = "controler=State&action=KillOnlineUserCloud"
    params = {'users': users}
    responce = http_call(url, params)
    return responce


def get_online_user_cloud(parent_group, **kwargs):
    '''
    用户接口-获取在线用户信息
    注意事项:
    1. Parent_group参数传入的为用户组的全路径，如“/SSL/测试组”。
    2. 提交 offset 和 limit 参数的场景:
    例如 offset=1,limit=1000 表示从 1 开始获取 1000 条用户信息;依次传参 offset=1001,limit=1000 即可获取所有用户信息。
    3. 超过 5000 用户时，推荐使用 offset 和 limit 分页获取数据，以免此接口因查询数据太多导 致设备 CPU 上升或者因数据量太大而出现错误。
    :param parent_group:用户组全路径
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=State&action=GetOnlineUserCloud"
    params = {'parent_group': parent_group}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


def move_grp_user_cloud(src_group, dst_group, **kwargs):
    '''
    用户接口-移动用户组或者用户
    注意事项:
    1. groups、users 可同时有或者只有一个，但不能都没有。
    2. src_group 必须要有，dst_group 没有时为根目录。 3.src_group=/group1&dst_group=/group2&groups=/group1/g11,/group1/g12&users=user1,user &sinfor_apitoken=4b0c........ac5b109。
    上述操作会将 group1 用户组下的 g11 和 g12 用户组，以及 group1 用户组下的 user1 和 user2 移动到 group2 用户组下。
    5. Users的搜索范围是用户管理中的全部用户，并不是根据特定的路径去搜索。
    :param src_group:原父级用户组全路径
    :param dst_group:新父级用户组全路径
    :param **kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Group&action=MoveGrpUserCloud"
    params = {'src_group': src_group,
              'dst_group': dst_group}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


'''
用户组接口
调用新建、编辑接口的时候会填入相关参数，但是在获取用户组信息的时候并不一定返
回新建、编辑接口时的参数字段。
'''


def add_group_cloud(name, parent_group,delay_flush=0, **kwargs):
    '''
    用户组接口-新建用户组
    注意事项:
    1. 不能在默认用户组匿名用户组下新建用户组
    2. 需要配置 ext_auth_id 时,同时设置 is_extauth 为 1
    3. 需要配置 token_svr_id 时,同时设置 is_token 为 1 4. VPN 中已经存在的用户组 id:
    "/"(根组) id 值为:-100; "匿名用户组" id 值为:-2; "默认用户组" id 值为:-1; "根目录的父级用户组"id 值为:-101;
    :param name:用户组名，最大长度 96 字节，不能 以“,”开头
    :param parent_group:用户组父组全路径
    :param delay_flush:延迟立即生效、延迟刷新数据库(1: 延迟;0:不延迟) 注:非1当做0处理
    :param **kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Group&action=AddGroupCloud"
    params = {'name': name,
              'parent_group': parent_group,
              'delay_flush':delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


def set_group_enable(groupname, enable):
    '''
    用户组接口-用户组启用和禁用接口
    :param groupname:传用户组的全路径
    :param enable: 启用或禁用(1:启用，0:禁用)
    :return:
    '''
    url = "controler=Group&action=ExtSetGroupEnable"
    params = {'groupname': groupname,
              'enable': enable}
    responce = http_call(url, params)
    return responce


def get_group_info(group_name):
    '''
    用户组接口-查询用户组
    :param group_name: 需要查询的用户组全路径(如:/某某分公司/IT部)
    :return:
    '''
    url = "controler=Group&action=GetGroupInfo"
    params = {'group_name': group_name}
    responce = http_call(url, params)
    return responce


def update_group_cloud(old_name, new_name, old_parent_group, new_parent_group,delay_flush=0, **kwargs):
    '''
    用户组接口-编辑用户组
    :param old_name: 旧用户组名，最大长度 96 字节，不能以“,”开头
    :param new_name: 新用户组名，最大长度 96 字节，不能以“,”开头
    :param old_parent_group: 老用户组全路径
    :param new_parent_group: 新用户组全路径
    :param delay_flush:延迟立即生效、延迟刷新数据  库(1:延迟;0:不延迟)
    :param **kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Group&action=UpdateGroupCloud"
    params = {'old_name': old_name,
              'new_name': new_name,
              'old_parent_group': old_parent_group,
              'new_parent_group': new_parent_group}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


def delete_group_cloud(names, delay_flush=0):
    '''
    用户组接口-删除用户组
    注意事项:
    1. names 参数可传多个,采用逗号隔开
    2. 用户组名前面必须带上/,如:/测试组或者/测试组,/SSL 部门
    3. 删除用户组时,会把下级用户组和其中的用户全部删除,请慎用
    参数说明:
    :param names: 需要删除的用户组全路径,可传多个,采用逗号隔开,
    :param delay_flush: 延迟立即生效、延迟刷新数据库(1: 延迟;0:不延迟)
    :return:
    '''
    url = "controler=Group&action=DeleteGroupCloud"
    params = {'names': names,
              'delay_flush': delay_flush, }
    responce = http_call(url, params)
    return responce


'''
资源接口
'''


def add_resource_cloud(name, rctype, main_host="", addr_str="",delay_flush=0, **kwargs):
    '''
    资源接口-新建资源
    注意事项:
    1. Rctype的值为0(web资源)时，此时main_host的值为必填，addr_str可不填;当rctype的 值为 1(TCP 资源)或者 2(L3VPN 资源)时，addr_str 为必填项，main_host 可不填;
    2. Addr_str的值可以配置为多个地址，多个地址用逗号分隔，配置多个端口号用/20:80(即放 通 20-80 的端口)，如:https://10.240.0.1/80:81,https://10.240.0.2/80:82
    3. Main_host只能配置一个地址，只用于web资源
    4. Service参数暂时只支持传HTTP和HTTPS，传其他值，会直接默认使用HTTP 5. 建立新版 WEB 资源需要到控制台配置 web 泛域名，否则配置将不能访问资源。
    参数说明:
    :param name:资源名称，最大长度48个字节
    :param rctype:资源类型 0:web资源 1:TCP资源 2:L3VPN资源
    :param main_host:Web资源地址(web资源必填),最大长度254个字节
    :param addr_str:TCP 资源和L3VPN资源的地址最大条数10条
    :param delay_flush:延迟立即生效、延迟刷新数据  库(1:延迟;0:不延迟)
    :param **kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Resource&action=AddResourceCloud"
    params = {'name': name,
              'rctype': rctype,
              'main_host': main_host,
              'addr_str': addr_str}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


def get_resource_data_cloud(name):
    '''
    资源接口-查询资源
    :param name:资源名称
    :return:
    '''
    url = "controler=Resource&action=GetRcDataCloud"
    params = {'name': name, }
    responce = http_call(url, params)
    return responce


def update_resource_cloud(old_name, new_name, rctype, main_host="", addr_str="", delay_flush=0, **kwargs):
    '''
    资源接口-编辑资源
     注意事项:
     1. 编辑资源时，无法改变资源的类型，如 web 资源改为 TCP 资源这种操作是不行的，所以 web 资源在这里 rctype 参数的值需要传 0，tcp 和 l3vpn 资源类型传 1 和 2。
     2. add_str的值可以配置为多个地址，多个地址用逗号分隔，配置多个端口号用/20:80(即放 通 20-80 的端口)，如:https://10.240.0.1/80:81,https://10.240.0.2/80:82。
     3. main_host只能配置一个地址，只用于web资源。
     4. 不修改资源名称，则 old_name 和 new_name 保持一致。
     5. service参数暂时只支持传HTTP和HTTPS，传其他值，会直接默认使用HTTP。
    :param old_name: 资源名称，最大长度 48 个字节
    :param new_name:修改后的资源名称，最大长度 48 个字节
    :param rctype: 资源类型 0:web 资源 1:TCP 资源 2:L3VPN 资源
    :param main_host: Web 资源地址，最大长度 254 个字节
    :param addr_str: TCP 资源和 L3VPN 资源的地 址，最大条数 10 条例如:10.10.10.20/80:80 1.1.1.1-2.2.2.2/80:80 https://www.domain.com:80
    :param delay_flush:延迟立即生效、延迟刷新数据  库(1:延迟;0:不延迟)
    :param **kwargs:其他可选参数，详见api文档
    :return: 
    '''
    url ="controler=Resource&action=UpdateResourceCloud"
    params = {'old_name': old_name,
              'rctype': rctype,
              'main_host': main_host,
              'addr_str': addr_str,
              'new_name':new_name,
              'delay_flush':delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce

def delete_resource_cloud(names,delay_flush=0):
    '''
    资源接口-删除资源
    注意事项:
    1. Names参数可多个，需使用数组格式传参如:web1或者web2,web3。
    2. 目前只提供删除 tcp,l3vpn,web(新版、旧版)资源。
    :param names:资源名称
    :param delay_flush:延迟立即生效、延迟刷新 数据库(1:延迟;0:不 延迟) 注:非1当做0处理
    :return:
    '''
    url = "controler=Resource&action=DeleteResourceCloud"
    params = {'names': names,
              'delay_flush': delay_flush,}
    responce = http_call(url, params)
    return responce


def get_resource_list_data_cloud(**kwargs):
    '''
    资源接口-获取资源列表
    注意事项:
    1. Start和limit用于分页，避免由于查询数据量太大导致cpu上升或者其他错误。
    2. Type控制要显示的资源种类，-1=资源组，0=WEB，1=TCP，2=L3VPN，65535=全部。
    :param **kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Resource&action=GetRcListDataCloud"
    responce = http_call(url, kwargs)
    return responce


'''
角色接口
'''

def get_role_data_cloud(name):
    '''
    角色接口-查询角色
    :param name:角色名称
    :return:
    '''
    url = "controler=Role&action=GetRoleDataCloud"
    params = {'name': name}
    responce = http_call(url, params)
    return responce

def add_role_cloud(name,delay_flush=0,**kwargs):
    '''
    角色接口-新建角色
    注意事项:
    1. 多个用户或者用户组,多个资源或者资源组用逗号,分开,例如: user1,user2
    2. 参数 userNamesStr,grpNamesStr,rcNamesStr,rcGrpNamesStr 中的名称,必须要在 VPN 上面 已经存在的用户名,用户组名,资源名,资源组名才能成功管理,否则虽然创建角色成功,但是角 色不会关联 VPN 上不存在的用户,用户组,资源,资源组
    :param name:角色名称，最大长度 48 个字 节
    :param delay_flush:延迟立即生效、延迟刷新数据 库(1:延迟;0:不延迟) 注:非1当做0处理
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Role&action=AddRoleCloud"
    params = {'name': name,
              'delay_flush': delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce


def update_role_cloud(oldName,newName,delay_flush=0,**kwargs):
    '''
    角色接口-编辑角色
    注意事项:
    1. 多个用户或者用户组,多个资源或者资源组用逗号,分开,例如: user1,user2
    2. 参数 userNamesStr,grpNamesStr,rcNamesStr,rcGrpNamesStr 中的名称,必须要在 VPN 上面
    已经存在的用户名,用户组名,资源名,资源组名才能成功管理,否则虽然创建角色成功,但是角 色不会关联 VPN 上不存在的用户,用户组,资源,资源组
    :param oldName:角色名称
    :param newName:修改后的角色名称，最大长度 48 个字节
    :param delay_flush:延迟立即生效、延迟刷新数据 库(1:延迟;0:不延迟) 注:非1当做0处理
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Role&action=UpdateRoleCloud"
    params = {'oldName': oldName,
              'newName': newName,
              'delay_flush':delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce

def delete_role_cloud(names,delay_flush=0):
    '''
    角色接口-删除角色
    注意事项:
    1. names 参数可多个,多个使用逗号分隔,如:test222,test333
    2. 删除多个角色时,只要一个是已经存在的角色就会返回成功
    :param names:资源名称
    :param delay_flush:延迟立即生效、延迟刷新 数据库(1:延迟;0:不 延迟)非1当做0处理
    :return:
    '''
    url = "controler=Role&action=DeleteRolesCloud"
    params = {'names': names,
              'delay_flush': delay_flush}
    responce = http_call(url, params)
    return responce

def get_role_list_data_cloud(**kwargs):
    '''
    角色接口-获取角色列表
    注意事项:
    1. start和limit用于分页,避免由于查询数据量太大导致cpu上升或者其他错误。
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=Role&action=GetRoleListDataCloud"
    responce = http_call(url, **kwargs)
    return responce


'''
资源组接口
调用新建、编辑接口的时候会填入相关功能参数，但是在获取资源组信息的时候并不一
定返回调用新建、编辑接口时的参数

'''
def add_rc_group_cloud(name,delay_flush=0,**kwargs):
    '''
    资源组接口-新建资源组
    :param name:资源组名，最大长度 48 个字节
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=RcGrp&action=AddRcGrpCloud"
    params = {'name': name,
              'delay_flush': delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce

def get_rc_group_info_cloud(rcGrpName):
    '''
    资源组接口-查询资源组
    :param rcGrpName:资源组名
    :return:
    '''
    url = "controler=RcGrp&action=GetRcGroupInfoCloud"
    params = {'rcGrpName': rcGrpName}
    responce = http_call(url, params)
    return responce

def update_rc_group_cloud(rcGrpName,delay_flush=0,**kwargs):
    '''
    资源组接口-编辑资源组
    :param rcGrpName:资源组名
    :param delay_flush:延迟立即生效、延迟刷新数据 库(1:延迟;0:不延迟) 注:非1当做0处理
    :param kwargs:其他可选参数，详见api文档
    :return:
    '''
    url = "controler=RcGrp&action=EditRcGrpCloud"
    params = {'rcGrpName': rcGrpName,
              'delay_flush': delay_flush}
    params = dict(params, **kwargs)
    responce = http_call(url, params)
    return responce

def delete_rc_group_cloud(rcGrpNames,delay_flush=0):
    '''
    资源组接口-删除资源组(单个或批量)
    :param rcGrpNames:资源组名，多个 资源组名用”,” 分隔，如: rcgroup1,rcgroup 2
    :param delay_flush:延迟立即生效、 延迟刷新数据库 (1:延迟;0: 不延迟) 注:非 1 当做 0 处理
    :return:
    '''
    url = "controler=RcGrp&action=DelRcGrpCloud"
    params = {'rcGrpNames': rcGrpNames,
              'delay_flush': delay_flush}
    responce = http_call(url, params)
    return responce