
import os
import random
# from datetime import date
import time
import re
import hashlib
import sys
import fileinput

global regex
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def welcome():
    print("*" * 20)
    print("CHOOSE AN OPTION BELOW: ")
    print("*" * 20)
    print("1: OPEN AN ACCOUNT WITH US")
    print("2: DEPOSIT INTO YOUR ACCOUNT")
    print("3: WITHDRAW FROM YOUR ACCOUNT")
    print("4: CHANGE YOUR PIN")
    print("5: TRANSFER TO A FRIEND")
    print("*" * 20)


def hash_pin(pin):
    hashed_pin = int(hashlib.sha256(repr(pin).encode('utf-8')).hexdigest(), 16) % 10 ** 8
    return hashed_pin


def existing_email(mail):
    check = True
    master_email_list = {"_email": []}
    if os.stat("user.txt").st_size == 0:
        pass
    else:
        with open("user.txt", 'r') as checkMail:
            for data in checkMail:
                row_dict = eval(data)
                for email_key in row_dict:
                    if email_key == '_email':
                        master_email_list['_email'].append(row_dict[email_key])
                        # {'_email': ['kash@ymail.com', 'rejuk@gmail.com']}
                    else:
                        continue
                mail_values = master_email_list.values()
        for elem in list(mail_values):
            for found in elem:
                if mail == found:
                    print("Email already exists, try again")
                    check = False
                # print(master_email_list)
    return check


def find_object(field, object_list):
    """ Check obj_list to see if object with 'name' equal to 'field exists'"""
    for item in object_list:
        if item.name == field:
            return item
        return None


def valid_email(email):
    if re.search(regex, email):
        print("Validating Email.....")
        return email
    else:
        print("wrong Email:")


def display(questions):
    for x, y in questions.items():
        print("{}: {}".format(x, y))


def valid_number(pin):
    if len(pin) > 1:
        print("Choose using '1', '2', '3' ")
    elif pin in "[!@#$%^&*(),.?\":{}|<>\'\\/+=~`-_]":
        print("No special characters please")
    elif not pin.isdigit():
        print("Takes only numbers")
    else:
        return int(pin)


def valid_string(response):
    if response == " ":
        print("Name cannot be empty")
    elif not response.isalpha():
        print("Enter only valid characters without space")
    else:
        return response


