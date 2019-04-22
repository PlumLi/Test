#!/venv/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 下午3:20
# @Author  : PlumLi
# @Contact : 
# @File    : APITest.py
# @esc     : 
from Crypto.Cipher import AES
import binascii
import json
import time
from pymongo import MongoClient


#AES 加密 解密
class AESHandle:
    def __init__(self):
        self.key = '2018061509562333'
        self.iv = self.key
        self.mode = AES.MODE_CBC

    def encrypt(self, data):
        """aes加密函数，如果data不是16的倍数，就补足"""
        cipher = AES.new(self.key, self.mode, self.key)  # 设置AES加密模式 此处设置为CBC模式
        block_size = AES.block_size
        # 判断data是不是16的倍数，如果不是用b'\0'补足
        if len(data) % block_size != 0:
            add = block_size - (len(data) % block_size)
        else:
            add = 0
        data += '\0' * add
        encrypted = cipher.encrypt(data)  # aes加密
        result = binascii.b2a_hex(encrypted).decode()  # b2a_hex encode  将二进制转换成16进制
        return result

    def decrypt(self, data):
        """解密"""
        cipher = AES.new(self.key, self.mode, self.key)
        result = binascii.a2b_hex(data)
        decrypted = cipher.decrypt(result)
        return decrypted.decode().rstrip('\0')


class SendData:

    #构建json
    def __init__(self, data, parkid):
        self.data = data
        self.parkid = parkid

    def create_json(self):
        parameters = {
            'user': 'subin',
            'sign': 'sign',
            'timestamp': int(round(time.time() * 1000)),
            'data': self.data,
            'version': '1.0',
            'method': 'method',
            'requesttoken': 'requesttoken'
        }
        if self.data.index('E') > 0:
            parameters['methond'] = 'scanbarcodeentry'
        elif self.data.index('K') > 0:
            parameters['methond'] = 'scanbarcodeexit'
        return json.dumps(parameters)

    def find_URL(self):
        client = MongoClient(
            host="127.0.0.1",
            port=27017,
        )
        db = client.park
        collection = db.park_management
        msg = collection.find_one({'park_id': self.parkid})
        return msg.get('server')

    def postdata(self, data=create_json(), url=find_URL()):
        #发送数据
        pass

