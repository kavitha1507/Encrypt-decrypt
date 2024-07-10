from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from .configs import *
import sys

def SendMail(html,jid,aid,toId='kavitha.anbukkarasu@tnqtech.com'):
		
	MAIL_SUB = input("Enter Mail Subject : ")

	print("Mail process..........")

	FROM_ID = mailUser
	PASSWORD = mailPassword

	TO_ID = '''kavitha.anbukkarasu@tnqtech.com,{}'''.format(toId)
	
	message = MIMEMultipart("alternative")
	if bool(MAIL_SUB) == True:
		message["Subject"] = MAIL_SUB
	else:
		message["Subject"] = "Resupply request for {}_{}".format(jid,aid)
	message["From"] = FROM_ID
	message["To"] = toId
	#poomukilan.velusamy@tnqtech.com,
	#sarathkumar.dhayalan@tnqtech.com,
	#praveen.senthil@tnqtech.com,
	#suresh.subramaniyan@tnqtech.com,
	#gayathri.selvaraj@tnqtech.com,
	#vinith.babu@tnqtech.com,
	#message["Cc"] = '''kavitha.anbukkarasu@tnqtech.com'''
	
	FORMAT = MIMEText(html, "html")
	message.attach(FORMAT)

	# Create a secure SSL context
	context = ssl.create_default_context()

	try:
		server = smtplib.SMTP("smtp.gmail.com",587)
		server.starttls(context=context) # Secure the connection
		server.login(FROM_ID, PASSWORD)
		server.sendmail(FROM_ID, TO_ID.split(','), message.as_string())
		print('\033[32m'+"Mail sent..........!"+'\033[39m')
	
	except Exception as e:
		# Print any error messages to stdout
		print('\033[31m'+'mail error : '+'\033[39m',e)
	
	finally:
		server.quit() 