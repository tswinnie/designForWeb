'''

Tyrone Swinnie
Design for Web Standards
Madlib Assignment
9/4/14
'''

# I will go ahead now and make the var for the user to input their name

usr_Name = raw_input('Enter Your First Name, then press enter. ')

if usr_Name != '':
   # I am going to use a dictionary to store the name of the user

    dict = {'name': ''}
    dict['name'] = usr_Name
else:
    print "Please Enter Your Name "

new_name = dict['name']
# Now I'm going to collect the user's age so that I can make sure they are human and not spam

born = raw_input("Please enter the year you were born, then press enter ")

# do the same thing but I want to collect the current year

current = raw_input("Please enter the current year, then press enter ")


#the thing I want to do is create a function that will except 2 parameters
#and it will check the age to see if they are a human or a robot, so we can block spam

def check(current_year, birth_year):
    alive = int(current_year) - int(birth_year)

    #now I am going to check to see if the age they entered is the correct age, which is older than 0
    if int(alive) >= 1:
        return int(alive)
    else:
        print"You are not old enough yet"
        exit()


check(current, born)




# i will create variables that will hold that data from user


adj1 = raw_input('Tell me an adjective, then press enter ')
num1 = raw_input('Give me a number between 1 and 10 and press enter. ')
noun1 = raw_input('Tell me an noun, then press enter ')
num2 = raw_input('Give me a number between 1 and 8 and press enter. ')
ver1 = raw_input('Tell me an verb, then press enter ')
num3 = raw_input('Give me a number between 1 and 5 and press enter. ')



'''
Now I need to store the variables that have
the data from the user. I will use an array

'''
myArray = [adj1, num1, noun1, num2, ver1, num3]

#added newly created name from user to my array
myArray.append(new_name)
myArray.append(born)





#the next thing I want to do is loop through the array and check to see if their are the correct number of items

for number_items in myArray:

    if number_items >= 5:
        break
    else:
        print"Something went wrong"
        exit()

# for the final part I am going to include the data collected from the user and insert it into my madlib

message = '''
My name is {new_name}. I was born on {born} and i'm feeling {adj1}.
I just relieved myself {num1} times on your yard. I don't like your {noun1}
and I don't sleep {num2} hours a night, but if you don't quite your dog, me
and you will {ver1}, {num3} times each night.



'''

message = message.format(**locals())

print message











