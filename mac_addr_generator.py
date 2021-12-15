import random
import string
def generator():
    part = ""
    for x in range(5):
        part = part + str(random.randint(0,9)) + str(random.randint(0,9)) + ":"
    part = part + str(random.randint(0,9)) + str(random.randint(0,9))
    print(part)

generator()