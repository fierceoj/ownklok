# User Recommendations

Given the security vulnerabilities in the OKLOK mobile application, users should be aware of the following warnings and recommendations:

- Any lock that uses the OKLOK mobile app should not be relied on to secure anything valuable. It is trivial for an attacker to unlock the lock using one of several working methods. 
- An attacker can obtain user information for any arbitrary (non-targeted) user account. 
  - Do not use a password for the OKLOK app that you use elsewhere (It is bad security practice to reuse passwords in general). 
  - Do not use personally identifying names for the lock, fingerprints, or account nickname.
  - Do not register an OKLOK account with an email address that you wish to keep private.
- Legitimate OKLOK emails come from app[@]oklock[.]net with an originating IP address in the 198.11.142.0/24 range (Alibaba). OKLOK sends automated emails for verification codes for the FB50 2.3 lock. They do not send emails regarding suspicious activity on an account.  
  - Be vigilant of OKLOK phishing emails and social engineering tactics. Attackers can easily obtain real user account information and use it in the email as a pretext to make the email seem legitimate.
  - Be aware that an attacker could tamper with your account or lock, and then send an email notifying you of the suspicious activity on your account. An attacker could use the email to deliver a malicious payload or phishing link.
- The vendors have not acknowledged the vulnerabilities or expressed any plans to patch them.
  
In summary, to mitigate some of the possible attacks and privacy issues, use a strong and unique password, use a junk email address to register the account, do not use personally identifying names anywhere in the app, and be aware of the phishing opportunities available to an attacker. Understand that even with these mitigatations:
  - An attacker can still open the lock if in physical proximity.
  - An attacker can still bypass account verification to change an account's password, granting the attacker access to the OKLOK account and the lock. 
  - An attacker can still remotely unbind any lock from any OKLOK user account and bind it to their own, thereby making the app's bind/unbind and unlock functions inaccessible through the app for the original owner.
