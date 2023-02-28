import random
#banner
print('''
-------------------------------------------------------------------------------------
   ______                        __  ___         _   __                __             
  / ____/_  _____  __________   /  |/  /_  __   / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / /|_/ / / / /  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /  / / /_/ /  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/  /_/  /_/\__, /  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/
                                    /____/   🎯👑  匚𝐨∂𝐄 𝓑у ᗪ𝔸гЌ Ď𝑒𝐕Ɨ𝓁  💚✊
                                            
------------------------------------------------------------------------------------''','\n\n\n')
#range [start]-[end]
start = int(input("Enter Lower bound:- "))
end   = int(input("Enter upper bound:- "))
print('\n')

#random number
random_=random.randint(start,end)

#timer
timer=0

#run
for i in range(start,end+1):
    print('Guess ►►►► {start} - {end}'.format(start=start,end=end))
    #user_input
    user=int(input('Enter a your Guess number = '))
    timer=timer+1
    if random_==user:
        print('-> well Done! It took you {timer},attempts to guess this number ☺'.format(timer=timer))
        break
    else:
        if random_<user:
            print('-> My number is less than this number','\n')
        else:
            print('-> My number is greater than this number','\n')