class Registration:
    """This class handles registration of users and helps creating the account

        Argument:
        firstName (str): User first name
        lastName (str): User Last name
        age (int): users age
        occupation (string): users occupation
        account_number (int): Randomly generated unique account number
        account_type (Array of string): account type assigned based on age and occupation
        security_question (tuple of string): security question used to retrieve user data
        email (varying characters): valid email address
        pin (int): user security pin
        confirm_pin (int): user confirm pin

    """

    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._age = None
        self._occupation = None
        self._account_number = None
        self._security_question = None
        self._email = None
        self._pin = None
        self._account_type = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @staticmethod
    def take_first_name():
        while True:
            name = input("Enter your FirstName: ")
            if name == " ":
                print("Name cannot be empty")
            elif not name.isalpha():
                print("Enter only valid characters without space")
            else:
                return name.lower()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    @staticmethod
    def take_last_name():
        while True:
            name = input("Enter your LastName: ")
            if name == " ":
                print("Name cannot be empty")
            elif not name.isalpha():
                print("Enter only valid characters without space")
            else:
                return name.lower()

    @property
    def valid_pin(self):
        return self._pin

    @valid_pin.setter
    def valid_pin(self, pin):
        self._pin = pin

    @staticmethod
    def take_pin():
        while True:
            pin = input("Enter your four digit pin: ")
            if len(pin) != 4:
                print("Pin must be four digits only")
            elif pin in "[!@#$%^&*(),.?\":{}|<>\'\\/+=~`-_]":
                print("No special characters please")
            elif not pin.isdigit():
                print("Takes only numbers")
            else:
                while True:
                    confirm_pin = input("Confirm Your Pin: ")
                    if confirm_pin != pin:
                        print("Pin does not match")
                        continue
                    else:
                        return hash_pin(pin)
                # return int(pin)

    @property
    def valid_age(self):
        return self._age

    @valid_age.setter
    def valid_age(self, age):
        self._age = age

    @staticmethod
    def take_age():
        today = time.localtime()
        valid = True
        while valid:
            year = input("Enter your YEAR of birth: ")
            if valid:
                if len(year) != 4:
                    print("Year must be YYYY ")
                    continue
                elif not year.isdigit():
                    print("Not a valid year integer format")
                    continue
                elif int(year) > today[0] or int(year) < today[0] - 60:
                    print("put a valid year within a 60 year period from today")
                    continue
                else:
                    year = int(year)

            while True:
                month = input("Enter your month of Birth: ")
                if len(month) < 1 or len(month) > 2:
                    print("Month must be MM ")
                    continue
                elif not month.isdigit():
                    print("Enter a valid month integer")
                    continue
                elif int(month) < 1 or int(month) > 12:
                    print("it is a twelve month calendar fam")
                    continue
                else:
                    month = int(month)
                    break
            while True:
                day = input("Enter your day of birth: ")
                if len(day) < 1 or len(day) > 2:
                    print("day must be DD ")
                    continue
                elif not day.isdigit():
                    print("Enter a valid day integer")
                    continue
                elif int(day) < 1 or int(day) > 31:
                    print("it is a thirty one day month calendar fam")
                    continue
                elif month == 2 and int(day) > 28:
                    print("February has 29 days max")
                    continue
                else:
                    day = int(day)
                    break
            age = (int(year), int(month), int(day))
            yr = today[0] - year
            mnt = today[1] - month
            if age == " ":
                print("Age cannot be empty")
            elif yr <= 18 and mnt < 0:
                print("You are now {} years, {} months. Check back at age 18".format(yr - 1, mnt % 12))
                break
            else:
                return age

    @property
    def valid_job(self):
        return self._occupation

    @valid_job.setter
    def valid_job(self, name):
        self._occupation = name

    @staticmethod
    def take_job():
        while True:
            name = input("Enter your Occupation: ")
            if name == " ":
                print("Name cannot be empty")
            elif not name.isalpha():
                print("Enter only valid characters without space")
            else:
                return name.lower()

    @property
    def valid_account_number(self):
        return self._account_number

    @valid_account_number.setter
    def valid_account_number(self, number):
        self._account_number = number

    @staticmethod
    def create_account_number():
        number = random.randint(0, 10 ** 10)
        return number

    @property
    def security_answer(self):
        return self._security_question

    @security_answer.setter
    def security_answer(self, answer):
        self._security_question = answer

    @staticmethod
    def take_questions():
        questions = {"1": "What is your favorite food",
                     "2": "What is your favorite football team",
                     "3": "Mother's Maiden Name"}
        display(questions)
        while True:
            choice = input("Enter your choice(1 or 2 or 3): ")
            if choice in questions.keys():
                break
            else:
                print("Wrong choice Fam")
                continue
        while True:
            response = input("Enter your answer: ")
            if valid_string(response):
                break
            else:
                continue
        answer = questions.get(choice), response
        return answer

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def get_email(self, email):
        self._email = email

    @staticmethod
    def take_email():
        while True:
            email = input("Enter your email is this format 'info@info.com' ")
            if not existing_email(email):
                continue
            else:
                return valid_email(email)

    @property
    def account_type(self):
        for accounts in self.account_type:
            if len(self.account_type) == 0:
                return "Choose from our options of savings or current account"
            else:
                return accounts

    @account_type.setter
    def account_type(self, accounts):
        self.account_type = accounts

    @staticmethod
    def take_account_type():
        account_type = []
        print("Choose the Account option you want: \n")
        account_option = {"1": "SAVINGS ACCOUNT", "2": "CURRENT ACCOUNT"}
        display(account_option)
        while True:
            acc = input("Make a choice ")
            if acc in account_option.keys():
                account_type.append(account_option.get(acc))
                # return ''.join(map(str, account_type))
                return account_type
            else:
                print("Wrong choice make a selection ")
                continue

    def __str__(self):
        return "\tFirstName: {0._first_name}\n \tLastName: {0._last_name}\n " \
               "\tDate of Birth: {0._age}\n \tOccupation: {0._occupation}\n" \
               "\tAccount_Number: {0._account_number}\n \tSecurity_Q&A: {0._security_question}\n" \
               "\tEmail: {0._email}\n \tHashed_Pin: {0._pin}\n \tAccount_Type: {0._account_type}\n".format(self)


