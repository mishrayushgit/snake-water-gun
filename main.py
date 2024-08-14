import random
print("\n WELCOME TO THE SNAKE WATER GUN GAME \n")
print("Enter your choice : ")
yourChoice = (input())
computerChoice = random.choice([1, 2, 3])
yourDict = {
    "s" : 1,
    "w" : 2,
    "g" : 3
}
swgDict ={
    1 :"snake",
    2 :"water",
    3 :"gun"  
}
if(yourChoice != "s" and yourChoice != "w" and yourChoice != "g"):
    print("!WRONG INPUT! \n pls try again ")


print(f"you chose {swgDict[yourDict[yourChoice]]} and the computer chose {swgDict[computerChoice]}")

if(computerChoice == yourChoice):
    print("its a draw")
else:
    if(yourDict[yourChoice] == 1 and computerChoice ==2):
        print("you win")
    if(yourDict[yourChoice] == 1 and computerChoice ==3):
        print("you lose")
    if(yourDict[yourChoice] == 2 and computerChoice ==1):
        print("you lose")
    if(yourDict[yourChoice] == 2 and computerChoice ==3):
        print("you win")
    if(yourDict[yourChoice] == 3 and computerChoice ==1):
        print("you win")
    if(yourDict[yourChoice] == 3 and computerChoice ==2):
        print("you lose")