# attack_scenario_remote.py
In this scenario, a remote attacker could acquire sensitive user info from arbitrary users, unbind their locks, and bind them to the attacker's account. Such a scenario would provide ample opportunity for successful large-scale phishing/malspam attacks against OKLOK users because the attacker would be in possession of user account information that he/she could utilize to make the email seem more legitimate.

# attack_scenario_proximate.py
In this scenario, a physically approximate attacker could unbind a lock from a victim account, bind the lock to the attacker's account, unlock the lock, and retrieve the user account information associated with the lock. In many instances, the unsalted MD5 hash could be cracked. Otherwise, the attacker could attempt to brute force the account with the email address that was found. Like in the remote scenario, the attacker would be poised to send a convincing phishing/malspam email to the user to inflict further damage.

# Usage

# Demos
