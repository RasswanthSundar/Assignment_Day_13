try:
    import tkinter as tk
except:
    print('Import Not Avilable')
    raise ImportError

# Setting up gui for calculator
win = tk.Tk()
win.geometry("300x380")
win.title('Calculator')
win.configure(bg = '#E5E4E2')
win.resizable(0, 0)

#Initialize the values
answer = '0'
history = '0'
num_count = 0
point_count = 0
oper_count = 0
equal_count = 0

#Setting up output and input frames
outfra = tk.Frame(win, bg = '#E5E4E2')
outfra.place(relx = 0.0125, relwidth = 0.975, relheight = 0.2)
infra = tk.Frame(win, bg = '#E5E4E2')
infra.place(relx = 0.0125, rely = 0.2, relwidth = 0.975, relheight = 0.7875)

#Setting up lables for history
his = tk.StringVar()
text = tk.Label(outfra, anchor = 'se', bg = '#E5E4E2', textvariable = his, font = ('arial', 10))
text.place(relheight = 0.4, relwidth = 0.975)
his.set(history)

#Setting up lables for output
val = tk.StringVar()
out = tk.Label(outfra, anchor = 'se', bg = '#E5E4E2', textvariable = val, font = ('arial', 32))
out.place(rely = 0.4, relheight = 0.6, relwidth = 1)
val.set(answer)

def num_but(num):
    '''
        This function will be triggred on 
        the action of the any numerical button 
        and will be entered into the output lable
    '''
    # Global declaration to use within the function
    global answer, num_count, equal_count, point_count, history

    # Checking if equal is pressed and initalizing the output
    if equal_count == 1:
        num_count = 0
        point_count = 0
        history = ''
        equal_count = 0

    # Checking for num count is zero or not
    if num_count == 0:
        # If zero assign it to the answer
        answer = num  
        # Set num count to 1 if the count is zero
        num_count = 1
    else:
        # Else append the number to the answer string
        answer += num

    
    # Call out the output and history function
    update_output()
    update_history()

def point_but():
    '''
        This function will add a point if there
        are not any points else it won't execute
    '''
    # Global declaration to use within the function
    global point_count, equal_count

    # Check if point count is zero or not
    if point_count == 0:
        # If zero change it to 1
        point_count = 1
        # Global declaration to use within the function
        global answer,num_count
        # Check the number is there or not 

        if num_count == 0:
            # If not there add a point to zero in the answer
            answer = '0.'    
        else:
            # Else append the point to the answer
            answer += '.'
    # To set num count to 1 so that the remaining numbers will append
    num_count = 1
    # Setting equal count to zero so that it won't get reseted 
    equal_count = 0
    # Updating the output label
    update_output()

def oper_but(oper):
    '''
        This function will get the operator and 
        either calculate or append the operator 
        to the history variable and update the 
        history and output
    '''

    # Global declaration to use within the function
    global oper_count, equal_count
    # check if operator count is zero if zero append the operator
    if oper_count == 0:
        # Global declaration to use within the function
        global answer, history, point_count, num_count
        # If zero check that last element is a point
        if answer[-1] == '.':
            # If point remove the point and append operator and store it in history
            history = answer[:-1] + oper
        else:
            # Else add the answer to history and append operator
            history = answer
            history += oper     
        # Setting operator count according to the operator if = then 0 else 1
        oper_count = 0 if oper == '=' else 1
        # Setting equal count to zero so that it won't get reseted
        equal_count = 0
    # Else the operator count is not 0
    else:
        # And if the num count is 1 check for equal 
        if num_count == 1:
            # If equal
            if oper == '=':
                # Set equal count to 1
                equal_count = 1
                # Append the answer to the history
                history += answer
                # Try calculating the answer and append the operator
                try:
                    answer = str(eval(history))
                    history += oper
                # If error set answer to error
                except Exception:
                    answer = 'Error'
                # Call the output at last
                finally:
                    update_output()
                # Set operator count to zero since this is a equal operator
                oper_count = 0
            # For Other operators
            else:
                # Append the answers to the history
                history += answer
                # Calculate the history and append the operator to it
                history = str(eval(history)) + oper
                # Store the answer by removing the operator at the end
                answer = history[:-1]
                # Change the operator count to 1 and equal count to 0
                oper_count = 1
                equal_count = 0
        else:
            # If num count is not zero the set the operator and equal count to 1 and 0
            oper_count = 1
            equal_count = 0
            # update the history with answer and operator
            history = answer + oper
    # Setting num count and operator count to zero so that the new no could be added
    num_count =0
    point_count = 0
    # Updating the lable of history and output
    update_history()
    update_output()

