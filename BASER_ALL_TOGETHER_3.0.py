# libraries
import itertools
import os

# logo
logo = '''
                             ██████╗  █████╗ ███████╗███████╗██████╗ 
                             ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
                             ██████╔╝███████║███████╗█████╗  ██████╔╝
                             ██╔══██╗██╔══██║╚════██║██╔══╝  ██╔══██╗
                             ██████╔╝██║  ██║███████║███████╗██║  ██║
                             ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
   
                                         author: MearWix
                                    version:BASER_PASSWORDS_1.2


   #############################################################################################
   |                                         WARNING!                                          |
   |             THE RESULT WILL BE SAVED TO THE FOLDER WHERE IS THAT PROGRAM!                 |
   |             AUTHOR IS NOT RESPONSIBLE FOR HOW THIS PROGRAMM WILL BE USED!                 |
   |                                         GOOD LUCK!                                        |
   #############################################################################################

'''
print(logo)

alphabet = "abcdefghijklmnopqrstuvxyz"
digits = "0123456789"

length = int(input("Enter a length of your password: "))

# choice
print("What mode of generation you want to use: ")
print("(1) Only numbers\n(2) Only letters\n(3) Letters and numbers")
choice = int(input("Write a number of a mode: "))

pass_chars = ""


while True:
    if choice == 1:
        pass_chars = digits
        break
    # code of a mode 2
    elif choice == 2:
        pass_chars = alphabet + alphabet.upper()
        break
    elif choice == 3:
        pass_chars = digits + alphabet + alphabet.upper()
        break

result_list = list(itertools.product(pass_chars, repeat=length))

with open("base.txt", "w") as f:
    for elem in result_list:
        f.write("".join(elem)+"\n")

print("\n\nWell done! Your base for brut was saved to the file 'base.txt'. Good afternoon!")
os.system('pause')
