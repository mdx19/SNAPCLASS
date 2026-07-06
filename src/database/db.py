from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    # Check for unique username. Returns True when the username is already
    # taken (i.e. a matching row exists), False when it's free to use.
    response = (
        supabase.table("teachers")
        .select("username")
        .eq("username", username)
        .execute()
    )
    return len(response.data) > 0


def create_teacher(username, password, name):
    data = {
        "username": username,
        "password": hash_pass(password),
        "name": name,
    }

    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = (
        supabase.table("teachers")
        .select("*")
        .eq("username", username)
        .execute()
    )

    if response.data:
        teacher = response.data[0]

        if check_pass(password, teacher["password"]):
            return teacher

    return None