class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Access granted")

try:
    user_age = int(input("Enter age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"Access denied: {e}")