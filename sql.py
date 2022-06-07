import psycopg2
from psycopg2.extras import RealDictCursor, execute_values

def add(user_id):
    with psycopg2.connect(dbname="bot", user="postgres", password="yfpfh2003") as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            execute_values(curs, f"INSERT INTO bot (user_id,updates) VALUES %s",
                           [(user_id,0)])
def sign(user_id,user_login,user_password,user_name):
    with psycopg2.connect(dbname="bot", user="postgres", password="yfpfh2003") as conn:
        with conn.cursor(cursor_factory= RealDictCursor) as curs:
            execute_values(curs, f"INSERT INTO bot (user_id,user_login,user_password,user_name,updates) VALUES %s",
                           [(user_id, f"{user_login}", f"{user_password}", f"{user_name}",0)])
def check(user_id):
    try:
        with psycopg2.connect(dbname="bot", user="postgres", password="yfpfh2003") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as curs:
                curs.execute("SELECT * FROM bot")

                record = curs.fetchall()
                for i in record:
                    us_id=str(user_id)
                    if i["user_id"] == us_id:
                        if i["user_login"]==None and i["user_name"]==None:
                            curs.execute(f"""
                                                               DELETE FROM bot
                                                               WHERE user_id='{user_id}'
                                                            """)
                            return True
                        else:
                            return None

    except:
        return None


def check_unsign(user_id):
        with psycopg2.connect(dbname="bot", user="postgres", password="yfpfh2003") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as curs:
                curs.execute("SELECT * FROM bot")
                record = curs.fetchall()
                a=[]
                a_i=str(user_id)
                for i in record:
                    a.append(i["user_id"])
                if a_i in a:
                    return None
                else:
                    return True
                print(a)

def give(user_id):
    with psycopg2.connect(dbname="bot", user="postgres", password="yfpfh2003") as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute("SELECT * FROM bot")
            item={}
            record = curs.fetchall()
            for i in record:
                if i["user_id"]==f"{user_id}":
                    item={"user_name":i["user_name"],
                          "user_login":i["user_login"]}
            return item
def delete(user_name,user_password):
    with psycopg2.connect(dbname="bot", user="postgres", password="yfpfh2003") as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute("SELECT * FROM bot")
            record = curs.fetchall()
            for i in record:
                if i["user_name"] == f"{user_name}" and i["user_password"] == f"{user_password}":
                    curs.execute(f"""
                                    DELETE FROM bot
                                    WHERE user_name='{user_name}'
                                 """)
def update(user_id):
    try:
        with psycopg2.connect(dbname="bot", user="postgres", password="yfpfh2003") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as curs:
                curs.execute("SELECT * FROM bot")
                record = curs.fetchall()
                a = []
                u_i = str(user_id)
                for i in record:
                    if i["user_id"]==u_i:
                        if i["user_name"]:
                            pass
                        else:
                            if int(i["updates"]) >= 7:
                                raise Exception
                            else:
                                value = int(i["updates"]) + 1
                                curs.execute(f"""
                                                            UPDATE bot
                                                            SET updates = %s
                                                            WHERE user_id = '{user_id}'
                                                                """, (value,))
                return True

    except:
        return None

 # if i["user_id"]==f"{user_id}":
