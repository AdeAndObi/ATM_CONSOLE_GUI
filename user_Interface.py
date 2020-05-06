import tkinter
import shelve
import validate_email
import datetime
# noinspection PyUnresolvedReferences
from bank import Account


def clear():
    global name_entry, dob_entry, occupation_entry, email_entry, pin_entry, answer_entry, dob, occupation, \
        email, pin, answer
    name_entry.delete(0, len(name.get()))
    dob_entry.delete(0, len(dob.get()))
    occupation_entry.delete(0, len(occupation.get()))
    rbvalue.set(1)
    email_entry.delete(0, len(email.get()))
    pin_entry.delete(0, len(pin.get()))
    question_values.set('--select--')
    answer_entry.delete(0, len(answer.get()))


def get_value():
    name_value = ""
    occupation_value = ""
    email_value = ""
    pin_value = ""
    dob_value = ""
    # check for name format
    if name.get().isalpha():
        name_value = name.get()
        tkinter.Label(account_open_canvas, text='                                                  ', bg='blue',
                      fg='white').grid(row=1, column=1, sticky='w')
    elif name.get() == "":
        tkinter.Label(account_open_canvas, text='Name field can not be empty', bg='blue',
                      fg='white').grid(row=1, column=1, sticky='w')
    else:
        tkinter.Label(account_open_canvas, text='Name can only be alphabets', bg='blue',
                      fg='white').grid(row=1, column=1, sticky='w')
    # validate date
    if dob.get() != "":
        try:
            dob_value = dob.get()
            datetime.datetime.strptime(dob_value, '%d.%m.%Y')
        except ValueError:
            tkinter.Label(account_open_canvas, text='Incorrect date format, should be DD.MM.YYYY', bg='blue',
                          fg='white').grid(row=3, column=1, sticky='w')
            dob_value = ""  # default the entry once there is an error
    else:
        tkinter.Label(account_open_canvas, text='Date of Birth field can not be empty', bg='blue',
                      fg='white').grid(row=3, column=1, sticky='w')
    # check for occupation format
    if occupation.get().isalpha():
        occupation_value = occupation.get()
        tkinter.Label(account_open_canvas, text='                                                  ', bg='blue',
                      fg='white').grid(row=5, column=1, sticky='w')
    elif occupation.get() == "":
        tkinter.Label(account_open_canvas, text='Occupation field can not be empty', bg='blue',
                      fg='white').grid(row=5, column=1, sticky='w')
    else:
        tkinter.Label(account_open_canvas, text='Occupation can only be alphabets', bg='blue',
                      fg='white').grid(row=5, column=1, sticky='w')
    # check for email format
    if email_value == "":
        tkinter.Label(account_open_canvas, text="e_mail field can not be empty", bg='blue',
                      fg='white').grid(row=8, column=1, sticky='w')
    elif not validate_email.validate_email(email.get(), verify=False):
        tkinter.Label(account_open_canvas, text="Incorrect email address", bg='blue',
                      fg='white').grid(row=8, column=1, sticky='w')
    else:
        email_value = email.get()
    # check for pin format
    try:
        pin_value = int(pin.get())
        if len(pin.get()) != 4:
            tkinter.Label(account_open_canvas, text='PIN must be four digits', bg='blue',
                          fg='white').grid(row=10, column=1, sticky='w')
        else:
            tkinter.Label(account_open_canvas, text='                                               ', bg='blue',
                          fg='white').grid(row=10, column=1, sticky='w')
    except ValueError:
        tkinter.Label(account_open_canvas, text='PIN can only be digits', bg='blue',
                      fg='white').grid(row=10, column=1, sticky='w')

    if name_value != "" and occupation_value != "" and email_value != "" and pin_value != "" and dob_value != "":
        new_account = Account()
        new_account._name = name_value
        new_account._date_of_birth = dob_value
        new_account._occupation = occupation_value
        new_account._account_type = rbvalue.get()
        new_account._account_number = new_account.generate_account_number()
        new_account._email = email_value
        new_account._pin = pin_value
        new_account._security_question = question_values.get()
        new_account._security_answer = answer.get()

        print(new_account)


def home_screen():
    global account_number
    account_canvas.grid(row=1, column=0, rowspan=2, sticky='nsew')
    account_canvas.rowconfigure(0, weight=10)
    account_canvas.rowconfigure(1, weight=1)
    account_canvas.columnconfigure(0, weight=20)
    account_canvas.columnconfigure(1, weight=1)
    account_canvas.columnconfigure(2, weight=29)

    display_text = tkinter.Label(message_canvas, text='Welcome to Stunner Bank\nPlease enter your account number',
                                 bg='yellow', fg='blue')
    display_text.grid(row=0, column=0)

    tkinter.Label(account_canvas, text='Account Number:', background='blue', fg='white').grid(row=0, column=0,
                                                                                              sticky='e')

    account_number_field = tkinter.Entry(account_canvas, textvariable=account_number, relief='sunken')
    account_number_field.grid(row=0, column=1, sticky='w')

    button_frame = tkinter.Frame(account_canvas)
    button_frame.rowconfigure(0, weight=1)
    button_frame.columnconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)
    button_frame.grid(row=0, column=2, sticky='w')

    tkinter.Button(button_frame, text='Enter', command=transaction_window).grid(row=0, column=0, sticky='e')
    tkinter.Button(button_frame, text='Open Account', command=open_account).grid(row=0, column=1, sticky='w')


