from random import  choices
import string

def crate_password():
    USER_KEY = int(input('enter your lengh : '))
    pool = string.digits + string.ascii_letters + string.punctuation
    password  = choices(pool, k=USER_KEY)
    return ''.join(password)


if __name__ == "__main__":
    print(crate_password())