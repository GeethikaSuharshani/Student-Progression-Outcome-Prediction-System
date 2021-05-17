# start of user-defined functions
def introduction():   # gives an introduction about the program
    print('''Hi, This program will be allowed you to get your students` progression outcome of this academic year.''')
    print()
    
def pass_input():    # get number of credits at pass
    global pass_credits
    global total_credits
    global index
    total_credits=0
    if index>=0 and index < len(pass_list):
        pass_credits=pass_list[index]
        print('Number of credits at pass(including condoned pass):', pass_credits)
        if pass_credits in credit_range:    # check whether the input is in the correct range
            total_credits+=pass_credits

def defer_input():    # get number of credits at defer
    global defer_credits
    global total_credits
    global index
    if index>=0 and index < len(defer_list):
        defer_credits=defer_list[index]
        print('Number of credits at defer:', defer_credits)
        if defer_credits in credit_range:   # check whether the input is in the correct range
            total_credits+=defer_credits

def fail_input():    # get number of credits at fail
    global fail_credits
    global total_credits
    global index
    if index>=0 and index < len(fail_list):
        fail_credits=fail_list[index]
        print('Number of credits at fail:', fail_credits)
        if fail_credits in credit_range:   # check whether the input is in the correct range
            total_credits+=fail_credits

def result():  # check the progression outcome of the student
    global progression_outcome
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

    print('This student`s progression outcome of this academic year is',progression_outcome)
    print()

def credit_total():   # check whether the total of credits entered equals to 120
    if total_credits == 120:
        result()

def histogram_count():   # keeps a count of progress,trailing,retriever and excluded students
    global progression_outcome
    global Progress
    global Trailing
    global Retriever
    global Excluded
    global total_outcome
    global quit_program

    if progression_outcome == 'Progress':
        Progress+=1
    elif progression_outcome == 'Progress - module trailer':
        Trailing+=1
    elif progression_outcome == 'Do not Progress - module retriever':
        Retriever+=1
    else:
        Excluded+=1

    total_outcome=Progress + Trailing + Retriever + Excluded   # total number of progression outcomes
    if index>=0 and index<len(pass_list):
        quit_program=str(input("If you want to quit the program please enter 'q':"))
        quit_program=quit_program.lower()  # return a copy of the string with all the cased characters converted to lowercase 
    else:
        print('You have reached to the end of process')

def histogram():  # makes a histogram of progress,trailing,retriever and excluded students
    global Progress
    global Trailing
    global Retriever
    global Excluded
    global total_outcome

    print('Progress', Progress, ':', '*'*Progress)
    print('Trailing', Trailing, ':', '*'*Trailing)
    print('Retriever', Retriever, ':', '*'*Retriever)
    print('Excluded', Excluded, ':', '*'*Excluded)

    print('There are', total_outcome, 'outcomes in total.')
# end of user-defined functions

# main program starts from here    
credit_range=[0, 20, 40, 60, 80, 100, 120]    # credit range
pass_list=[120, 100, 100, 80, 60, 40, 20, 20, 20, 0]
defer_list=[0, 20, 0, 20, 40, 40, 40, 20, 0, 0]
fail_list=[0, 0, 20, 20, 20, 40, 60, 80, 100, 120]
quit_program=''
Progress=0
Trailing=0
Retriever=0
Excluded=0
index=0

introduction()
while quit_program != 'q' and index>=0 and index<len(pass_list):   # program iterate until the user enter 'q' to quit
    pass_input()
    defer_input()
    fail_input()
    credit_total()
    histogram_count()
    index+=1

histogram()      
print('Now you are exiting from the program.')
# end of main program
