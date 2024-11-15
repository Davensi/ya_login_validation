import secrets
import string
import json
import urllib.parse
import time
import ddddocr
# 解析图形验证码
def getCode(path):
    if path == '':
        return '' 
    
    ocr = ddddocr.DdddOcr()
    with open(path, 'rb') as f:
        img_bytes = f.read()
        verifyCode = ocr.classification(img_bytes)
        return verifyCode
 
 # 生成一个类似 PHPSESSID 的随机字符串
def generate_phpsessid(lne=23):
    characters = string.ascii_lowercase + string.digits  # PHPSESSID 通常为小写字母和数字
    phpsessid = ''.join(secrets.choice(characters) for _ in range(lne))
    return phpsessid

# 生成一个类似 twk_uuid_* 的字段
def generate_twk_uuid(len=86):
    # 模拟 UUID 部分的随机字符串
    uuid_part = '1.' + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(len))

    # 获取当前的时间戳
    timestamp = int(time.time() * 1000)

    # 生成 twk_uuid 内容
    twk_uuid_content = {
        "uuid": uuid_part,
        "version": 3,
        "domain": "yaeei.com",
        "ts": timestamp
    }

    # 将内容转换为 JSON 字符串并进行 URL 编码
    twk_uuid_encoded = urllib.parse.quote(json.dumps(twk_uuid_content))
    return twk_uuid_encoded
