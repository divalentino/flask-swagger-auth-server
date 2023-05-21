import sqlite3

class User(object):                                      
    def __init__(self, id, username, password):          
        self.id = id                                     
        self.username = username                         
        self.password = password                         
    def __str__(self):                                   
        return "User(id='%s')" % self.id                 
                   
# User lookup needs to be better in prod, e.g., authenticate and identity
# functions implement lookups done using Postgres DB, hashed passwords
def authenticate(username, password):
    with sqlite3.connect("users.db") as con:      
        cur = con.cursor()
        pws = list(cur.execute("SELECT * FROM users where username='%s'"%(username)))
        cur.close()
        if len(pws)!=1:
            return None
        if pws[0][2].encode('utf-8') == password.encode('utf-8'):
            return User(pws[0][0],pws[0][1],pws[0][2])

def identity(payload):
    with sqlite3.connect("users.db") as con:                 
        user_id = payload['identity']
        cur = con.cursor()
        pws = list(cur.execute("SELECT * FROM users where id='%s'"%(user_id)))
        cur.close()
        if len(pws)>0:
            return user_id
        return None
