import random
import string
def generator():
    while True:
        try:
            input_value = int(input("Choose a type of MAC Address:\n" +  "1) Default\n" + "2) Only Integer\n" + "3) Only Character\n"))
            if input_value > 0 and input_value < 4:
                break
            else: 
                print("Choose '1', '2', or '3'")
                continue
        except:
            print("Choose '1', '2', or '3'")
    if input_value == 1:
        #Placeholder code for default generation
        print(input)
    elif input_value == 2:
        part = ""
        for x in range(3):
            part = part + str(random.randint(0,9)) + str(random.randint(0,9)) + ":"
        part = part + str(random.randint(0,9)) + str(random.randint(0,9))
        print(part)
    else:
        part = ""
        for x in range(3):
            part = part + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + ":"
        part = part + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        print(part)

generator()