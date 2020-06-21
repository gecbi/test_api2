from user import User

ussrs = [
    User(1,"bob","asdf")
]

username_mapping = {u.username: u for u in users}

userid_mapping = {1:{
        "id":1,
        "username": "bob",
        "password":"asdf"
}
     }

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    ussr_id = payload["ídentity"]
    return userid_mapping.get(user_id, None)
