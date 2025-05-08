import pandas as pd
import sys
from Function import login_user, tax_prompt, save_to_csv,file_read_csv


print("Welcome TO Malaysia Tax Input Program")
username = input("Please Input Your Username: ")
ic_number = input("Please Input Your IC Number: ")
password = ic_number[8:13]

login_user(username,ic_number,password)

while True:
    print('========== What would you like to do today? ==========')
    print('Option 1: Calculate Taxes')
    print('Option 2: View Past Tax Infomation')
    print('Option 3: Logout ')
    option_ans = int(input('Your choice: '))

    match option_ans:
        case 1: 
            tax_year = input("Please enter the tax year (e.g., 2024): ")
            income = float(input("Please Key In Your Annual Income Amount: "))
            tax_data, result = tax_prompt(income,tax_year)
            save = input("Would you like to save your tax data? (Y/N): ").upper()
            if save == 'Y':
                save_to_csv(username,tax_year,tax_data, result)
                priyn = input('Would you like to view the information saved? (Y/N): ').upper()
                if priyn == 'Y':
                    file_read_csv(username)
                else:
                    print('Thank Your For Using Malaysia Tax Input Program.')
            else:
                print("Data not saved.")

        case 2:
            file_read_csv(username)

        case 3:
            print('Thank Your For Using Malaysia Tax Input Program. You will be automatically Logged Out.')
            sys.exit()

    
