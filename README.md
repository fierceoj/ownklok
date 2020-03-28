# ownklok
PoC code for vulnerabilities in the OKLOK (3.1.1) mobile companion app for Fingerprint Bluetooth Padlock FB50 (2.3). 
```CVE-2020-8790``` <br/>
```CVE-2020-8791``` <br/>
```CVE-2020-8792``` <br/>
```CVE-2020-10876```

This repo also contains two attack scenarios which combine my CVE-2020-8791 exploit with methods similar to the CVE-2019-13143 PoC by SecureLayer7 ([pwnfb50.py](https://github.com/securelayer7/pwnfb50/blob/master/pwnfb50.py)).

# Requirements
- python3 <br/>
- requests module <br/>

```pip3 install -r requirements.txt```

# Legal Disclaimer
This project is made for educational and ethical testing purposes only. Usage of ownklok scripts for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

# Disclosure Notes
- 1st outreach to vendors on 1/20/2020 <br/>
- CERT/CC notified on 1/29/2020 <br/>
- 2nd outreach to vendors, CNCERT/CC notified on 1/31/2020 <br/>
- CVE-2020-8790, CVE-2020-8791, CVE-2020-8792 reserved on 2/7/2020 <br/>
- CVE-2020-10876 reserved on 3/23/2020 <br/>
- Publicly disclosed on 4/30/2020 <br/>
<br/>
There has been no response from the vendors.

# Acknowledgments
IDOR issues similar to CVE-2020-8791 were expressed in prior research on similar locks/apps:
- [OKLOK mobile app/FB50 lock research](https://blog.securelayer7.net/fb50-smart-lock-vulnerability-disclosure/) by SecureLayer7 
    - CVE-2019-13143 allows an attacker to transfer ownership of the lock from the victim account to the attacker account
- [Nokelock mobile app and lock research](https://www.pentestpartners.com/security-blog/pwning-the-nokelock-api/) by Pen Test Partners
- [Klic mobile app/Tzumi Klic lock research](https://github.com/whitehatdefenses/KlicUnLock) by WhiteHat Defenses
    - CVE-2019-11334 allows a physically proximate attacker to unlock the lock
    
# Other Notes
Tested against iOS mobile app.