def special_oper_but(oper):
    '''
        This function will check for the 
        special operator and calculate the history 
        and answer and update them in the display
    '''
    # Global declaration to use within the function
    global answer, history, num_count, point_count, equal_count
    if oper == 'Square':
        # If square is the oper then it will cal the square of answer and update in the history
        history = f'squre({answer})'
        answer = str(float(answer)**2)
    elif oper == 'Sqrt':
        # If sqrt is the oper then it will cal the sqrt of answer and update in the history
        history = f'sqrt({answer})'
        answer = str(float(answer)**(0.5))
    elif oper == 'Inverse':
        # If inverse is the oper then it will cal the inverse of answer and update in the history
        history = f'1/({answer})'
        answer = str(float(1/float(answer)))
    # Call the update history and output and reset num count and point count to zero
    update_history()
    update_output()
    num_count = 0
    point_count = 0
    # Set the equal count as 1
    equal_count = 1

def clear_but():
    '''
        This function will clear both history and answer
        and call the update history ans output function
    '''
    # Global declaration to use within the function
    global answer, history, num_count, point_count, oper_count, equal_count
    answer = '0'
    history = '0'
    # Reinitializing counter values to zero
    num_count = 0
    point_count = 0
    oper_count = 0
    equal_count = 0
    update_output()
    update_history()

def clear_equal_but():
    '''
        This function will check for equal 
        if equal is pressed then it will clear all 
        on CE button press else it will clear the answer and call the output
    '''
    if equal_count == 1:
        # Clear all
        clear_but()
    else:
        # Global declaration to use within the function
        global answer, num_count, point_count
        answer = '0'
        num_count = 0
        point_count = 0
        update_output()
        update_history()

def back_but():
    '''
        This function will erase the the value on pressing back button
    '''
    # Global declaration to use within the function
    global answer, num_count, point_count
    # Storing the len of the string
    len_str = len (answer)
    if len_str>1:
        # Checking if len is greater than 1 then remove last element
        answer = answer[:-1]
    else:
        # Else set it to zero
        answer = '0'
        num_count = 0
        point_count = 0
    # update the output at end
    update_output()

def perce_but():
    '''
        This function will calculate percentage
        and update the answer and call the update output function
    '''
    # Global declaration to use within the function
    global answer
    answer = str(float(answer)/100)
    update_output()

def invert_but():
    '''
        This function will invert the sign of 
        the answer and update the output
    '''
    # Global declaration to use within the function
    global answer
    if answer[0] == '-':
        # Checking the answer is negative and remove the negative 
        answer = '' + answer[1:]
    else:
        # Else add the negative sign
        answer = '-' + answer
    update_output()

def update_history():
    '''
        This function will update the history 
        on call with the history value
    '''
    his.set(history)

def update_output():
    '''
        This function will update the output 
        on call with the answer value
    '''   
    val.set(answer[0:11])
    pass

#Buttons constants for reuse
button_relwidth = 0.2375
button_relheight = 0.1541
button_border = 0
button_color = '#CECECE'

#Buttons of row 1 with (%, CE, C, <)
percent = tk.Button(infra, text = '%', bg = button_color, bd = button_border, command = lambda:perce_but())
win.bind('%', lambda event:perce_but())
percent.place(relheight = button_relheight, relwidth = button_relwidth)
ce = tk.Button(infra, text = 'CE', bg = button_color, bd = button_border, command = lambda:clear_equal_but())
win.bind('<Delete>', lambda event:clear_equal_but())
ce.place(relx = 0.25, relheight = button_relheight, relwidth = button_relwidth)
clear = tk.Button(infra, text = 'C', bg = button_color, bd = button_border, command = lambda:clear_but())
clear.place(relx = 0.5, relheight = button_relheight, relwidth = button_relwidth)
bac = tk.Button(infra, text = '<', bg = button_color, bd = button_border, command = lambda:back_but())
win.bind('<BackSpace>', lambda event:back_but())
bac.place(relx = 0.75, relheight = button_relheight, relwidth = 0.25)

#Buttons of row 2 with (1/X, X**2, Sqrt(X), /)
button_rely_r2 = 0.1666
inverse = tk.Button(infra, text = '1/X', bg = button_color, bd = button_border, command = lambda:special_oper_but('Inverse'))
inverse.place(rely = button_rely_r2, relheight = button_relheight, relwidth = button_relwidth)
pow = tk.Button(infra,text='X**2',bg=button_color, bd=button_border, command = lambda :special_oper_but('Square'))
pow.place(rely = button_rely_r2, relx = 0.25, relheight = button_relheight, relwidth = button_relwidth)
root = tk.Button(infra, text = 'Sqrt(X)', bg = button_color, bd = button_border, command = lambda:special_oper_but('Sqrt'))
root.place(rely = button_rely_r2, relx = 0.5, relheight = button_relheight, relwidth = button_relwidth)
division = tk.Button(infra, text = '/', bg = button_color, bd = button_border, command = lambda:oper_but('/'))
win.bind('/', lambda event:oper_but('/'))
division.place(rely = button_rely_r2, relx = 0.75, relheight = button_relheight, relwidth = 0.25)

