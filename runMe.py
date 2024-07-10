from j3_resupply import j3
from sjs_resupply import sjs
from rsc2_resupply import rsc2
from rsc3_resupply import rsc3
from rec_resupply import rec
from aip_resupply import aip
from deg_resupply import deg
from kia_resupply import kia
from kar_resupply import kar
from book3_resupply import book3
from j3n_resupply import j3n
import sys

OPTION = input('''Choose a option
	1 -> Journal 3.1
	2 -> SJS
	3 -> RSC 2.0
	4 -> RSC 3.0
	5 -> REC
	6 -> AIP
	7 -> DEGRUYTER
	8 -> KIADO
	9 -> KARGER
	10 -> BOOK 3.1
	11 -> Journal New
''')

inputOption = input('''Enter the option
	1 -> Single Input
	2 -> Multi Input
''')

if inputOption == '1':
	Jid = input("Enter JID : ")
	Aid = input("Enter AID : ")
	
	if OPTION == '1':
		j3(Jid,Aid)
	elif OPTION == '2':
		sjs(Jid,Aid)
	elif OPTION == '3':
		rsc2(Jid,Aid)
	elif OPTION == '4':
		rsc3(Jid,Aid)
	elif OPTION == '5':
		rec(Jid,Aid)
	elif OPTION == '6':
		aip(Jid,Aid)
	elif OPTION == '7':
		deg(Jid,Aid)
	elif OPTION == '8':
		kia(Jid,Aid)
	elif OPTION == '9':
		kar(Jid,Aid)
	elif OPTION == '10':
		book3(Jid,Aid)
	elif OPTION == '11':
		j3n(Jid,Aid)


elif inputOption == '2':
	Inputs = eval(input("Enter input format 'jid aid','jid aid'..."))

	for Input in Inputs:
		Jid = Input.split()[0]
		Aid = Input.split()[1]
		
		if OPTION == '1':
			j3(Jid,Aid)
		elif OPTION == '2':
			sjs(Jid,Aid)
		elif OPTION == '3':
			rsc2(Jid,Aid)
		elif OPTION == '4':
			rsc3(Jid,Aid)
		elif OPTION == '5':
			rec(Jid,Aid)
		elif OPTION == '6':
			aip(Jid,Aid)
		elif OPTION == '7':
			deg(Jid,Aid)
		elif OPTION == '8':
			kia(Jid,Aid)
		elif OPTION == '9':
			kar(Jid,Aid)
		elif OPTION == '10':
			book3(Jid,Aid)
		elif OPTION == '11':
		    j3n(Jid,Aid)


else:
	print("Enter valid input")
	sys.exit()