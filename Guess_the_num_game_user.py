print("welcome to the guess the number game!")
print("welcome of a number in your mind, and i will try to guess it.")

#step 1: ask for range
low = int(input("enter the starting number of the range:"))
high = int(input("enter the ending number of the range:"))

print(f"okay, i will guess a number between {low} and {high}. let s begin!")

# step 2: initialize variable
attemps = 0
feedback = ""

#step 3: start guessing loop
while feedback != "c":
    #step 4: computer guesses
    guess = (low + high) // 2
    attemps += 1

    print(f"my guess is: {guess}")
    feedback = input("is my guess too (h)igh, too (l)ow, or (c)orrect?").lower()

    #step 5: adjust range based on feedback
    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1
    elif feedback == "c":
        print(f"yay! i guessed your number in (attempts) attempts.")
    else:
        print("please enter valid feedback: 'h', 'l', or 'c',")         
