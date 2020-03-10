# ownklok
PoCs for vulnerabilities in the OKLOK (3.1.1) mobile companion app for Fingerprint Bluetooth Padlock FB50 (2.3).


### CVE-2020-8790
The OKLOK (3.1.1) mobile companion app for Fingerprint Bluetooth Padlock FB50 (2.3) has weak password requirements combined with improper restriction of excessive authentication attempts, which could allow a remote attacker to discover user credentials and obtain access via a brute force attack.

### CVE-2020-8791
The OKLOK (3.1.1) mobile companion app for Fingerprint Bluetooth Padlock FB50 (2.3) allows remote attackers to submit API requests using authenticated but unauthorized tokens, resulting in IDOR issues. A remote attacker can use their own authenticated token to make unauthorized API requests on behalf of arbitrary user IDs. Valid and current user IDs are simple to guess because of the user ID assignment pattern used by the app. A remote attacker could harvest email addresses, unsalted MD5 password hashes, owner-given lock names, and owner-given fingerprint names for any list of arbitrary user IDs.

### CVE-2020-8792
The OKLOK (3.1.1) mobile companion app for Fingerprint Bluetooth Padlock FB50 (2.3) has an information-exposure issue. An attempt to add an already-bound lock by its barcode in the app reveals the email address of the account to which the lock is bound, as well as the name of the lock. Valid barcode inputs can be easily guessed because barcode strings follow a predictable pattern. Correctly guessed valid barcode inputs entered through the app interface disclose a user's email address and lock name, while correctly guessed valid barcode inputs entered via specially crafted API requests, used in conjunction with the userID IDOR vulnerability in CVE-2020-8791, reveal account information including email addresses, unsalted MD5 password hashes, owner-given lock names, and owner-given fingerprint names for any list of arbitrary user IDs. 

# Requirements

# Disclaimer

# Disclosure Notes

# Acknowledgments
remember to acknowledge securelayer7 here (CVE-2019-13143)
