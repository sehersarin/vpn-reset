# vpn-reset

Description:

The purpose of this code is to auto-reset the US VPN. It is a python script using selenium and is implemented through the use of a Cron Job.

Steps to run: 

1. Set up Cron Job to run vpn_reset.py at a specified interval
2. Set Login & password through the use of environment variables <VPN_USERNAME> & <VPN_PASSWORD>. The environment variables must be set in the System environment as well as the cron tab itself.

Notes:

- Any time there is an error in the code, an email will be sent to the listed email address, showing you the error (usually in SPAM folder)
- In order for Cron Job to run, the computer mustn't be sleeping (Apple > System Preferences > Energy Saver > Schedule > set a wake time for the computer)
- Once the computer is woken up, use 'Amphetamine' to set a trigger and keep your computer awake for a set period of time (so you can run the cron job multiple times throughout the day)
