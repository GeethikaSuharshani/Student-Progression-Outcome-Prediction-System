# start of user-defined functions
def introduction():  # gives an introduction about the program
    print('''Hi, This program will be allowed you to get your progression outcome of this academic year.''')
    print()
    print('To get your progression outcome, please enter the following details')
    print()

def pass_input():  # get number of credits at pass and validate the user input
    try:
        global pass_credits
        global total_credits
        total_credits=0
        pass_credits=int(input('Number of credits at pass(including condoned pass) :'))
        if pass_credits in credit_range:  # check whether the input is in the correct range
            total_credits+=pass_credits
        else:
            print('Number of credits at pass, should be in the range 0,20,40,60,80,100 and 120.So please try again with a valid credit value within this range.')
            pass_input()
    except:
        print('Number of credits at pass should be an integer.So please enter a valid integer.')
        pass_input()

def defer_input():  # get number of credits at defer and validate the use input
    try:
        global defer_credits
        global total_credits
        defer_credits=int(input('Number of credits at defer :'))
        if defer_credits in credit_range:  # check whether the input is in the correct range
            total_credits+=defer_credits
        else:
            print('Number of credits at defer, should be in the range 0,20,40,60,80,100 and 120.So please try again with a valid credit value within this range.')
            defer_input()
    except:
        print('Number of credits at defer should be an integer.So please enter a valid integer.')
        defer_input()

def fail_input():  # get number of credits at fail and validate the user input
    try:
        global fail_credits
        global total_credits
        fail_credits=int(input('Number of credits at fail :'))
        if fail_credits in credit_range:  # check whether the input is in the correct range
            total_credits+=fail_credits
        else:
            print('Number of credits at fail, should be in the range 0,20,40,60,80,100 and 120.So please try again with a valid credit value within this range.')
            fail_input()
    except:
        print('Number of credits at fail should be an integer.So please enter a valid integer.')
        fail_input()

def result():  # check the progression outcome of the student
    if pass_credits == 120:
        progression_outcome='Progress'   # progress
    elif pass_credits == 100:
        progression_outcome='Progress - module trailer'   # trailing
    elif pass_credits == 80:
        progression_outcome='Do not Progress - module retriever'   # retriever
    elif pass_credits == 60:
        progression_outcome='Do not Progress - module retriever'   # retriever
    elif pass_credits == 40:
        if defer_credits == 0:
            progression_outcome='Exclude'   # excluded
        else:
            progression_outcome='Do not Progress - module retriever'   # retriever
    elif pass_credits == 20:
        if defer_credits == 20 or defer_credits == 0:
            progression_outcome='Exclude'   # excluded
        else:
            progression_outcome='Do not Progress - module retriever'   # retriever
    else:
        if pass_credits == 0:
            if defer_credits == 40 or defer_credits == 20 or defer_credits == 0:
                progression_outcome='Exclude'   # excluded
            else:
                progression_outcome='Do not Progress - module retriever'   # retriever

    print('Your progression outcome of this academic year is:', progression_outcome)
    print()

def credit_total():  # check whether the total of credits entered equals to 120
    global total_credits
    if total_credits == 120:
        result()
    else:
        print('The total of the credits you have entered is not 120.Please try again with correct credit values.')
        pass_input()
        defer_input()
        fail_input()
        credit_total()
# end of user-defined functions

# main program starts from here
credit_range=[0, 20, 40, 60, 80, 100, 120]  # credit range

introduction()
pass_input()
defer_input()
fail_input()
credit_total()
# end of main program