class Account(Registration):
    def __init__(self):
        self._balance = 1000.00
        super().__init__()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @staticmethod
    def top_up(account_number, pin):
        # obj_reg = {"_first_name": [], "_last_name": [], "_age": [], "_occupation": [], "_account_number": [],
        #  "_security_question": [], "_email": [], "_pin": [], "_account_type": []}
        num_lines = sum(1 for line in open('user.txt'))
        count = 0
        with open("user.txt", 'r') as obj:
            for obj_row in obj:
                count += 1
                obj_dict = eval(obj_row)
                if account_number == obj_dict['_account_number'] and hash_pin(pin) == obj_dict['_pin']:
                    print("Hello, " + obj_dict['_first_name'])
                    account_types = obj_dict['_account_type']
                else:
                    if num_lines == count:
                        print("Invalid Account or pin")
                    # print("Validating....")
                    continue
                while True:
                    deposit = input("Enter the Amount you want to top up to your account: ")
                    if not deposit.isdigit():
                        print("Invalid Amount")
                        continue
                    elif 'SAVINGS ACCOUNT' in account_types and int(deposit) > 500:
                        print('You cannot deposit more than 500 euros to your Savings Account')
                        continue
                    elif 'CURRENT ACCOUNT' in account_types and int(deposit) > 1000:
                        print('You cannot deposit more than 1000 euros to your Current Account')
                        continue
                    else:
                        obj_dict['_balance'] += float(deposit)
                        # obj_dict['_balance'] = self._balance
                        print("Your account hs been topped up with {} , Your Balance is {}"
                              .format(float(deposit), obj_dict["_balance"]))
                        # print(str(obj_dict['_account_number']))
                        break

                for line in fileinput.input("user.txt", inplace=1):
                    if str(obj_dict['_account_number']) in line:
                        lin_obj = line.replace(line, str(obj_dict))
                        sys.stdout.write(lin_obj + '\n')
                    else:
                        sys.stdout.write(line)
                return True

    @staticmethod
    def withdrawal(account_number, pin):
        num_lines = sum(1 for line in open('user.txt'))
        count = 0
        with open("user.txt", 'r') as reader:
            for line in reader:
                count += 1
                obj_dict = eval(line)
                if account_number == obj_dict['_account_number'] and hash_pin(pin) == obj_dict['_pin']:
                    print("Hello, " + obj_dict['_first_name'])
                    account_types = obj_dict['_account_type']
                else:
                    if num_lines == count:
                        print("Invalid Account or pin")
                    continue
                while True:
                    withdraw = input("Enter the Amount you want to withdraw from your account: ")
                    if not withdraw.isdigit():
                        print("Invalid Amount")
                        continue
                    elif 'SAVINGS ACCOUNT' in account_types and int(withdraw) > 500:
                        print('You cannot withdraw more than 500 euros from your Savings Account')
                        continue
                    elif 'CURRENT ACCOUNT' in account_types and int(withdraw) > 1000:
                        print('You cannot withdraw more than 1000 euros from your Current Account')
                        continue
                    elif int(withdraw) > obj_dict['_balance']:
                        print("Your balance is {}, you cannot withdraw more than you have. "
                              "".format(obj_dict['_balance']))
                        continue
                    elif int(withdraw) == obj_dict['_balance']:
                        print("You cannot leave your account empty, go to the help desk for clarifications")
                    else:
                        obj_dict['_balance'] -= float(withdraw)
                        print("You just withdrew {} form your account , Your Balance is {}"
                              .format(float(withdraw), obj_dict["_balance"]))
                        break

                for ln in fileinput.input("user.txt", inplace=1):
                    if str(obj_dict['_account_number']) in ln:
                        lin_obj = ln.replace(ln, str(obj_dict))
                        sys.stdout.write(lin_obj + '\n')
                    else:
                        sys.stdout.write(ln)
                return True

     @staticmethod
    def change_pin_code(account_number, pin):
        num_lines = sum(1 for line in open('user.txt'))
        count = 0
        with open("user.txt", 'r') as cpc:
            for obj_cpc in cpc:
                count += 1
                cpc_dict = eval(obj_cpc)
                if account_number == cpc_dict['_account_number'] and hash_pin(pin) == cpc_dict['_pin']:
                    print("Hello, " + cpc_dict['_first_name'])
                    takepin()




    def __str__(self):
        return "\tFirstName: {0._first_name}\n \tLastName: {0._last_name}\n " \
               "\tDate of Birth: {0._age}\n \tOccupation: {0._occupation}\n" \
               "\tAccount_Number: {0._account_number}\n \tSecurity_Q&A: {0._security_question}\n" \
               "\tEmail: {0._email}\n \tHashed_Pin: {0._pin}\n \tAccount_Type: {0._account_type}\n" \
               "\t Balance: {0._balance}\n".format(self)


