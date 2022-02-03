import random
list_of_island_treasures = ['slab of chocolate', 'sailor map', 'sea conch', 'sea shell', 'packed dried meat', 'sun dial']

list_of_rare_island_treasures = ['baby dragon', 'Golderoy Atlas', 'large gold bar', 'golden chest', 'secret treasure map', 'dragon egg', 'pirate ship']

number_of_treasures = random.randint(1, 12)

natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #to be used in generating random numbers of treasures, up to 12, for Johnnie(Computer)

Johnnie_number_of_treasures = random.choice(natural_numbers)

price_of_treasures = [0.25, 1.87, 0.15, 0.09, 2.03, 0.83 ]

random_words = ['dug up', 'found', 'unearthed', 'discovered'] #to be used to avoid monotony in verbs to make it look as if the system is learned

random_phrases = random.choice(random_words)

Johnnie_random_phrases = random.choice(random_words)

userReply = ['yeah', 'yep', 'yes', 'yaddah', 'yup', 'oui'] #list of possible user replies when asked if they want to play the game

userScore = 0

computer_Score = 0

looper = 0 #Used to loop the game

print('This an adventure game. Do you wanna play?\n\t')

userInput = input().lower()

if userInput in userReply:
    print('You are shipwrecked with grumbly old Johnnie in a mysterious treasure island in the North Balkan Seas.\n\nThe two of you are on the hunt for the many treasures here\nWho will loot the most riches, you or old Johnnie?')
    while looper >= 0:
        print('\nChoose a magic number between 0 and 6 to dig for treasures!\n\t')
        userChoice = input()
        if userChoice.isdigit() and int(userChoice) <= 6:
            inputConverter = int(userChoice)
            generated_treasure = random.choice(list_of_island_treasures)
            if number_of_treasures > 1:
                print('You just', random_phrases, number_of_treasures, generated_treasure + 's!')
            else:
                print('You just', random_phrases, number_of_treasures, generated_treasure + '!')

            worth_of_treasure = number_of_treasures * price_of_treasures[list_of_island_treasures.index(generated_treasure)]
            print('The treasure you discovered is worth $' + str(worth_of_treasure))
            userScore += worth_of_treasure
#This is where Old Johnnie's wheel will be spinned, below:
            print('\nOld Johnnie is spinning...')
            Johnnie_treasure = random.choice(list_of_island_treasures)
            if Johnnie_number_of_treasures > 1:
                print('\nOld Johnnie just', random_phrases, Johnnie_number_of_treasures, Johnnie_treasure + 's!')
            else:
                print('\nOld Johnnie just', random_phrases, Johnnie_number_of_treasures, Johnnie_treasure + '!')
#Calculates the worth of Johnnie's treasures:
            Johnnie_worth_of_treasure = Johnnie_number_of_treasures * price_of_treasures[list_of_island_treasures.index(Johnnie_treasure)]
            print('The treasure old Johnnie just discovered is worth $' + str(Johnnie_worth_of_treasure))
            computer_Score += Johnnie_worth_of_treasure
            if userScore > computer_Score:
                print('\nLooks like you are leading!')
            else:
                print('\nOld Johnnie is leading. Giddy up!')

        elif userChoice.isalpha() and (userChoice.lower() == 'q' or userChoice.lower() == 'stop' or userChoice.lower() == 'quit' or userChoice.lower() == 'end'):
            print('You quitted the game...')
            print('\nThe total treasures you discovered is worth $' + str(userScore) + '\nOld Johnnie treasures are worth $' + str(computer_Score))
            if userScore > computer_Score:
                print('\nCongratulations! You won!')
            else:
                print('\nOld Johnnie won!')
            quit()

        else:
            print('Enter a valid input...')
        looper += 1
        Johnnie_number_of_treasures = random.choice(natural_numbers)
        number_of_treasures = random.randint(1, 12)
        random_phrases = random.choice(random_words)
        Johnnie_random_phrases = random.choice(random_words)
    print('Your total treasure discovered is worth $' + str(userScore) + '\nOld Johnnie treasures are worth $' + str(computer_Score))
    if userScore > computer_Score:
        print('\nCongratulations! You won!')
    else:
        print('\nOld Johnnie won!')
else:
    print('Ok. You do not want to have some fun in this mysterious island')
    quit()