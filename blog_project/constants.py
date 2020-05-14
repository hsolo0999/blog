import os

class Const:
    SECRET_KEY = 'v^a^xoxveyk^q@u#39-wz$i#b=)-kgn2_@+qwa0zs$jst9)9z='
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #on/off debug mode
    DEBUG = True
    

    #add data here to connect your database in prodaction
    DBNAME = None
    DBUSER = None
    DBPASSWORD = None
    DBHOST = None
    DBPORT = None


    DATABASES_DEBUG = {
	'default': {
			    'ENGINE': 'django.db.backends.sqlite3',
			    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
				}
    }

    DATABASES_PROD = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': DBNAME,
                'USER' : DBUSER,
                'PASSWORD' : DBPASSWORD,
                'HOST' : DBHOST,
                'PORT' : DBPORT,
                }
    }
