# attack_scenario_remote.py
In this scenario, a remote attacker acquires sensitive user info from arbitrary users, unbinds their locks, and binds them to the attacker's account. Such a scenario would provide ample opportunity for successful large-scale phishing/malspam attacks against OKLOK users because the attacker would be in possession of user account information that he/she could utilize in the email to make it seem more legitimate. The attack_scenario_remote.py script creates a csv file called 'userdata.csv', which contains the email address, lock name, fingerprint name, and barcode of the victim account. 

# attack_scenario_proximate.py
In this scenario, a physically proximate attacker unbinds a lock from a victim account, binds the lock to the attacker's account, unlocks the lock, and retrieves the user account information associated with the lock. In many instances, the unsalted MD5 hash could be cracked. Otherwise, the attacker could attempt to brute force the account with the email address that was found. Like in the remote scenario, the attacker would also be poised to send a convincing phishing/malspam email to the user to inflict further damage.

# Usage
```python3 attack_scenario_remote.py <victim_userID> <attacker_email_address>```

`<victim_userID>` = the userID of the victim account
`<attacker_email_address>` = the email address of the attacker account to which the lock will be bound (account will also be used to generate an accepted token for the HTTP headers)

# Demos
