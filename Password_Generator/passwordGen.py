import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = input("Enter password length:")

password = "".join(random.sample(total, length))

print(password)
