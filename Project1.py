# Guessing Number & Win Game..

winning_number=49
count=0
while True:
    count+=1
    guessed_number=input("Guess any two digit number :- ")
    guessed_number=int(guessed_number)
    if winning_number==guessed_number:
        print("congrets! you win this match.")
        print("\U0001F602 \U0001F602 \U0001F603 \U0001F601 \U0001F602") 
        break

    else:    
        if guessed_number<winning_number:
            print("sorry!, your guessed number is smaller then winning number.")
            print(f"Hint: Please..! choose some greater number then {guessed_number}.")
            print("Try again...!")
            print("\U0001F644 \U0001F620")
        else:  
            print("sorry!, your guessed number is greater then winning number.") 
            print(f'Hint: Please..! Choose smaller number then {guessed_number}.')
            print("Try again...!")
            print("\U0001F644 \U0001F620")

print(f'After {count} number of rounds you win the match..')
