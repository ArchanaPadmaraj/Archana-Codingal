def quiz():
    score = 0
    answer1 = input("Who was the first person to walk on the moon?")
    if answer1.lower() == "neil armstrong":
        print("You have guessed correct!")
    else:
        print("Uh oh! you got it wrong!")
    answer2 = input("What gas do plants absorb from the atmosphere for photosynthesis?")
    if answer2.lower() == "carbon dioxide":
        print("You have guessed correct!")
        score +=1
    else:
        print("Uh oh! you got it wrong!")
    answer3 = input("Which country is famous for inventing pizza?")
    if answer3.lower() == "italy":
        print("You have guessed correct!")
        score +=1
    else:
        print("Uh oh! you got it wrong!")
    print(f"\nYou got {score} out of 3 correct!")

quiz()
