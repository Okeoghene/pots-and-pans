import random

values = [0,1,2,3,4,5,6,7,8,9]

computer_user = random.sample(values, k=4) #The computer values

attempt = 0 #The number of times the user has tried to solve the game

while True:
    pot = 0
    pan = 0
    user_input = int(input('Please enter four unique numbers: \n '))
    user_list = []
    while user_input > 0:
        user_list.append(user_input % 10)
        user_input = (user_input - user_input % 10) // 10
        
    #validate user_input.
    if len(user_list) == 4:
        users_input = True
    else:
        print('Wrong entry: Please 4 unique digits')
    user_list.reverse()

    #POT logic
    for x,y in zip(user_list,computer_user):
        if x == y:
            pot += 1

    #PAN logic
    if len(user_list) == len(computer_user):
        for i in range(len(user_list)):
            if user_list[i] != computer_user[i]:
                if user_list[i] in computer_user:
                    pan += 1
    

    if pot == 4:        #GAME ENDS WHEN
        print('YOU WIN!')
        break
    else:               #GAME CONTINUES WHEN
        attempt += 1
        sentence = f"The number of attempts so far {attempt} \n The number of pan {pan} \n The number of pot {pot}"
        print(sentence)


print(computer_user)
print(user_list)