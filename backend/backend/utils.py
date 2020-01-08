from voluptuous import Schema,error
from rethinkdb import r
import os

user_schema = Schema({'user':str,'password':str})
users_table = os.getenv("USERS_TABLE","users")

def get_rethink():
    return r.connect(
        host=os.getenv("RETHINK_HOST","127.0.0.1"),
        port=os.getenv("RETHINK_PORT",28015),
        db=os.getenv("RETHINK_DB",'test')
    )

def validate_user_post(post_user):
    try:
        user_schema(post_user)
    except error.MultipleInvalid:
        return False
    except error.Invalid:
        return False
    return True

def save_user(user):
    con = get_rethink()
    r.table(users_table).insert(user).run(con)
    con.close()