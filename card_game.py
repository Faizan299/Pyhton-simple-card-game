print("---- Card Game ----")
print("\n")
player1=input("Enter your Player1 card")
p1=input("Double your card?")
player2=input("Enter your Player2 card")
p2=input("Double your card?")
player3=input("Enter your Player3 card")
p3=input("Double your card?")
player4=input("Enter your Player4 card")
p4=input("Double your card?")

if player1 == 'A':
    point=40
    if p1 == "yes":
        p1point=point*2
        print("Player1 is win the game And Your Point is :",p1point)
    else:
        p1point=point
    
ppoint=30
if player2 == 'J':
    if p2 == "yes":
        p2point=ppoint*2
        print("Player2 is win the game And Your Point is :",p2point)
    
    else:
        p2point=ppoint

pppoint=20
if player3 == 'K':
    if p3 == "yes":
        p3point=pppoint*2
        print("Player3 is win the game And Your Point is :",p3point)
    
    else:
        p3point=pppoint
        
ppppoint=10
if player4 == 'Q':
    if p4 == "yes":
        p4point=ppppoint*2
        print("Player4 is win the game And Your Point is :",p4point)
    else:
        p4point=ppppoint
    

else:
    print("Invalid Card")



    
    
