import random
while True:
    lower=1
    upper=100
    secret=random.randint(lower,upper)
    n=int(input("HOW MANY CHANCE U WANT: "))
    for i in range(n):
        num=int(input("ENTER THE NUMBER U THINK IT WILL (1-100): "))
        if num==secret:
              print("YAYAYAYA!!!! GOTCHA U GOT IT")
              break;
        elif num>secret:
              print("TOO HIGH")
              continue;
        elif n<secret:
              print("TOO LOW")
              continue;
        else:
            break;

        try:
           if num>upper or num<lower:
                print("ENTER THE NUMBER BETWEEN 1-100 ONLY")
                continue
        except:
               print(" ENTER DIGIT ONLY: ")
  
    ask=input("DO YOU WANT TO CONTINUE (YES/yes/y/Y): ")
    if ask not in ('YES','yes','y','Y'):
        break;
print("THANKYOU FOR PLAYING")
