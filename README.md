# ownklok
PoCs for vulnerabilities in the OKLOK (3.1.1) mobile companion app for Fingerprint Bluetooth Padlock FB50 (2.3). 
```CVE-2020-8790``` <br/>
```CVE-2020-8791``` <br/>
```CVE-2020-8792```

Tested on iOS.

This repo also contains a full attack demo (attack_demo.py) to illustrate an attack scenario which combines the CVE-2020-8791 exploit and a modified version of the [CVE-2019-13143](https://blog.securelayer7.net/fb50-smart-lock-vulnerability-disclosure/) exploit ([pwnfb50.py](https://github.com/securelayer7/pwnfb50/blob/master/pwnfb50.py)).

# Requirements
- python3 <br/>
- requests

# Legal Disclaimer
This project is made for educational and ethical testing purposes only. Usage of ownklok scripts for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

# Disclosure Notes
- 1st outreach to vendors on 1/20/2020 <br/>
- CERT/CC notified on 1/29/2020 <br/>
- 2nd outreach to vendors, CNCERT/CC notified on 1/31/2020 <br/>
- CVEs reserved on 2/7/2020 <br/>
- Publicly disclosed on 4/30/2020 <br/>
<br/>
There has been no response from the vendors.

# Acknowledgments
IDOR issues similar to CVE-2020-8791 were noted in prior research on similar locks/apps:
- Android Nokelock app research by [Pen Test Partners](https://www.pentestpartners.com/security-blog/pwning-the-nokelock-api/)
- Android Nokelock app research by [SecureLayer7](https://blog.securelayer7.net/fb50-smart-lock-vulnerability-disclosure/)
- 

remember to acknowledge securelayer7 here (CVE-2019-13143)