#Button of row 3 with (7, 8, 9, *)
button_rely_r3 = 0.3332
seven = tk.Button(infra, text = '7', bg = 'white', bd = button_border, command = lambda:num_but('7'))
win.bind(str('7'), lambda event:num_but('7'))
seven.place(rely=button_rely_r3, relheight=button_relheight,relwidth=button_relwidth)
eight = tk.Button(infra, text = '8', bg = 'white', bd = button_border, command=lambda:num_but('8'))
win.bind(str('8'), lambda event:num_but('8'))
eight.place(rely = button_rely_r3, relx = 0.25, relheight = button_relheight, relwidth = button_relwidth)
nine = tk.Button(infra, text = '9', bg = 'white', bd = button_border, command = lambda:num_but('9'))
win.bind(str('9'), lambda event:num_but('9'))
nine.place(rely = button_rely_r3, relx = 0.5,relheight = button_relheight, relwidth = button_relwidth)
mul = tk.Button(infra, text = '*', bg = button_color, bd = button_border, command = lambda:oper_but('*'))
win.bind('*', lambda event:oper_but('*'))
mul.place(rely = button_rely_r3, relx = 0.75, relheight = button_relheight, relwidth = 0.25)

#Button of row 4 with (4, 5, 6, -)
button_rely_r4 = 0.4998
four = tk.Button(infra, text = '4', bg = 'white', bd = button_border, command = lambda:num_but('4'))
win.bind(str('4'), lambda event:num_but('4'))
four.place(rely = button_rely_r4, relheight = button_relheight, relwidth = button_relwidth)
five = tk.Button(infra, text = '5', bg = 'white', bd = button_border, command = lambda:num_but('5'))
win.bind(str('5'), lambda event:num_but('5'))
five.place(rely = button_rely_r4, relx = 0.25, relheight = button_relheight, relwidth = button_relwidth)
six = tk.Button(infra,text='6',bg='white', bd=button_border, command = lambda:num_but('6'))
win.bind(str('6'), lambda event:num_but('6'))
six.place(rely = button_rely_r4, relx = 0.5, relheight = button_relheight, relwidth = button_relwidth)
sub = tk.Button(infra, text = '-', bg = button_color, bd = button_border, command = lambda:oper_but('-'))
win.bind('-', lambda event:oper_but('-'))
sub.place(rely = button_rely_r4, relx = 0.75, relheight = button_relheight, relwidth = 0.25)

#Button of row 5 with (1, 2, 3, +)
button_rely_r5 = 0.6664
one = tk.Button(infra, text = '1', bg = 'white', bd = button_border, command = lambda:num_but('1'))
win.bind(str('1'), lambda event:num_but('1'))
one.place(rely = button_rely_r5, relheight = button_relheight, relwidth = button_relwidth)
two = tk.Button(infra, text = '2',bg = 'white', bd = button_border, command = lambda:num_but('2'))
win.bind(str('2'), lambda event:num_but('2'))
two.place(rely = button_rely_r5, relx = 0.25, relheight = button_relheight, relwidth = button_relwidth)
three = tk.Button(infra, text = '3', bg = 'white', bd = button_border, command = lambda:num_but('3'))
win.bind(str('3'), lambda event:num_but('3'))
three.place(rely = button_rely_r5, relx = 0.5, relheight = button_relheight, relwidth = button_relwidth)
add = tk.Button(infra, text = '+', bg = button_color, bd = button_border, command = lambda:oper_but('+'))
win.bind('+', lambda event:oper_but('+'))
add.place(rely = button_rely_r5, relx = 0.75, relheight = button_relheight, relwidth = 0.25)

#Button of row 6 with (+/-, 0, ., =)
button_rely_r6 = 0.833
sign = tk.Button(infra, text = '+/-', bg = 'white', bd = button_border, command = lambda:invert_but())
sign.place(rely = button_rely_r6, relheight = 0.166, relwidth = button_relwidth)
zero = tk.Button(infra, text = '0', bg = 'white', bd = button_border, command = lambda:num_but('0'))
win.bind(str('0'), lambda event:num_but('0'))
zero.place(rely = button_rely_r6, relx = 0.25, relheight = 0.166, relwidth = button_relwidth)
point = tk.Button(infra, text = '.', bg = 'white', bd = button_border, command = lambda:point_but())
point.place(rely = button_rely_r6, relx = 0.5, relheight = 0.166, relwidth = button_relwidth)
equal = tk.Button(infra, text = '=', bg = 'lightblue', bd = button_border, command = lambda:oper_but('='))
win.bind('=', lambda event:oper_but('='))
win.bind('<Return>', lambda event:oper_but('='))
equal.place(rely = button_rely_r6, relx = 0.75, relheight = 0.166, relwidth = 0.25)

# Main loop function to run continously
win.mainloop()