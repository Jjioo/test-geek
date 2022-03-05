import random
liste = list()
def user_guess(x):
    random_guess =random.randint(1,x)
    guess = 0
    while guess != random_guess :
        guess = int(input("enter number :"))
        if guess < random_guess:
            print("try up")
        elif guess > random_guess:
                print("try down")
    print(f"congrat you have guessed the number {guess}")


def computer_guess(x):
    global random_guess
    low= 1
    high =x
    feedback= ''
    while feedback != 'c'  :
            if(low !=high):
                random_guess = random.randint(low, high)
                liste.append(random_guess)
                remove_duplicate(liste)
            else:
                random_guess=low
            feedback= str(input(f"is ({random_guess}) to High(H) or to Low(L) or Correct (C) --->").lower())
            if feedback =='h' :
                h=high
                high=random_guess -1
                while high> h :
                    high = random_guess - 1
                    liste.append(high)
                    remove_duplicate(liste)
                    if high in liste:
                        exit(0)

            elif feedback == 'l' :
                l=low
                low = random_guess + 1
                while low<l:
                    low = random_guess + 1
                    liste.append(low)
                    remove_duplicate(liste)
                    if high in liste:
                        exit(0)


            if ((random_guess == x and feedback =='l') or (random_guess == 1 and feedback == 'h')):
                print("You are a liar I got you HAHAHA\nDon't be a cheater ")
                exit(0)
            elif(high or low)  in liste and feedback!='c':
                    print("You are a liar I got you HAHAHA\nDon't be a cheater ")
                    exit()
            elif (random_guess==1) and feedback!='c':
                print("You are a liar I got you HAHAHA\nDon't be a cheater ")
                exit()

    liste.append(random_guess)
    y=remove_duplicate(liste)
    print("yaaaay congrat")
    print(y)

def remove_duplicate(duplist):
    new_List = []
    for e in duplist:
        if e not in new_List:
            new_List.append(e)
    return new_List


#user_guess(100)
computer_guess(100)

#I am just a beginner and I tried to develop your mini project(GUESS THE NUMBER "USER" -- 13:15/3:00:29)
