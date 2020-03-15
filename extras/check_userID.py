#!/usr/bin/env python3

#Code to check the userID of your OKLOK account

import requests
import json
import sys
import getpass

#login to the account
#grab and print the userID
def acct_login(email_address, password):
    
    url = 'https://app.oklok.com.cn/oklock/user/loginByPassword'
    body = {"code":password,"account":email_address,"type":"0"}

    login_headers = {'Host': 'app.oklok.com.cn',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'OKLOK/3.1.1 (iPhone; iOS 13.3; Scale/2.00)',
    'Accept-Language': 'en-US;q=1',
    'Content-Length': '70',
    'Accept-Encoding': 'gzip, deflate, br'}

    print('\n-------------------------------------------------------------')
    print('Logging in...')
    
    response = requests.post(url, data=json.dumps(body), headers=login_headers)
    json_resp = response.json()
    status = json_resp['status']
    if status == '2000':
        print('Login successful!\n')
        result = json_resp['result']
        userID = result['userId']
        print('userId: ' + str(userID))
        print('-------------------------------------------------------------\n')

    else:
        sys.exit('Login not successful.')


def main():

    if len(sys.argv) is not 2:
        sys.exit('Usage: python3 check_userID.py <email_address>')
    else:
        email_address = sys.argv[1]
        password = getpass.getpass('Password: ')
        acct_login(email_address, password)

if __name__ == '__main__':
    main()
