#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (C) 2021 All rights reserved.
#
# @Author Kaco
# @Version 1.0
from config import API_KEY,API_SERVER,SSL_ENABLE
import time
import hashlib
import requests
import logging
from urllib.parse import urlencode, parse_qs, unquote


def make_api_token(param, time_stamp):
    params = str(param) + str(time_stamp) + API_KEY
    s = hashlib.sha256()
    s.update(params.encode("utf8"))
    return s.hexdigest()


def http_call(url, params={}):
    # 获取unix时间
    time_stamp = str(time.time())[:10]
    # url转dict 合并params为一个数组
    params.update(dict([(k, v[0]) for k, v in parse_qs(url).items()]))
    # 时间戳插入params
    params['timestamp'] = time_stamp
    # 数组进行排序
    params = make_dict(params)
    # 数组转换为url编码
    params_str = urlencode(params)
    params_str = unquote(params_str)
    # 提供params的url编码 unix时间生成token
    api_token = make_api_token(params_str, time_stamp)
    # token插入到原parsms
    params['sinfor_apitoken'] = api_token
    # 删除无关参数
    params.pop('action')
    params.pop('controler')
    # print(params)
    # 拼接请求url
    request_url = API_SERVER + '/cgi-bin/php-cgi/html/delegatemodule/WebApi.php?' + url
    # 禁用ssl证书方式请求 ，避免出错
    if SSL_ENABLE == False:
        requests.packages.urllib3.disable_warnings()
    # 设置header
    headers = {'Content-Type': "application/x-www-form-urlencoded", "charset": "UTF-8"}
    response = requests.post(request_url,
                             params, verify=SSL_ENABLE, headers=headers).json()
    if 'error' in response:
        logging.error("深信服API调用失败,错误:" + response['message'])
        return response

    if response['code'] == 0:
        return response
    else:
        logging.error("深信服API调用失败,错误:" + response['message'])
        return response
        # 错误处理


def make_dict(mydict):
    new_dict = sorted(mydict.items(), key=lambda d: d[0])
    new_dict = dict(new_dict)
    return new_dict
