from PyModules.configs import *
import mysql.connector
import os
def pcv2():
	con=mysql.connector.connect(
		host = host['j2'],
		user = user['j2'],
		password = password['j2']
		)
	
	cur=con.cursor()
	cur.execute('''SELECT A.ArticleKey,S.name,S.status,S.updated_at 
	FROM pc.Article A JOIN pc.users U ON  U.optarticleid=A.ArticleKey 
	JOIN pc.chain_workflow W ON A.ArticleKey=W.article_key 
	JOIN pcchain.workflow CW ON W.uuid=CW.uuid 
	JOIN pcchain.stage S ON S.workflow_id=CW.id 
	WHERE U.jid='{}' and U.aid='{}';'''.format(jid,aid))
	res=cur.fetchall()
	row=cur.rowcount
	
	if row==0:
		no_rec_j2.append(jid+'_'+aid)
	
	else:
		for i in res:
			if i[1]=='AU' and i[2]=='completed':
				print("\nAU is completed for {}_{}".format(jid,aid))
				
				# Force Resupply
				FR = input("Do you want force resupply [y/n] :")
				
				if FR.lower()=='y':
					os.system("node ~/Proofcentral/Scripts/resupply/forcejournal.js {} {}".format(i[0],ticket_id))
					sent_j2.append('forceresupply'+'_'+jid+'_'+aid)

				elif FR.lower()=='n':
					au_comp_j2.append(jid+'_'+aid)

			elif i[1]=='AU' and i[2]=='inProgress':

				# Resupply
				os.system("node ~/Proofcentral/Scripts/resupply/journal.js {} {}".format(i[0],ticket_id))
				sent_j2.append(jid+'_'+aid)

def pcv3():
	conn=mysql.connector.connect(
		host = host['j3'],
		user = user['j3'],
		password = password['j3']
		)
	
	cur=conn.cursor()
	cur.execute('''SELECT A.ArticleKey,S.name,S.status,S.updated_at
	FROM pcv3.Article A
	JOIN pcv3.users U ON  U.optarticleid=A.ArticleKey
	JOIN pcv3.chain_workflow W ON A.ArticleKey=W.article_key 
	JOIN pcv3_chain.workflow CW ON W.uuid=CW.uuid 
	JOIN pcv3_chain.stage S ON S.workflow_id=CW.id 
	WHERE U.JID='{}' and U.AID={};'''.format(jid,aid))
	res=cur.fetchall()
	row=cur.rowcount
	
	if row==0:
		no_records_j3.append(jid+'_'+aid)
	
	else:
		for i in res:
			if i[1]=='AU' and i[2]=='completed':
				au_comp_j3.append(jid+'_'+aid)
			
			elif i[1]=='AU' and i[2]=='inProgress':
				os.system("python3 ~/Desktop/PyScripts/Resupply/journals_3.1_resupply.py {} {} '{}'".format(jid,aid,MAIL_SUB))
				sent_j3.append(jid+'_'+aid)

def book():
	conn=mysql.connector.connect(
		host = host['book'],
		user = user['book'],
		password = password['book']
		)
	
	cur=conn.cursor()
	cur.execute('''SELECT A.ArticleKey,S.name,S.status,S.updated_at 
	FROM pcv2_book.Article A
	JOIN pcv2_book.users U ON  U.optarticleid = A.ArticleKey
	JOIN pcv2_book.chain_workflow W ON A.ArticleKey = W.article_key 
	JOIN pcv2_book_chain.workflow CW ON W.uuid = CW.uuid 
	JOIN pcv2_book_chain.stage S ON S.workflow_id = CW.id 
	WHERE U.jid='{}' and U.aid='{}';'''.format(jid,aid))
	res1=cur.fetchall()
	row=cur.rowcount
	
	if row==0:
		no_rec_book.append(aid)
	
	else:
		for i in res1:
			if i[1]=='AU' and i[2]=='completed':
				print("\nAU is completed for {}_{}".format(jid,aid))
								
				# Force Resupply
				FR=input("do you want force resupply [y/n] :")
				
				if FR.lower()=='y':
						os.system("node /home/poomukilan/Proofcentral/Scripts/resupply/forcebook.js {} {}".format(i[0],ticket_id))
						sent_book.append("forceresupply"+'-'+str(aid))

				elif FR.lower()=='n':
					au_comp_book.append(aid)

			elif i[1]=='AU' and i[2]=='inProgress':
				
				# Resupply
				os.system("node ~/Proofcentral/Scripts/resupply/book.js {} {}".format(i[0],ticket_id))
				sent_book.append(aid)


jid_aid=eval(input("enter JID AID: "))


sent_j2=[]
no_rec_j2=[]
au_comp_j2=[]

sent_j3=[]
no_records_j3=[]
non_sent_j3=[]
au_comp_j3=[]

sent_book=[]
no_rec_book=[]
au_comp_book=[]


print("Count of jid_aid:- ",len(jid_aid))

a = input('''Enter 
	1-> journal 3.0
	2-> journal 3.1
	3-> book:-
	 ''')

if a == '2':
	MAIL_SUB = input("Enter the mail subject : ")
else:
	ticket_id = input("enter the ticket_id : ")

for i in jid_aid:
	jid=i.split()[0]
	aid=i.split()[1]
	if a=='1':
		pcv2()
	elif a=='2':
		pcv3()
	elif a=='3':
		book()
	else:
		print("Enter a valid input")

# 3.0 Article Status
if len(sent_j2)>0:
	print("send items in j2:- ",set(sent_j2),"--->count - ",len(sent_j2))
if len(no_rec_j2)>0:
	print("no records in j2:- ",set(no_rec_j2),"--->count - ",len(no_rec_j2))
if len(au_comp_j2)>0:
	print("AU is completed j2:- ",set(au_comp_j2),"--->count - ",len(au_comp_j2))


# 3.1 Article Status
if len(sent_j3)>0:
	print("Resupply sent for ",sent_j3,"--->count - ",len(sent_j3))
if len(no_records_j3)>0:
	print("no records in j3:- ",no_records_j3,"--->count - ",len(no_records_j3))
if len(non_sent_j3)>0:
	print("non sent in j3:- ",non_sent_j3,"--->count - ",len(non_sent_j3))
if len(au_comp_j3)>0:
	print("AU is completed j3:- ",au_comp_j3,"--->count - ",len(au_comp_j3))

# Book Status
if len(sent_book)>0:
	print("sent items for book:- ",sent_book,"--->count - ",len(sent_book))
if len(no_rec_book)>0:
	print("no records in book:- ",no_rec_book,"--->count - ",len(no_rec_book))
if len(au_comp_book)>0:
	print("AU is completed for book:- ",au_comp_book,"--->count - ",len(au_comp_book))