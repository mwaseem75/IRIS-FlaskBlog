from website import create_app
from website.myconfig import *

if __name__ == "__main__":
    # get db info from config file
    database_uri = 'iris://'+DB_USER + \
        ':'+DB_PASS+'@'+DB_URL+':'+DB_PORT+'/'+DB_NAMESPACE
    app = create_app(database_uri)
    app.run('0.0.0.0', port="4040", debug=False)
