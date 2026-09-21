import random
import string

def generate_password(length=12):
    # Characters, numbers aur symbols ka combination
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    length = int(input("Password ki length kitni chahiye? (jaise 12 ya 16): "))
    print(f"Aapka naya password: {generate_password(length)}")
