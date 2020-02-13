# -*- coding:utf-8 -*-
# @Time : 2020/2/13 12:48
# @Author : naihai

"""
阿里域名解析更新脚本 无需浏览器手动设置

使用说明:
pip install aliyun-python-sdk-domain
登录阿里云 获取Acs密钥

参考文档
https://help.aliyun.com/document_detail/29776.html?spm=a2c4g.11186623.2.37.d31b31dfNqojPT
"""

import json

from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

ACCESS_KEY_ID = "xxx"
ACCESS_KEY_SECRET = "xxx"
REGION_ID = "cn-hangzhou"


class DNSUpdater(object):
    def __init__(self, domain, rr_key_word, value_key_word):
        self.domain = domain
        self.rr_key_word = rr_key_word
        self.value_key_word = value_key_word

        self.client = AcsClient(ak=ACCESS_KEY_ID, secret=ACCESS_KEY_SECRET, region_id=REGION_ID)
        self.request = CommonRequest(domain="alidns.aliyuncs.com", version="2015-01-09")
        self.record_id = None
        self.get_record_id()

    def get_record_id(self):
        self.request.set_accept_format('json')
        self.request.set_method('POST')
        self.request.set_action_name('DescribeDomainRecords')
        self.request.add_query_param('DomainName', self.domain)
        self.request.add_query_param('RRKeyWord', self.rr_key_word)  # 主机记录关键字 例如www blog
        self.request.add_query_param('TypeKeyWord', 'A')  # 解析类型的关键字

        try:
            response = self.client.do_action_with_exception(self.request)
            encode_json = json.loads(response)
            self.record_id = encode_json['DomainRecords']['Record'][0]['RecordId']  # 需要获取这个RecordId
        except ServerException as e:
            print(e.message)
            exit(1)

    def update(self):
        self.request.set_action_name('UpdateDomainRecord')
        self.request.add_query_param('RecordId', self.record_id)
        self.request.add_query_param('RR', self.rr_key_word)
        self.request.add_query_param('Type', 'A')
        self.request.add_query_param('Value', self.value_key_word)
        try:
            response = self.client.do_action_with_exception(self.request)
            print("update record succeed")
        except ServerException as e:
            print(e.message)
            exit(1)


if __name__ == "__main__":
    DNSUpdater("zhfsky.com", "www", "xxx").update()
