mailUser = "kavitha.anbukkarasu@tnqtech.com"
mailPassword = "ylawzjnzwadxodlj"

host = {
	"j2" : "pagecentral.c6sacrsspylv.us-east-1.rds.amazonaws.com",
	"j3n" : "pc-env1-live.cjuffjljaxvb.us-east-1.rds.amazonaws.com",
	"j3" : "pc-env1-elsevierjournals-live.cjuffjljaxvb.us-east-1.rds.amazonaws.com",
	"j3_2" : "pc-env1-elsevierjournals-live.cjuffjljaxvb.us-east-1.rds.amazonaws.com",
	"rec" : "pcv3-aip-live.c6sacrsspylv.us-east-1.rds.amazonaws.com",
	"rsc2" : "pc-rsc-elife.c6sacrsspylv.us-east-1.rds.amazonaws.com",
	"rsc3" : "pcv3-rsc-live.c6sacrsspylv.us-east-1.rds.amazonaws.com",
	"sjs" : "pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com",
	"book" : "pc-elsevierbooks.c6sacrsspylv.us-east-1.rds.amazonaws.com",
	"kar_kia_deg" : "pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com",
	"book3" : "pcv3-elsbook-live.c6sacrsspylv.us-east-1.rds.amazonaws.com"
	}

user = {
	"j2" : "support",
	"j3n": "supportuser",
	"j3" : "supportuser",
	"rec" : "suppotuser",
	"rsc2" : "rscsupportuser",
	"rsc3" : "supportuser",
	"sjs" : "rup_support",
	"book" : "supportuser",
	"kar_kia_deg" : "supportuser",
	"book3" : "support_user"
	}

password = {
	"j2" : "27PNO300Mb",
	"j3" : "mk9ZxpZcqyDV",
	"j3n" : "mk9ZxpZcqyDV",
	"rec" : "tQJ54QV6K5XY",
	"rsc2" : "pXe7CC65hN",
	"rsc3" : "tMF4ee4rhWS7R8zX",
	"sjs" : "5vPsWeQQyp3UUgVs",
	"book" : "45D466wK9T",
	"kar_kia_deg" : "3efenBJvFt89",
	"book3" : "aYJe2N9SRSFnUUJm"
	}



template = {
	'j3':'j3Query.tpl',
	'j3n':'j3nQuery.tpl',
	'rsc3':'rsc3Query.tpl',
	'sjs':'sjsQuery.tpl',
	'rec':'recQuery.tpl',
	'aip':'aipQuery.tpl',
	'deg':'degQuery.tpl',
	'kia':'kiaQuery.tpl',
	'kar':'karQuery.tpl',
	'b3':'b3Query.tpl'
	}

data = {
	'j3':{
		'toName':'Lawrence',
		'customerVersion':'ELSEVIER JOURNALS PCv3.1 RDS-1',
		'dbHost':'pcv3-elsevier-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3, pcv3_meta'
		},
	'j3n':{
	    'toName':'Lawrence',
	    'customerVersion':'ELSEVIER JOURNALS PCv3.1 RDS-4',
	    'dbHost':'pc-env1-live.cjuffjljaxvb.us-east-1.rds.amazonaws.com',
	    'dbTable':'pcv3, pcv3_meta'
    },
    'j3_2':{
	    'toName':'Lawrence',
	    'customerVersion':'ELSEVIER JOURNALS PCv3.1 RDS-4',
	    'dbHost':'  pc-env1-elsevierjournals-live.cjuffjljaxvb.us-east-1.rds.amazonaws.com',
	    'dbTable':'pcv3, pcv3_meta'
    },
	'sjs':{
		'toName':'Meena',
		'customerVersion':'RUP PCv3.0',
		'dbHost':'pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_rup '
		},
	'rsc3':{
		'toName':'Lawrence',
		'customerVersion':'RSC PCv3.0',
		'dbHost':'pcv3-rsc-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_rsc, pcv3_rsc_meta'
		},
	'rec':{
		'toName':'Lawrence',
		'customerVersion':'REC PCv3.0',
		'dbHost':'pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_rec, pcv3_karger_meta'
		},
	'aip':{
		'toName':'Meena',
		'customerVersion':'AIP PCv3.0',
		'dbHost':'pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_aip, pcv3_karger_meta'
		},
	'deg':{
		'toName':'Lawrence',
		'customerVersion':'DEGRUYTER PCv3.1',
		'dbHost':'pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_degruter, pcv3_karger_meta'
		},
	'kia':{
		'toName':'Lawrence',
		'customerVersion':'KIADO PCv3.1',
		'dbHost':'pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_kiado, pcv3_karger_meta'
		},
	'kar':{
		'toName':'Lawrence',
		'customerVersion':'KARGER PCv3.1',
		'dbHost':'pcv3-karger-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_karger, pcv3_karger_meta'
		},
	'b3':{
		'toName':'Lawrence',
		'customerVersion':'BOOK PCv3.1',
		'dbHost':'pcv3-elsbook-live.c6sacrsspylv.us-east-1.rds.amazonaws.com',
		'dbTable':'pcv3_elsevier_books, pcv3_elsevier_books_meta'
		}
	}
