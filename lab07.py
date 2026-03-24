
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

'''
print(hash_password('muak2079'))


verify_password('muak2079','$2b$12$Q0BikGf0pHn/m93TKMXRh.47KZAvUwQ4o4ozPGtIqLwX1SIAvmqWa')


# TEMPORARY TEST CODE - Remove after testing
test_password = "SecurePassword123"
# Test hashing
hashed = hash_password(test_password)
print(f"Original password: {test_password}")
print(f"Hashed password: {hashed}")
print(f"Hash length: {len(hashed)} characters")

# Test verification with correct password
is_valid = verify_password(test_password, hashed)
print(f"\nVerification with correct password: {is_valid}")

# Test verification with incorrect password
is_invalid = verify_password("WrongPassword", hashed)
print(f"Verification with incorrect password: {is_invalid}")
'''
USER_DATA_FILE = "users.txt"

username = input('Enter username:')
password = input('Enter password:')
epassword = hash_password(password)

with open(USER_DATA_FILE, 'a') as f:
    f.write(f"{username},{epassword}\n")

def register_user(username, password):
username = input('Enter username:')
if username in USER_DATA_FILE:
    print('Already registered')
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





