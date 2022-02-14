# introduction
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

# user's name
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

# guessing the age of an user through a game
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

# counting up
def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

# short quiz
def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("What was 'Python' named after?")
    print("""
    1. Snake
    2. Monty Python 
    3. Song
    4. Because why not? 
     """)
    answer = int(input())
    while answer != 2:
        print("Please, try again.")
        answer = int(input())
    print('Completed, have a nice day!')

    
def end():
    print('Congratulations, have a nice day!')


greet('Omega', '2022')  
remind_name()
guess_age()
count()
test()
end()
