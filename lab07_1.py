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
        return True
    else:
        return False



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
    
        for user in users:
            store_user_name, store_user_hash = user.strip().split(',')
            if user_name == store_user_name and verify_password(password, store_user_hash):
                return True
            else:
                return False
                print('Envalid user')


while True:
    print('Welcome')
    print('1. Register')
    print('2. Log in')
    print('3. Exit')
    choice = input('Choose from (1-3): ')

    if choice == '1':
        register_user()
    elif choice == '2':
        print(login_user())
    elif choice =='3':
        print('Goodbye!')
        break
    else:
        print('Invalid input !!!!!')

