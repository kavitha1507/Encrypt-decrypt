from PyModules.mailsender import SendMail
from PyModules.configs import *
from BackupScripts.rsc2 import rsc2Backup
from string import Template
import mysql.connector
from sys import *
import os

def rsc2(JID,AID):
	connection=mysql.connector.connect(
		host = host['rsc2'],
		user = user['rsc2'],
		password = password['rsc2']
		)
	
	dbCursor=connection.cursor()
	dbCursor.execute('''SELECT S.name,S.status,A.ArticleKey,D.DatasetStatusID,D.DatasetID
		FROM pc_rscv2.users U
		JOIN pc_rscv2.Article A ON U.optarticleid=A.ArticleKey
		JOIN pc_rscv2.DatasetStatus D ON A.DatasetStatusID=D.DatasetStatusID
		JOIN pc_rscv2.chain_workflow W ON U.optarticleid=W.article_key 
		JOIN pc_rscv2_chain.workflow CW ON W.uuid=CW.uuid 
		JOIN pc_rscv2_chain.stage S ON S.workflow_id=CW.id
		WHERE U.jid='{}' AND U.aid='{}';'''.format(JID, AID))
	recordSet=dbCursor.fetchall()
	recordCount=dbCursor.rowcount
	
	if recordCount==0:
		connection.close()
		print('\033[31m'+"No Records Found for {}_{}".format(JID,AID)+'\033[39m')
	
	else:
		for record in recordSet:
			Actor = 'AU' if record[0] == 'AU' else 'Other actors'
			Status = 'inProgress' if record[1] == 'inProgress' else 'completed' if record[1] == 'completed' else 'No status'
			
			if Actor == 'Other actors':
				continue
			
			if Actor == 'AU' and Status == 'completed':
				print('\033[31m'+"{} stage is completed for {}_{}".format(Actor,JID,AID)+'\033[39m')
				FR_option = input('\033[93m'+"Do you need Force Resupply [Y/N] : "+'\033[39m')

				if FR_option.lower() == 'y':
					rsc2Backup(JID,AID)
					templateToMail(record,JID,AID)
					
				else:
					sys.exit()
						
			elif Actor == 'AU' and Status == 'inProgress':
				print('\033[32m'+"{} Resupply process for {}_{}".format(Actor,JID,AID)+'\033[39m')
				
				rsc2Backup(JID,AID)
				templateToMail(record,JID,AID)
				
		connection.close()

def templateToMail(record,JID,AID):
	
	querydata = {
	'article_key':record[2],
	'datasetstatusid':record[3],
	'datasetid':record[4]
	}
	templateFilePath = os.path.realpath(os.path.join(os.path.dirname(__file__),"Templates/rsc2Query.tpl"))

	with open(templateFilePath) as templateFile:
		SQL_DUMP = Template(templateFile.read()).substitute(querydata)

	htmldata = {
	'toName':'Shradda',
	'customerVersion':'RSCv2.0',
	'dbHost':'pc-rsc-elife.c6sacrsspylv.us-east-1.rds.amazonaws.com',
	'dbTable':'pc_rscv2',
	'SQL_DUMP':SQL_DUMP
	}
	htmlFilePath = os.path.realpath(os.path.join(os.path.dirname(__file__),"Templates/mail.tpl"))

	with open(htmlFilePath) as htmlFile:
		HTML_FORMAT = Template(htmlFile.read()).substitute(htmldata)

	SendMail(HTML_FORMAT,JID,AID)