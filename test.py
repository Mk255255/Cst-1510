import bcrypt


def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode("utf-8")

    salt = bcrypt.gensalt()
    bcrypted_password = bcrypt.hashpw(password_bytes, salt )
    return(bcrypted_password.decode('utf-8'))



def check_password(plain_text_password, hash_password_):
    password_bytes = plain_text_password.encode("utf-8")
    hash_password_bytes = hash_password_.encode("utf-8")
    if bcrypt.checkpw(password_bytes, hash_password_bytes):
        print('Password is correct')
    else:
        print("password is incorrect")




import bcrypt
import os
def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode("utf-8")

    salt = bcrypt.gensalt()
    bcrypted_password = bcrypt.hashpw(password_bytes, salt )
    return(bcrypted_password.decode('utf-8'))



def verify_password(plain_text_password, hash_password_):
    password_bytes = plain_text_password.encode("utf-8")
    hash_password_bytes = hash_password_.encode("utf-8")
    if bcrypt.checkpw(password_bytes, hash_password_bytes):
        print('Password is correct')
    else:
        print("password is incorrect")


print(hash_password('Magic123'))
test_password='SecurePassword123'
hashed=hash_password(test_password)
print(f"Original password: {test_password}")
print(f"Hashed password: {hashed}")
print(f"Hash length: {len(hashed)} characters")
is_valid=verify_password(test_password,hashed)
print(f"\n verification with correct password:{is_valid}")
is_invalid= verify_password("WrongPassword", hashed)
print(f"Verification with incorrect password: {is_invalid}")
USER_DATA_FILE = "users.txt"
username=input('Enter your username')
password=input('eEnter your Password')
epassword=hash_password(password)
with open(USER_DATA_FILE, 'a') as f:
   f.write(f'{username},{epassword}/n)')
def register_user():
    user_name=input('what is your name?')
    password=input('what is your password?')
    h_password=hash_password(password)
    with open ('users.txt','a')as f:
        f.write(f"{user_name},{h_password}\n")
        print('User registered successfully!')
def login_user():
    user_name=input('what is your name?')
    password=input('what is your password?')
    h_password=hash_password(password)
    with open ('users.txt','r')as f:
        users=f.readlines()
    for i in users:
        print(users)
        print("user not found!")


print(login_user())