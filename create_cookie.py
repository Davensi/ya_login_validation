import requests
from util import getCode
from util import generate_twk_uuid
from util import generate_phpsessid


# 请求地址
baseUrl = "https://www.yaeei.com/"
# 创建一个会话对象，用于模拟会话
session = requests.Session()

# 生成 cookies 字典
cookies = {
    "PHPSESSID": "md5fefp045nohzoyvvdvp0a6ck", 
    "TawkConnectionTime": "0",
    "twk_uuid_%7B%22uuid%22%3A%20%221.V2HrVVwTKQCOvcvHwvXe7dKg%22%2C%20%22version%22%3A%203%2C%20%22domain%22%3A%20%22yaeei.com%22%2C%20%22ts%22%3A%201731640971768%7D": "%7B%22uuid%22%3A%20%221.OTPke7AJghlmS4csl0Zpsy0UePGzkiZlJNBnL8pkroIQ4kq3Iz9mMdlChYPUniYKBQpX1ocfeygMihIumesW4l%22%2C%20%22version%22%3A%203%2C%20%22domain%22%3A%20%22yaeei.com%22%2C%20%22ts%22%3A%201731640971768%7D"
    # "PHPSESSID": "md5" + generate_phpsessid(23), 
    # "TawkConnectionTime": "0",
    # "twk_uuid_" + generate_twk_uuid(24): generate_twk_uuid(86)
}

# 设置 headers 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

print("模拟的 cookies:", cookies)


 # 目标 URL 替换为你要访问的 URL
url = baseUrl+"/api.php/basis/getConf"  # 请将 your_endpoint 替换为实际的访问路径

# 向目标 URL 发送带有 cookies 和 headers 的 GET 请求
response = session.get(url, headers=headers, cookies=cookies)

# 检查响应状态码是否为 200
if response.status_code == 200:
    print("请求成功")
    print("响应内容：", response.text)
else:
    print(f"请求失败，状态码: {response.status_code} ",response)
# 输出生成的 cookies

verifyUrl = baseUrl + "/api.php/login/verify" 
response2 = session.get(verifyUrl, headers=headers, cookies=cookies)
verifyPath = "./captcha_image.jpg"
# 检查请求是否成功
if response2.status_code == 200:
    # 将图片数据写入文件
    with open(verifyPath, "wb") as file:
        file.write(response2.content)
    print("验证码图片已成功保存为",verifyPath)
else:
    print(f"请求失败，状态码: {response2.status_code}")
    
# 解析图形验证码
 
verifyCode = getCode(verifyPath)

print("当前验证码---->",verifyCode)

loginUrl = baseUrl+"/api.php/login/login" 
def login (url,headers,cookies):
    loginResponse = session.post(url, headers=headers, cookies=cookies, data={
        "cipher":verifyCode,
        "phone": "15xxxxx",
        "password": "1887722",
        "code_id": 9,
    }                                 
)
    return loginResponse
def loopLogin(loginUrl,headers,cookies):
    loginResponse = login(loginUrl,headers,cookies)
    if loginResponse.status_code == 200:
        print("登录成功",loginResponse.text)
        return loginResponse
    else:
        print("验证失败",loginResponse.text)
        return login(loginUrl,headers,cookies)
    
    
    
text = loopLogin(loginUrl,headers,cookies)
print(text.text)
# # 检查请求是否成功
# if loginResponse.status_code == 200:
#     print("登录成功",loginResponse.text)
# else:
#     print(f"登录失败，状态码: {loginResponse.status_code}-->{loginResponse.text}")