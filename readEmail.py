"""
This function allows you to read emails which are sent
from your personal email to the Pi email.

I wrote this function because i wanted to
send commands to my raspberry pi from anywhere in the world
through email.

i call this function from the main.
"""

import imaplib, email

def command():
	msrvr = imaplib.IMAP4_SSL('imap.gmail.com')

	un = 'example@gmail.com'
	pwd = 'password goes here'
	msrvr.login(un,pwd)
	
	stat,cnt = msrvr.select('inbox')

	stat, dta = msrvr.fetch \
		(cnt[0], \
		'(UID BODY[TEXT])')
	raw_email = dta[0][1]
        
	email = raw_email.decode('utf-8')
	cmd = email[75:77]
	cmd2 = email[0:2]
	#print(raw_email)
	#print()
	#print(cmd)
	#print(cmd2)
	if cmd == 'tp' or cmd2 == 'tp':
		msrvr.store('2', '+FLAGS', '\\Deleted')
		msrvr.expunge()
	
	msrvr.close()
	msrvr.logout()
	return cmd,cmd2
