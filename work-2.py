import random
secret_number = random.randint(1, 20)
print("Guess my number between 1 and 20. You have 5 tries!")
for attempt in range(5):
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("🎉 Correct! You win!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"❌ Game over! The number was {secret_number}")
