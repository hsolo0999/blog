class Const:
    SECRET_KEY = 'v^a^xoxveyk^q@u#39-wz$i#b=)-kgn2_@+qwa0zs$jst9)9z='
    
    DBNAME = None
    DBUSER = None
    DBPASSWORD = None
    DBHOST = None
    DBPORT = None


    DATABASES_DEBUG = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'blog_db',
                'USER' : 'blog_user',
                'PASSWORD' : 'qwerty',
                'HOST' : '127.0.0.1',
                'PORT' : '5432',
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
