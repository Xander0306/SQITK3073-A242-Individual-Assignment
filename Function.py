import pandas as pd
import sys


def login_user(username, ic_number, password):
    file_path = r'A:\UUM\Sem 4\Business ANalytics\Excel\\' + username + '.csv'

    try:
        df = pd.read_csv(file_path, header=None)
        username_cell = df.iloc[1, 0]
        password_cell = df.iloc[1, 2]


        if username == username_cell and password == password_cell:
            if len(ic_number) == 12 and password == password_cell:
                return('Welcome ' + username.upper())
            else:
                print('Username or Password incorrect. Please try again.')
                prompt_login_again()
        else:
            print('Username or Password incorrect. Please try again.')
            prompt_login_again()
    except FileNotFoundError:
        regyn = input('User Not Found. Would you like to register an account (Y/N): ').upper()
        if regyn == 'Y':
            register_user()
        else:
            print('Thank you for using our service.')
            sys.exit()
            


def prompt_login_again():
    print("Welcome TO Malaysia Tax Input Program")
    username = input("Please Input Your Username: ")
    ic_number = input("Please Input Your IC Number: ")
    password = ic_number[8:13]
    login_user(username, ic_number, password)


def register_user():
    username = input("Please Input Your Username: ")
    ic_number = input("Please Input Your IC Number: ")
    password = ic_number[8:13]

    data = {
        'username': [username],
        'ic_number': [ic_number],
        'password': [password]
    }

    new_df = pd.DataFrame(data)
    file_path = r'A:\UUM\Sem 4\Business ANalytics\Excel\\' + username + '.csv'
    new_df.to_csv(file_path, index=False)
    print('Registration successful.')
    prompt_login_again()


def tax_prompt(income,tax_year):

    print('-----Tax Relief-----')
    print('Key In Value According To Each Category')  
    while True:
        if income <= 5000:
            tax_rate = 0
            tax_payable = income * tax_rate
            category = 'A'
        elif 5000 < income <= 20000:
            tax_rate = 0.01
            tax_payable = income * tax_rate
            category = 'B'
        elif 20000 < income <= 35000:
            tax_rate = 0.03
            tax_payable = 150 + (income * tax_rate)
            category = 'C'
        elif 35000 < income <= 50000:
            tax_rate = 0.06
            tax_payable = 600 + (income * tax_rate)
            category = 'D'
        elif 50000 < income <= 70000:
            tax_rate = 0.11
            tax_payable = 1500 + (income * tax_rate)
            category = 'E'
        elif 70000 < income <= 100000:
            tax_rate = 0.19
            tax_payable = 3700 + (income * tax_rate)
            category = 'F'
        elif 100000 < income <= 400000:
            tax_rate = 0.25
            tax_payable = 9400 + (income * tax_rate)
            category = 'G'
        elif 400000 < income <= 600000:
            tax_rate = 0.26
            tax_payable = 84400 + (income * tax_rate)
            category = 'H'
        elif 600000 < income <= 2000000:
            tax_rate = 0.28
            tax_payable = 136400 + (income * tax_rate)
            category = 'I'
        elif income > 2000000:
            tax_rate = 0.30
            tax_payable = 528400 + (income * tax_rate)
            category = 'J'
        else:
            print("Please Input A Valid Number")
            break


    while True:
        indi_tax_relief = float(input('Individual Tax Relief (Limited To RM9000): RM'))
        if 0 <= indi_tax_relief <= 9000:
            break
        else:
            print('Individual Tax Relief Exceeds Limit. Please Try Again.')

    while True:
        spouse_tax_relief = float(input('No income Resident Spouse Tax Relief (Limited to  RM4000): RM'))
        if 0 <= spouse_tax_relief <= 4000:
            break
        else:
            print('Spouse Tax Relief Exceeds Limit. Please Try Again')

    while True:
        num_child = float(input('Number of Childern: '))
        child_tax_relief = float(input('Child Tax Relief(RM8000 per child up to 12 child): RM'))
        limit = num_child * 8000
        if 0 <= child_tax_relief <= limit:
            break
        else:
            print('Child Tax Relief Exceeds Limit. Please Try Again')

    while True:
        medical_tax_relief = float(input('Serious Medical Tax Relief(Limited To RM8000): RM'))
        if 0 <= medical_tax_relief <= 8000:
            break
        else:
            print('Medical Tax Relief Exceeds Limit. Please Try Again')   

    while True:
        lifestyle_tax_relief = float(input('Lifestyle Tax Relief(Limited to RM2500): RM'))
        if 0 <= lifestyle_tax_relief <= 2500:
            break
        else:
            print('Lifestyle Tax Relief Exceeds Limit. Please Try Again')       

    while True:
        edu_tax_relief = float(input('Education Tax Relief(Limited to RM7000) :RM'))
        if 0 <= edu_tax_relief <= 7000:
            break
        else:
            print('Education Tax Relief Exceeds Limit. Please Try Again')           

    while True:
        par_tax_relief = float(input('Parent Tax Relief(Limited To RM5000): RM'))
        if 0 <= par_tax_relief <= 5000:
            break
        else:
            print('Parent Tax Relief Exceeds Limit. Please Try Again') 

                            
    tax_relief = (indi_tax_relief + spouse_tax_relief + child_tax_relief + medical_tax_relief + lifestyle_tax_relief + edu_tax_relief + par_tax_relief)
    

    final_pay = tax_payable - tax_relief
    net_income = income - final_pay

    tax_data = {
        'Individual Tax Relief': indi_tax_relief,
        'Spouse Tax Relief': spouse_tax_relief,
        'Child Tax Relief': child_tax_relief,
        'Medical Tax Relief': medical_tax_relief,
        'Lifestyle Tax Relief': lifestyle_tax_relief,
        'Education Tax Relief': edu_tax_relief,
        'Parent Tax Relief ': par_tax_relief,
    }

    result = {
        'Gross Income ' : income, 
        'Income Tax Category' : 'Category ' + category,
        'Income Tax Amount ' : tax_payable,
        'Total Tax Relief ' : tax_relief,
        'Your Payable Tax Is ' : final_pay,
        'Net Income After Taxes ' : net_income,
    }

    print('Year: ' + tax_year)

    print('=====Tax Details=====')
    for key,value in tax_data.items():
        print(f"{key}: {value}")
    print('\n')
    print('=====Tax Summary=====')
    for key,value in result.items():
        print(f"{key}: {value}")


    return tax_data, result

import pandas as pd

def save_to_csv(username, tax_year, tax_data, result):
    file_path = r'A:\UUM\Sem 4\Business ANalytics\Excel\\' + username + '.csv'

    tax_year_df = pd.DataFrame([['Year', tax_year]], columns=['Description', 'Amount (RM)'])
    
    combined_data = {**tax_data, **result}
    tax_df = pd.DataFrame(combined_data.items(), columns=['Description', 'Amount (RM)'])

    tax_year_df.to_csv(file_path, mode='a', header=False, index=False)
    tax_df.to_csv(file_path, mode='a', header=False, index=False)
    
    print('Successfully Saved')


def file_read_csv(username):
    file_path = r'A:\UUM\Sem 4\Business ANalytics\Excel\\' + username + '.csv'
    updated_csv = pd.read_csv(file_path)

    print(updated_csv)
