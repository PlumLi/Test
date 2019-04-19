#!/venv/bin/python
# -*- coding: utf-8 -*-
# @Time    : 4/18/19 9:34 PM
# @Author  : PlumLi
# @Contact : jing_li@subin.cn
# @File    : sacncode.py
# @esc     :

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import random, string
from Crypto.Cipher import AES
import os
import base64

# 用aes加密，再用base64  encode
def aes_encrypt(data):
    from Crypto.Cipher import AES
    import base64
    key = '2018061509562333' # 加密时使用的key，只能是长度16,24和32的字符串
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(key)
    encrypted = cipher.encrypt(pad(data))  # aes加密
    result = base64.b64encode(encrypted)  # base64 encode
    return result


#把加密的数据，用base64  decode，再用aes解密
def aes_decode(data):
    key='2018061509562333'

    unpad = lambda s:s[0:-ord(s[-1])]
    cipher = AES.new(key)
    result2 = base64.b64decode(data)
    print(cipher.decrypt(result2))

    #decrypted = unpad(cipher.decrypt(result2))
    #return  decrypted


result = aes_encrypt('action=enter&channel=1&parkid=0218')

result = result.decode()

result1 = aes_decode(result)
print(result)
