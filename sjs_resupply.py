from PyModules.mailsender import SendMail
from PyModules.configs import *
from BackupScripts.sjs import sjsBackup
from string import Template
import mysql.connector
import os, sys

def sjs(JID,AID):
	connection=mysql.connector.connect(
		host = host['sjs'],
		user = user['sjs'],
		password = password['sjs']
		) # Change credentials name mentioned in configs file
	
	dbCursor = connection.cursor()
	dbCursor.execute('''SELECT AAW.role_id,AAW.is_completed,A.ArticleKey
		FROM pcv3_sjs.Journals J
		JOIN pcv3_sjs.Article A ON J.JournalKey=A.JournalKey
		JOIN pcv3_sjs.article_actor_workflow AAW ON A.ArticleKey=AAW.article_key
		WHERE J.JID='{}' and A.AID='{}';'''.format(JID, AID))
	recordSet = dbCursor.fetchall()
	recordCount = dbCursor.rowcount
	
	if recordCount == 0:
		connection.close()
		print('\033[31m'+"No Records Found for {}_{}".format(JID,AID)+'\033[39m')
	
	else:
		for record in recordSet:
			Actor = 'AU' if record[0] == 1 else 'Other actors' # change roleid
			Status = 'inProgress' if record[1] == 0 else 'completed' if record[1] == 1 else 'No status'
			Articlekey = record[2]

			if Actor == 'Other actors':
				continue

			if Actor == 'AU' and Status == 'completed':
				print('\033[31m'+"{} stage is completed for articleKey - {} in {}_{}".format(Actor,Articlekey,JID,AID)+'\033[39m')
				#sys.exit()
						
			elif Actor == 'AU' and Status == 'inProgress':
				print('\033[32m'+"{} Resupply process for articleKey - {} in {}_{}".format(Actor,Articlekey,JID,AID)+'\033[39m')
								
				sjsBackup(Articlekey)
				templateToMail(record,JID,AID)

		connection.close()

def templateToMail(record,JID,AID):
	
	querydata = {'article_key':record[2]}
	templateFilePath = os.path.realpath(os.path.join(os.path.dirname(__file__),"Templates/{}".format(template['sjs']))) # Change template filename mentioned in configs file
	
	with open(templateFilePath) as templateFile:
		SQL_DUMP = Template(templateFile.read()).substitute(querydata)
	
	htmldata = data['sjs'] # Change data name for mail mentioned in configs file
	htmldata.update(SQL_DUMP=SQL_DUMP)

	htmlFilePath = os.path.realpath(os.path.join(os.path.dirname(__file__),"Templates/mail.tpl"))
	with open(htmlFilePath) as htmlFile:
		HTML_FORMAT = Template(htmlFile.read()).substitute(htmldata)
		
	SendMail(HTML_FORMAT,JID,AID,toId='maragathameena.inbaraj@tnqsoftware.co.in')
