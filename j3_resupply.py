from PyModules.mailsender import SendMail
from PyModules.configs import *
from BackupScripts.j3 import j3Backup
from string import Template
import mysql.connector
import os, sys

def resupplyValidation(recordSet,JID,AID,dataFormat):

	for record in recordSet:
		Actor = 'AU' if record[0] == 1 else 'Other actors'
		Status = 'inProgress' if record[1] == 0 else 'completed' if record[1] == 1 else 'No status'

		if Actor == 'Other actors':
			continue
		
		if Actor == 'AU' and Status == 'completed':
			print('\033[31m'+"{} stage is completed for {}_{}".format(Actor,JID,AID)+'\033[39m')
			FR_option = input('\033[93m'+"Do you need Force Resupply [Y/N] : "+'\033[39m')

			if FR_option.lower() == 'y':
				j3Backup(JID,AID)
				templateToMail(record,JID,AID,dataFormat)

			else:
				sys.exit()

		elif Actor == 'AU' and Status == 'inProgress':
			print('\033[32m'+"{} Resupply process for {}_{}".format(Actor,JID,AID)+'\033[39m')
			j3Backup(JID,AID)
			templateToMail(record,JID,AID,dataFormat)

def j3(JID,AID):

	connection=mysql.connector.connect(
		host = host['j3'],
		user = user['j3'],
		password = password['j3']
		) # Change credentials name mentioned in configs file
	
	dbCursor=connection.cursor()
	dbCursor.execute('''SELECT AAW.role_id,AAW.is_completed,A.ArticleKey,D.DatasetStatusID,D.DatasetID
		FROM pcv3.Journals J
		JOIN pcv3.Article A ON J.JournalKey=A.JournalKey
		JOIN pcv3_meta.DatasetStatus D ON A.DatasetStatusID=D.DatasetStatusID
		JOIN pcv3.article_actor_workflow AAW ON A.ArticleKey=AAW.article_key
		WHERE J.JID='{}' and A.AID={};'''.format(JID, AID))
	recordSet=dbCursor.fetchall()
	recordCount=dbCursor.rowcount

	dataFormat = 'j3'

	if recordCount==0:

		connection.close()
		connection=mysql.connector.connect(
			host = host['j3_2'],
			user = user['j3'],
			password = password['j3']
			) # Change credentials name mentioned in configs file
		dbCursor=connection.cursor()
		dbCursor.execute('''SELECT AAW.role_id,AAW.is_completed,A.ArticleKey,D.DatasetStatusID,D.DatasetID
			FROM pcv3.Journals J
			JOIN pcv3.Article A ON J.JournalKey=A.JournalKey
			JOIN pcv3_meta.DatasetStatus D ON A.DatasetStatusID=D.DatasetStatusID
			JOIN pcv3.article_actor_workflow AAW ON A.ArticleKey=AAW.article_key
			WHERE J.JID='{}' and A.AID={};'''.format(JID, AID))
		recordSet=dbCursor.fetchall()
		recordCount=dbCursor.rowcount

		dataFormat = 'j3_2'

		if recordCount==0:
			connection.close()
			print('\033[31m'+"No Records Found for {}_{}".format(JID,AID)+'\033[39m')
		else:
			resupplyValidation(recordSet,JID,AID,dataFormat)
			connection.close()
			
	else:
		resupplyValidation(recordSet,JID,AID,dataFormat)
		connection.close()
				
def templateToMail(record,JID,AID,dataFormat):
	
	querydata = {
	'article_key':record[2],
	'datasetstatusid':record[3],
	'datasetid':record[4],
	'jid':JID,
	'aid':AID
	}

	templateFilePath = os.path.realpath(os.path.join(os.path.dirname(__file__),"Templates/{}".format(template['j3']))) # Change template filename mentioned in configs file
	with open(templateFilePath) as templateFile:
		SQL_DUMP = Template(templateFile.read()).substitute(querydata)
	#print(SQL_DUMP+'\n\n')
	htmldata = data[dataFormat] # Change data name for mail mentioned in configs file
	htmldata.update(SQL_DUMP=SQL_DUMP)
		
	htmlFilePath = os.path.realpath(os.path.join(os.path.dirname(__file__),"Templates/mail.tpl"))
	with open(htmlFilePath) as htmlFile:
		HTML_FORMAT = Template(htmlFile.read()).substitute(htmldata)

	SendMail(HTML_FORMAT,JID,AID)