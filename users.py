import mysql.connector as cor
import config

# create creates a user in our database.
# It takes username and password as arguments
# It gives us no output
def create(name, password, cfg):
    sql = cor.connect(host=cfg["host"], user=cfg["user"], password=cfg["passwd"], database="code_metrics")
    x = sql.cursor()
    x.execute("insert into users(name, password) values ('" + name +"','" + password + "')")
    sql.commit()

def delete(name, cfg):
    sql = cor.connect(host=cfg["host"], user=cfg["user"], password=cfg["passwd"], database="code_metrics")
    u = sql.cursor()
    u.execute("delete from users where name='"+name+"'")
    sql.commit()

# authorize checks whether the given username and password combination exists in the database.
# In other words, it tells us whether or not the user is registered/created
# It gives us a boolean output
# True if the user exists, False if not.
def authorize(name, password, cfg):
    sql = cor.connect(host=cfg["host"], user=cfg["user"], password=cfg["passwd"], database="code_metrics")
    x = sql.cursor()
    x.execute(
            'select count(name) from users where name="' + \
            name + \
            '" and password="'+ \
            password + \
            '"'
    )
    return bool(x.fetchone()[0])

def list(cfg):
    sql = cor.connect(host=cfg["host"], user=cfg["user"], password=cfg["passwd"], database="code_metrics")
    x = sql.cursor()
    x.execute('SELECT name FROM users')
    tuples = x.fetchall()
    l = []
    for t in tuples:
        l.append(t[0])
    return l

### For testing only ###
if __name__ == "__main__":
    cfg = config.read_from_user()
    create("Archie", "Anime", cfg)
    print(authorize("Archie", "Anime", cfg))
    delete("Archie", cfg)
    print(authorize("Archie", "Anime", cfg))
