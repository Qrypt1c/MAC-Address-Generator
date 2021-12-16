import random
import string
import platform
import os

def platformCheck(address):
    if platform.system() == 'Windows':
        f = open("mac_addr.txt", "w")
        f.write("Here is your generated MAC address: " + address)
        f.close()
        os.startfile("mac_addr.txt")

def generator():
    while True:
        try:
            if platform.system() == 'Windows':
                print("***You are using Windows, so expect to have a text file to open after choosing an option***")
                print("\n")
            input_value = int(input("Choose a type of MAC Address:\n" +  "1) Default\n" + "2) Only Integer\n" + "3) Only Character\n"))
            if input_value > 0 and input_value < 4:
                break
            else: 
                print("Choose '1', '2', or '3'")
                continue
        except:
            print("Choose '1', '2', or '3'")
    alphabet = ['A','B','C','D','E','F']
    
    # Default MAC address Generation
    if input_value == 1:
        address = ""
        int_or_char_list1 = [str(random.randint(0,9)), random.choice(alphabet)]
        int_or_char_list2 = [str(random.randint(0,9)), random.choice(alphabet)]
        int_or_char_list3 = [str(random.randint(0,9)), random.choice(alphabet)]
        int_or_char_list4 = [str(random.randint(0,9)), random.choice(alphabet)]
        int_or_char_list5 = [str(random.randint(0,9)), random.choice(alphabet)]
        int_or_char_list6 = [str(random.randint(0,9)), random.choice(alphabet)]
        address = random.choice(int_or_char_list1) + random.choice(int_or_char_list1) + ":" + random.choice(int_or_char_list2) + random.choice(int_or_char_list2) + ":" + random.choice(int_or_char_list3) + random.choice(int_or_char_list3) + ":" + random.choice(int_or_char_list4) + random.choice(int_or_char_list4) + ":" + random.choice(int_or_char_list5) + random.choice(int_or_char_list5) + ":" + random.choice(int_or_char_list6) + random.choice(int_or_char_list6)
        print(address)
        platformCheck(address)
    
    # Only integer MAC address generation
    elif input_value == 2:
        address = ""
        for x in range(5):
            address = address + str(random.randint(0,9)) + str(random.randint(0,9)) + ":"
        address = address + str(random.randint(0,9)) + str(random.randint(0,9))
        print(address)
        platformCheck(address)
    
    #Only character MAC address generation
    else:
        address = ""
        for x in range(5):
            address = address + random.choice(alphabet) + random.choice(alphabet) + ":"
        address = address + random.choice(alphabet) + random.choice(alphabet)
        print(address)
        platformCheck(address)

generator()