if __name__ == "__main__":
    print("WELCOME TO MEGA BANK PLC, AT YOUR SERVICE. ")
    welcome()
    while True:
        new_customer = Account()
        choices = input("Make your choice: ")
        if not choices.isdigit():
            print("USE either '1', '2', '3', '4', '5' or 'Q' to EXIT application")
            continue
        elif choices.lower() == 'q':
            print("Thanks for Banking with us")
            exit()
        elif choices == 1:
            new_customer._email = new_customer.take_email()
            new_customer._account_type = new_customer.take_account_type()
            new_customer._pin = new_customer.take_pin()
            new_customer._first_name = new_customer.take_first_name()
            new_customer._last_name = new_customer.take_last_name()
            new_customer._age = new_customer.take_age()
            new_customer._occupation = new_customer.take_job()
            new_customer._account_number = new_customer.create_account_number()
            new_customer._security_question = new_customer.take_questions()
            with open("user.txt", 'a+') as users:
                print(vars(new_customer), file=users)
        elif choices == 2:
            while True:
                account_num = input("Enter your account Number: ")
                if not account_num.isdigit():
                    print("Account Number should be made up of only INTEGERS ")
                    continue
                else:
                    account_num = int(account_num)
                password = input("Enter your Pin: ")
                if not password.isdigit():
                    print("Pin should be made up of only INTEGERS ")
                    continue
                else:
                    password = int(password)
                    break
            new_customer._balance = new_customer.top_up(account_num, password)
        elif choices == 3:
            while True:
                account_num = input("Enter your account Number: ")
                if not account_num.isdigit():
                    print("Account Number should be made up of only INTEGERS ")
                    continue
                else:
                    account_num = int(account_num)
                password = input("Enter your Pin: ")
                if not password.isdigit():
                    print("Pin should be made up of only INTEGERS ")
                    continue
                else:
                    password = int(password)
                    break
            new_customer._balance = new_customer.withdrawal(account_num, password)
        elif choices == 4:





    # new_customer._balance = new_customer.withdrawal(6395910347, 2345)

    # pinn = hash_pin(2345)
    # print(pinn)

    #
    # # new_customer._email = new_customer.take_email()
    # # new_customer._account_type = new_customer.take_account_type()
    # # new_customer._pin = new_customer.take_pin()
    #

