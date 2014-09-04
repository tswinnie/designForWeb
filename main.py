'''

Tyrone Swinnie
Design for Web Standards
Madlib Assignment
9/4/14
'''

# I will go ahead now and make the var for the user to input their name

usr_Name = raw_input('Enter Your First Name, then press enter.')

if usr_Name != '':
   # I am going to use a dictionary to store the name of the user

    dict = {'name': ''}
    dict['name'] = usr_Name

print dict['name']



# i will create variables that will hold that data from user


adj1 = raw_input('Tell me an adjective, then press enter')
num1 = raw_input('Give me a number between 1 and 10 and press enter.')
noun1 = raw_input('Tell me an noun, then press enter')
num2 = raw_input('Give me a number between 1 and 8 and press enter.')
ver1 = raw_input('Tell me an verb, then press enter')
num3 = raw_input('Give me a number between 1 and 5 and press enter.')



'''
Now I need to store the variables that have
the data from the user. I will use an array

'''
myArray = [adj1, num1, noun1, num2, ver1, num3]

#added newly created name from user to my array
myArray.append(dict['name'])

print myArray