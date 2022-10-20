import mysql.connector as cor

# createuser creates a user in our database.
# It takes username and password as arguments
# It gives us no output
def createuser(name,password):
    sql = cor.connect(host="localhost", user="root", password="tablecloth", database="code_metrics")
    x = sql.cursor()
    x.execute("insert into users(name, password) values ('" + name +"','" + password + "')")
    sql.commit()

def deleteuser(name):
    sql = cor.connect(host="localhost", user="root", password="tablecloth", database="code_metrics")
    u = sql.cursor()
    u.execute("delete from users where name='"+name+"'")
    sql.commit()

# authorize checks whether the given username and password combination exists in the database.
# In other words, it tells us whether or not the user is registered/created
# It gives us a boolean output
# True if the user exists, False if not.
def authorization(name,password):
    sql = cor.connect(host="localhost", user="root", password="tablecloth", database="code_metrics")
    x = sql.cursor()
    x.execute(
            'select count(name) from users where name="' + \
            name + \
            '" and password="'+ \
            password + \
            '"'
    )
    return bool(x.fetchone()[0])

### For testing only ###
if __name__ == "__main__":
    createuser(name="Archie",password="Anime")
    print(authorization(name="Archie",password="Anime"))
    deleteuser(name="Archie")
    print(authorization(name="Archie",password="Anime"))