def open_account():
    global account_canvas, rbvalue, question_values, email, pin, answer, name_entry
    account_canvas.destroy()  # destroy account_canvas(home screen)

    account_open_canvas.grid(row=1, column=0, sticky='nsew')  # add account canvas to the window
    # add labels to account open canvas
    tkinter.Label(account_open_canvas, text='Name:', bg='blue', fg='white').grid(row=0, column=0, sticky='e')
    tkinter.Label(account_open_canvas, text='Date of Birth:', bg='blue', fg='white').grid(row=2, column=0, sticky='e')
    tkinter.Label(account_open_canvas, text='Occupation:', bg='blue', fg='white').grid(row=4, column=0, sticky='e')
    tkinter.Label(account_open_canvas, text='Account Type:', bg='blue', fg='white').grid(row=6, column=0, sticky='e')
    tkinter.Label(account_open_canvas, text='E-mail:', bg='blue', fg='white').grid(row=7, column=0, sticky='e')
    tkinter.Label(account_open_canvas, text='PIN:', bg='blue', fg='white').grid(row=9, column=0, sticky='e')
    tkinter.Label(account_open_canvas, text='Security Question:', bg='blue', fg='white').grid(row=11, column=0,
                                                                                              sticky='e')
    tkinter.Label(account_open_canvas, text='Answer:', bg='blue', fg='white').grid(row=12, column=0, sticky='e')
    # entry to receive name
    name_entry.grid(row=0, column=1, sticky='w')
    # Entry for date of birth
    dob_frame.rowconfigure(0, weight=1)
    dob_frame.columnconfigure(0, weight=50)
    dob_frame.columnconfigure(1, weight=10)
    dob_frame.grid(row=2, column=1, sticky='w')
    dob_entry.grid(row=0, column=0, sticky='w')
    tkinter.Label(dob_frame, text='DD.MM.YYYY', bg='blue', fg='white').grid(row=0, column=1, sticky='w')
    # entry for occupation
    occupation_entry.grid(row=4, column=1, sticky='w')
    # radio button to select account
    radio_frame = tkinter.Frame(account_open_canvas)
    radio_frame.grid(row=6, column=1, sticky='w')
    rbvalue.set(1)
    tkinter.Radiobutton(radio_frame, text='Savings Account', bg='blue', fg='white', value=1, variable=rbvalue,
                        selectcolor='blue').grid(row=0, column=0)
    tkinter.Radiobutton(radio_frame, text='Current Account', bg='blue', fg='white', value=2, variable=rbvalue,
                        selectcolor='blue').grid(row=1, column=0)
    # email entry
    email_entry.grid(row=7, column=1, sticky='w')
    # pin entry
    pin_entry.grid(row=9, column=1, sticky='w')
    # menu for security question
    questions = {'Who is your Daddy', 'What is the name of your first pet', 'What is you mother\'s maiden name'}
    question_menu = tkinter.OptionMenu(account_open_canvas, question_values, *questions)
    question_menu.grid(row=11, column=1, sticky='w')
    # security answer entry
    answer_entry.grid(row=12, column=1, sticky='w')

    new_button_frame = tkinter.Frame(account_open_canvas)
    new_button_frame.rowconfigure(0, weight=1)
    new_button_frame.rowconfigure(1, weight=1)
    new_button_frame.rowconfigure(2, weight=1)
    new_button_frame.grid(row=12, column=2)

    tkinter.Button(new_button_frame, text='Submit', command=get_value).grid(row=0, column=1)
    tkinter.Button(new_button_frame, text='Clear', command=clear).grid(row=0, column=0)
    tkinter.Button(new_button_frame, text='Quit', command=quit_).grid(row=0, column=2)
    # configure row weight
    account_open_canvas.rowconfigure(0, weight=50)
    account_open_canvas.rowconfigure(1, weight=1)
    account_open_canvas.rowconfigure(2, weight=50)
    account_open_canvas.rowconfigure(3, weight=1)
    account_open_canvas.rowconfigure(4, weight=50)
    account_open_canvas.rowconfigure(5, weight=1)
    account_open_canvas.rowconfigure(6, weight=50)
    account_open_canvas.rowconfigure(7, weight=50)
    account_open_canvas.rowconfigure(8, weight=1)
    account_open_canvas.rowconfigure(9, weight=50)
    account_open_canvas.rowconfigure(10, weight=1)
    account_open_canvas.rowconfigure(11, weight=50)
    account_open_canvas.rowconfigure(12, weight=50)
    # configure column weight
    account_open_canvas.columnconfigure(0, weight=1)
    account_open_canvas.columnconfigure(1, weight=10)
    account_open_canvas.columnconfigure(2, weight=1)
    # create account_canvas(home screen) back
    account_canvas = tkinter.Frame(mainWindow, relief='sunken', borderwidth=3, background='blue')


