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
    
    # Default MAC address Generation
    if input_value == 1:
        address = ""
        int_or_char_list = [str(random.randint(0,9)), random.choice(string.ascii_uppercase)]
        for x in range(3):
            address = address + random.choice(int_or_char_list) + random.choice(int_or_char_list) + ":"
        address = address + random.choice(int_or_char_list) + random.choice(int_or_char_list)
        print(address)
    
    # Only integer MAC address generation
    elif input_value == 2:
        address = ""
        for x in range(3):
            address = address + str(random.randint(0,9)) + str(random.randint(0,9)) + ":"
        address = address + str(random.randint(0,9)) + str(random.randint(0,9))
        print(address)
    
    #Only character MAC address generation
    else:
        address = ""
        for x in range(3):
            address = address + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + ":"
        address = address + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        print(address)

generator()