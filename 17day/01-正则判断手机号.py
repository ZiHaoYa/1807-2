import re

# 验证手机号是否正确

phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')

while True:
    phone = input('请输入您的手机号:')

    res = re.search(phone_pat, phone)
    if res:
        print('正常手机号')
    else:
        print('不是手机号')
