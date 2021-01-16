#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (C) 2021 All rights reserved.
#
# @Author Kaco
# @Version 1.0
from api import api_client
if __name__ == '__main__':


    # 查询用户信息
    # result = api_client.get_user_info(username="kisksis")
    # 启用禁用用户
    # result = api_client.set_user_enable(username="kisksis",enable=1)
    # 添加用户
    result = api_client.add_user_cloud(name="kisksis",note="接口",phone="13800138000")
    # 修改用户
    # result = api_client.update_user_cloud(old_name="kisksis",new_name="jenkis",parent_group="/默认用户组",note="kaco",is_enable=0)
    # 删除用户
    # result = api_client.del_user_by_name_cloud(names="kisksis")
    # 获取用户列表
    # result = api_client.get_search_data()
    # 断开用户连接
    # result = api_client.kill_online_user_cloud(users="kisksis")
    # 获取在线用户信息
    # result = api_client.get_online_user_cloud(parent_group="/")
    print(result)