def quit_():
    global account_open_canvas, name_entry, dob_frame, dob_entry, occupation_entry, email_entry, pin_entry, answer_entry
    clear()
    account_open_canvas.destroy()
    home_screen()
    account_open_canvas = tkinter.Frame(mainWindow, relief='sunken', borderwidth=3, background='blue')
    name_entry = tkinter.Entry(account_open_canvas, relief='sunken', bg='white', textvariable=name)
    dob_frame = tkinter.Frame(account_open_canvas, bg='blue')
    dob_entry = tkinter.Entry(dob_frame, relief='sunken', textvariable=dob)
    occupation_entry = tkinter.Entry(account_open_canvas, relief='sunken', textvariable=occupation)
    email_entry = tkinter.Entry(account_open_canvas, relief='sunken', textvariable=email)
    pin_entry = tkinter.Entry(account_open_canvas, relief='sunken', show='*', textvariable=pin)
    answer_entry = tkinter.Entry(account_open_canvas, relief='sunken', textvariable=answer)


def transaction_window():
    txt = account_number.get()

    with shelve.open('AccountDB') as db:
        if txt in db.keys():
            account = db[txt]

            global account_canvas
            account_canvas.destroy()

            transaction_canvas.grid(row=1, column=0, sticky='nsew')
            transaction_canvas.rowconfigure(0, weight=1)
            transaction_canvas.rowconfigure(1, weight=1)
            transaction_canvas.rowconfigure(2, weight=1)
            transaction_canvas.rowconfigure(3, weight=1)
            transaction_canvas.columnconfigure(0, weight=1)
            transaction_canvas.columnconfigure(1, weight=1)

            tkinter.Button(transaction_canvas, text='Check Balance', bg='blue', fg='white', relief='flat',
                           command=account.check_balance).grid(row=0, column=0)
            tkinter.Button(transaction_canvas, text='Deposit', bg='blue', fg='white', relief='flat',
                           command=account.deposit).grid(row=1, column=0)
            tkinter.Button(transaction_canvas, text='Withdrawal', bg='blue', fg='white', relief='flat',
                           command=account.withdrawal).grid(row=2, column=0)
            tkinter.Button(transaction_canvas, text='Transfer', bg='blue', fg='white', relief='flat',
                           command=account.transfer).grid(row=0, column=1)
            tkinter.Button(transaction_canvas, text='Change PIN', bg='blue', fg='white', relief='flat',
                           command=account.change_pin).grid(row=1, column=1)

            button_frame = tkinter.Frame(transaction_canvas)
            button_frame.grid(row=3, column=1)

            tkinter.Button(button_frame, text='Quit', bg='blue', fg='white', command=home_screen).grid()

            account_canvas = tkinter.Canvas(mainWindow, relief='sunken', borderwidth=3, background='blue')
            account_number.__del__()
        else:
            tkinter.Label(account_canvas, text='Account does not exist',
                          bg='blue', fg='white').grid(row=1, column=1, sticky='n')


if __name__ == "__main__":
    mainWindow = tkinter.Tk()
    mainWindow.title("Stunner Bank")
    mainWindow.geometry('640x480')

    mainWindow.columnconfigure(0, weight=1)
    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=20)

    message_canvas = tkinter.Frame(mainWindow, relief='raised', borderwidth=3, background='yellow')
    message_canvas.grid(row=0, column=0, sticky='nsew')
    message_canvas.rowconfigure(0, weight=1)
    message_canvas.columnconfigure(0, weight=1)

    account_canvas = tkinter.Canvas(mainWindow, relief='sunken', borderwidth=3, background='blue')
    account_open_canvas = tkinter.Canvas(mainWindow, relief='sunken', borderwidth=3, background='blue')
    transaction_canvas = tkinter.Canvas(mainWindow, relief='sunken', borderwidth=3, background='blue')
    account_number = tkinter.StringVar()
    # variables that will be need for account open
    name = tkinter.StringVar()
    name_entry = tkinter.Entry(account_open_canvas, relief='sunken', bg='white', textvariable=name)
    dob = tkinter.StringVar()
    dob_frame = tkinter.Frame(account_open_canvas, bg='blue')
    dob_entry = tkinter.Entry(dob_frame, relief='sunken', textvariable=dob)
    occupation = tkinter.StringVar()
    occupation_entry = tkinter.Entry(account_open_canvas, relief='sunken', textvariable=occupation)
    email = tkinter.StringVar()
    email_entry = tkinter.Entry(account_open_canvas, relief='sunken', textvariable=email)
    pin = tkinter.StringVar()
    pin_entry = tkinter.Entry(account_open_canvas, relief='sunken', show='*', textvariable=pin)
    rbvalue = tkinter.IntVar()
    question_values = tkinter.StringVar()
    question_values.set('--select--')
    answer = tkinter.StringVar()
    answer_entry = tkinter.Entry(account_open_canvas, relief='sunken', textvariable=answer)
    # welcome screen
    home_screen()

    mainWindow.mainloop()
