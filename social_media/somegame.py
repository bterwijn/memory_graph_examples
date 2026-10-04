from random import *
from math import *
from time import *

God_Has_No_Need=[0,1]
God_Has_Need=choice(God_Has_No_Need)
High_IQ=[0,1,2,3]
Num_Props=[]
UBound=[]
LBound=[]
Factors=[]
Square=[]
Set=[]
GuessB=[50,100]
def Square(a):
  r=[]
  for i in range(1,int(a**0.5)+1):
    r.append(i**2)
  return r
def Even(a):
  r=[]
  for i in range(2,a,2):
    r.append(i)
  return r
def Random(a):
  b=randint(1,a)
  return b
def PrimeList(a):
  primes=[]
  r=[True]*a
  r[0]=r[1]=False
  for i in range(4, a, 2):
    r[i]=False
  for i in range(3, int((a**0.5)+1), 2):
    if r[i]:
      for j in range(i*i, a, 2*i):
        r[j]=False
  for i in range(len(r)):
    if r[i] == True:
      primes.append(i)
  return primes
while True:
  print("1. Guess my number")
  print("2. I guess your number")
  print("")
  print("1 or 2?")
  print("")
  determine=int(input())
  print("Game starting...", end="")
  sleep(0.75)
  print("Game initialized")
  print("")
  if determine == 2:
    init_range=101
    print("Is a range of 1 to 100 okay(yes/no)?")
    range_okay=input()
    if range_okay == "yes":
      print("Optimized or interesting method?")
      method_determine=input()
      guess=50
      tries=1
      if method_determine == "optimized":
        while True:
          print(f"Is your number >= {guess}, <= {guess}, or = {guess}")
          sign=input()
          diff=round(0.5*(abs(GuessB[0]-GuessB[1])))
          if sign == ">=":
            guess=guess+diff
            if GuessB[0]<GuessB[1]:
              del GuessB[0]
              GuessB.append(guess)
            else:
              del GuessB[1]
              GuessB.append(guess)
          if sign == "<=":
            guess=guess-diff
            if GuessB[0]>GuessB[1]:
              del GuessB[0]
              GuessB.append(guess)
            else:
              del GuessB[1]
              GuessB.append(guess)
          if sign == "=":
            if tries == 1:
              print(f"Your number is {guess}, I took {tries} try to guess it, which is albeit unimpressive as a computer :P")
            else:
              print(f"Your number is {guess}, I took {tries} tries to guess it, which should be about {log2(100)}")
            print("Good game fool. I have won, and you are my pawn. You are but a cog in my machine, a loop in my algorithm -\\_('_')_/-")
            break
          tries+=1
      elif method_determine == "interesting":
        print("Is your number <= 50(yes/no)?")
        The_Parting_Of_The_Red_Sea=input()
        if The_Parting_Of_The_Red_Sea == "yes":
          Set.append("less50/eq50")
        else:
          Set.append("more50")
        print("Is your number prime(yes/no)")
        All_Alone=input()
        if All_Alone == "yes":
          Set.append("prime")
        else:
          Set.append("composite")
        print("Is your number even(yes/no)?")
        OddBall=input()
        if OddBall=="yes":
          Set.append("even")
        else:
          Set.append("odd")
        if "prime" in Set and "even" in Set:
          print("Your number is 2")
        if "composite" in Set:
          print("Is your number square(yes/no)?")
          Triangle=input()
          if Triangle == "yes":
            Set.append("square")
          else:
            Set.append("not square")
        if "square" in Set:
          if "less50/eq50" in Set:
            if "even" in Set:
              print("Is your number's last digit 6(yes/no)?")
              Demon_Number=input()
              if Demon_Number == "yes":
                print("Is your number less than 26(yes/no)?")
                Arithmetic_Mean=input()
                if Arithmetic_Mean == "yes":
                  print("Your number is 16")
                else:
                  print("Your number is 36")
              else:
                print("Your number is 4")
            else:
              print("Is your number's last digit 9(yes/no)?")
              Holy_Number=input()
              if Holy_Number == "yes":
                print("Is your number less than 29(yes/no)?")
                The_Great_Divide=input()
                if The_Great_Divide == "yes":
                  print("Your number is 9")
                else:
                  print("Your number is 49")
              else:
                print("Meme or real question?")
                A_True_Consideration=input()
                if A_True_Consideration == "meme":
                  print("Is your number Legendre's constant(yes/no)?")
                  Multiplicative_Identity=input()
                  if Multiplicative_Identity == "yes":
                    print("Your number is 1, or Legendre's constant")
                  else:
                    print("Your number is 25")
                else:
                  print("Is your number less than 13(yes/no)?")
                  Trivial_Matter=input()
                  if Trivial_Matter == "yes":
                    print("Your number is 1")
                  else:
                    print("Your number is 25")
          else:
            print("Is your number's last digit 4(yes/no)?")
            Read_This=input()
            if Read_This == "yes":
              print("Your number is 64")
            else:
              print("Is your number's last digit 1(yes/no)?")
              Binary=input()
              if Binary == "yes":
                print("Your number is 81")
              else:
                print("Your number is 100")
        if "prime" in Set:
          if "less50/eq50" in Set:
            print("Is your number less than 21(yes/no)?")
            Boy_You_Stupid=input()
            if Boy_You_Stupid == "yes":
              print("Is your number less than 10(yes/no)?")
              Based_Out=input()
              if Based_Out == "yes":
                print("Is your number a difference of 2 from 5, 2 away from 5(yes/no)?")
                Twin=input()
                if Twin == "yes":
                  print("Is the sign of difference positive, addition(yes/no)?")
                  Excluded_Middle=input()
                  if Excluded_Middle == "yes":
                    print("Your number is 7")
                  else:
                    print("Your number is 3")
                else:
                  print("Your number is 5")
              else:
                print("Is your number's last digit a square number(yes/no)?")
                Weird_But_Okay=input()
                if Weird_But_Okay == "yes":
                  print("Is your number less than 15(yes/no)?")
                  Makes_Sense=input()
                  if Makes_Sense == "yes":
                    print("Your number is 11")
                  else:
                    print("Your number is 19")
                else:
                  print("Is your number less than 15(yes/no)")
                  Still_Weird_That_It_Happened_Twice=input()
                  if Still_Weird_That_It_Happened_Twice == "yes":
                    print("Your number is 13")
                  else:
                    print("Your number is 17")
            else:
              print("Is your number less than 39(yes/no)?")
              No_Pun_Yet=input()
              if No_Pun_Yet == "yes":
                print("Is your number's last digit a square number(yes/no)?")
                Really_Weird_It_Happened_Twice=input()
                if Kinda_Weird_It_Happened_Twice == "yes":
                  print("Is your number less than 30(yes/no)?")
                  Huh=input()
                  if Huh == "yes":
                    print("Your number is 29")
                  else:
                    print("Your number is 31")
                else:
                  print("Is your number less than 30(yes/no)?")
                  Really_Weird_Its_Happening_Twice=input()
                  if Really_Weird_Its_Happening_Twice == "yes":
                    print("Your number is 23")
                  else:
                    print("Your number is 37")
              else:
                print("Is your number's last digit less than 2(yes/no)?")
                Even_Steven=input()
                if Even_Steven == "yes":
                  print("Your number is 41")
                else:
                  print("Is your number less than 45(yes/no)?")
                  Like_The_Triangle=input()
                  if Like_The_Triangle == "yes":
                    print("Your number is 43")
                  else:
                    print("Your number is 47")
          else:
            print("Is your number less than 72(yes/no)?")
            Still_No_Pun=input()
            if Still_No_Pun == "yes":
              print("Is your number's last digit prime(yes/no)?")
              Primer=input()
              if Primer == "yes":
                print("Is your number less than 60(yes/no)?")
                Thats_Odd=input()
                if Thats_Odd == "yes":
                  print("Your number is 53")
                else:
                  print("Your number is 67")
              else:
                print("Is your number less than 66(yes/no)?")
                The_Devil_Lurks=input()
                if The_Devil_lurks == "yes":
                  print("Is your number less than 60(yes/no)?")
                  Not_Again=input()
                  if Not_Again == "yes":
                    print("Your number is 59")
                  else:
                    print("Your number is 61")
                else:
                  print("Your number is 71")
            else:
              print("Is the last digit of your number prime(yes/no)?")
              Why_Again=input()
              if Why_Again == "yes":
                print("Is your number less than 90(yes/no)?")
                So_Close=input()
                if So_Close == "yes":
                  print("Is your number less than 88(yes/no)?")
                  Double_Digit=input()
                  if Double_Digit == "yes":
                    print("Your number is 73")
                  else:
                    print("Your number is 83")
                else:
                  print("Your number is 97")
              else:
                print("Is your number less than 84")
                Last_Prime_Test=input()
                if Last_Prime_Test == "yes":
                  print("Your number is 79")
                else:
                  print("Your number is 89")
        if "even" in Set and "prime" not in Set and "square" not in Set:
          if "less50/eq50" in Set:
            print("Is your number divisible by 6(yes/no)?")
            Sixer=input()
            if Sixer == "yes":
              print("Is your number less than 27(yes/no)?")
              RP1=input()
              if RP1 == "yes":
                print("Is your number less than 15(yes/no)?")
                RP2=input()
                if RP2 == "yes":
                  print("Is your number less than 9(yes/no)?")
                  What=input()
                  if What == "yes":
                    print("Your number is 6")
                  else:
                    print("Your number is 12")
                else:
                  print("Is your number less than 21(yes/no)?")
                  Drinking_Age=input()
                  if Drinking_Age == "Yes":
                    print("Your number is 18")
                  else:
                    print("Your number is 24")
              else:
                print("Is your number less than 39(yes/no)?")
                Blank_Variable=input()
                if Blank_Variable == "yes":
                  print("Is your number less than 33(yes/no)?")
                  IOI=input()
                  if IOI == "yes":
                    print("Your number is 30")
                  else:
                    print("Your number is 36")
                else:
                  print("Is your number less than 45(yes/no)?")
                  Ninety_90_45=input()
                  if Ninety_45_45 == "yes":
                    print("Your number is 42")
                  else:
                    print("Your number is 48")
            else:
              print("Is the greatest prime divisor of your number less than 12(yes/no)?")
              Miller_Rabin=input()
              if Miller_Rabin == "yes":
                print("Is the greatest prime divisor of your number less than 6(yes/no)?")
                AKS=input()
                if AKS == "yes":
                  print("Is the greatest prime divisor of your number less than 3(yes/no)?")
                  E_Sieve=input()
                  if E_Sieve == "yes":
                    print("Is your number less than 20(yes/no)?")
                    Mean_Means=input()
                    if Mean_Means == "yes":
                      print("Your number is 8")
                    else:
                      print("Your number is 32")
                  else:
                    print("Is your number less than 30(yes/no)?")
                    Thirty_60_90=input()
                    if Thirty_60_90 == "yes":
                      print("Is your number less than 15")
                      Probably_Legal=input
                      if Probably_Legal == "yes":
                        print("Your number is 10")
                      else:
                        print("Your number is 20")
                    else:
                      print("Is your number less than 45(yes/no)?")
                      FortyFive_45_90=input()
                      if FortyFive_45_90 == "yes":
                        print("Your number is 40")
                      else:
                        print("Your number is 50")
                else:
                  print("Is the greatest prime divisor of your number less than 9(yes/no)?")
                  Squarey=input()
                  if Squarey == "yes":
                    print("Is your number less than 21(yes/no)?")
                    Leads_To_Sheldon_Number=input()
                    if Leads_To_Sheldon_Number == "yes":
                      print("Your number is 14")
                    else:
                      print("Your number is 28")
                  else:
                    print("Is your number less than 33(yes/no)?")
                    Looks_Cool=input()
                    if Looks_Cool == "yes":
                      print("Your number is 22")
                    else:
                      print("Your number is 44")
              else:
                print("Is the greatest prime divisor of your number less than 18(yes/no)?")
                Legal_Age=input()
                if Legal_Age == "yes":
                  print("Is the greatest prime divisor of your number less than 15")
                  Variable=input()
                  if Variable == "yes":
                    print("Your number is 26")
                  else:
                    print("Your number is 34")
                else:
                  print("Is the greatest prime divisor of your number less than 21(yes/no)?")
                  You_Can_Drink=input()
                  if You_Can_Drink == "yes":
                    print("Your number is 38")
                  else:
                    print("Your number is 46")
          else:
            print("Is the greatest prime divisor of your number less than 21(yes/no)?")
            Twelve_Backwards=input()
            if Twelve_Backwards == "yes":
              print("Is the greatest prime divisor of your number less than 12(yes/no)?")
              Twenty_One_Backwards=input()
              if Twenty_One_Backwards == "yes":
                print("Is the greatest prime divisor of your number less than 6(yes/no)?")
                Binary_Variable=input()
                if Binary_Variable == "yes":
                  print("Is the greatest prime divisor of your number less than 4(yes/no)?")
                  So_Many_Questions=input()
                  if So_Many_Questions == "yes":
                    print("Is your number less than 84(yes/no)?")
                    Above_Average=input()
                    if Above_Average == "yes":
                      print("Is your number less than 63(yes/no)?")
                      Kinda_Old=input()
                      if Kinda_Old == "yes":
                        print("Your number is 54")
                      else:
                        print("Your number is 72")
                    else:
                      print("Your number is 96")
                  else:
                    print("Is your number less than 85(yes/no)?")
                    Very_Old=input()
                    if Very_Old == "yes":
                      print("Is your number less than 75(yes/no)?")
                      Perfectly_Balanced=input()
                      if Perfectly_Balanced == "yes":
                        print("Your number is 60")
                      else:
                        print("Your number is 70")
                    else:
                      print("Your number is 90")
                else:
                  print("Is the greatest prime divisor of your number less than 9(yes/no)?")
                  In_Between=input()
                  if In_Between == "yes":
                    print("Is your number less than 77(yes/no)?")
                    Doubly_Digits=input()
                    if Doubly_Digits == "yes":
                      print("Is your number less than 63(yes/no)?")
                      Arbitrary_Property=input()
                      if Arbitrary_Property == "yes":
                        print("Your number is 56")
                      else:
                        print("Your number is 70")
                    else:
                      print("Is your number less than 91(yes/no)?")
                      Not_Yet_Ancient=input()
                      if Not_Yet_Ancient == "yes":
                        print("Your number is 84")
                      else:
                        print("Your number is 98")
                  else:
                    print("Is your number less than 77(yes/no)?")
                    Almost_Nice=input()
                    if Almost_Nice == "yes":
                      print("Your number is 66")
                    else:
                      print("Your number is 88")
              else:
                print("Is the greatest prime divisor of your number less than 15(yes/no)?")
                Everything_Circles_Back=input()
                if Everything_Circles_Back == "yes":
                  print("Is your number less than 65(yes/no)?")
                  Ouroboros=input()
                  if Ouroboros == "yes":
                    print("Your number is 52")
                  else:
                    print("Your number is 78")
                else:
                  print("Is the greatest prime divisor of your number less than 18")
                  Legal_Age_Pun=input()
                  if Legal_Age_Pun == "yes":
                    print("Your number is 68")
                  else:
                    print("Your number is 76")
            else:
              print("Is the greatest prime divisor of your number less than 39(yes/no)?")
              Data_Halved=input()
              if Data_Halved == "yes":
                print("Is the greatest prime divisor of your number less than 30(yes/no)?")
                Condition=input()
                if Condition == "yes":
                  print("Is the greatest prime divisor of your number less than 26(yes/no)?")
                  Random_Variable=input()
                  if Random_Variable == "yes":
                    print("Your number is 92")
                  else:
                    print("Your number is 58")
                else:
                  print("Is the greatest prime divisor of your number less than 34(yes/no)?")
                  Valiant_Variable=input()
                  if Valiant_Variable == "yes":
                    print("Your number is 62")
                  else:
                    print("Your number is 74")
              else:
                print("Is the greatest prime divisor of your number less than 45(yes/no)?")
                Triangle_Love=input()
                if Triangle_Love == "yes":
                  print("Is the greatest prime divisor of your number less than 42(yes/no)?")
                  Meme_Factors=input()
                  if Meme_Factors == "yes":
                    print("Your number is 82")
                  else:
                    print("Your number is 94")
        if "composite" in Set and "even" not in Set:
          if "less50/eq50" in Set:
            print("Is your number less than 34(yes/no)?")
            Forty_Three_Backwards=input()
            if Forty_Three_Backwards == "yes":
              print("Is your number less than 24(yes/no)?")
              One_Off=input()
              if One_Off == "yes":
                print("Is the last digit of your number square(yes/no)?")
                Not_Too_Odd=input()
                if Not_Too_Odd == "yes":
                  print("Your number is 21")
                else:
                  print("Your number is 15")
              else:
                print("Is the last digit of your number less than 5(yes/no)?")
                Prime_Vibe=input()
                if Prime_Vibe == "yes":
                  print("Your number is 33")
                else:
                  print("Your number is 27")
            else:
              print("Is your number less than 42(yes/no)?")
              Meme_Factors_Again=input()
              if Meme_Factors_Again == "yes":
                print("Is the last digit of your number square(yes/no)?")
                Arbitrary_Binary=input()
                if Arbitrary_Binary == "yes":
                  print("Your number is 39")
                else:
                  print("Your number is 35")
              else:
                print("Your number is 45")
          else:
            print("Is your number less than 76(yes/no)?")
            Backwards_Meme=input()
            if Backwards_Meme == "yes":
              print("Is your number less than 64(yes/no)")
              Power_Of_Two=input()
              if Power_Of_Two == "yes":
                print("Is the last digit of your number less than 4(yes/no)?")
                It_Goes_In_The_Square_Hole=input()
                if It_Goes_In_The_Square_Hole == "yes":
                  print("Is the last digit of your number square(yes/no)?")
                  Why_Do_I_Do_This=input()
                  if Why_Do_I_Do_This == "yes":
                    print("Your number is 51")
                  else:
                    print("Your number is 63")
                else:
                  print("Is your number less than 56(yes/no)?")
                  Seven_Fun=input()
                  if Seven_Fun == "yes":
                    print("Your number is 55")
                  else:
                    print("Your number is 57")
              else:
                print("Is the last digit of your number square(yes/no)?")
                Thus_I_Repeat=input()
                if Thus_I_Repeat == "yes":
                  print("Your number is 69, noice")
                else:
                  print("Is your number less than 70(yes/no)?")
                  Still_A_Variable=input()
                  if Still_A_Variable == "yes":
                    print("Your number is 65")
                  else:
                    print("Your number is 75")
            else:
              print("Is your number less than 89(yes/no)?")
              Final_Splitter=input()
              if Final_Splitter == "yes":
                print("Is the last digit of your number 7(yes/no)?")
                Seven_Crazy=input()
                if Seven_Crazy == "yes":
                  print("Is your number less than 82")
                  Something_About_X=input()
                  if Something_About_X == "yes":
                    print("Your number is 77")
                  else:
                    print("Your number is 87")
                else:
                  print("Your number is 85")
              else:
                print("Is your number less than 94(yes/no)?")
                The_End_Is_Near=input()
                if The_End_Is_Near == "yes":
                  print("Is the last digit of your number square(yes/no)?")
                  The_End_Is_Now=input()
                  if The_End_Is_Now == "yes":
                    print("Your number is 91")
                  else:
                    print("Your number is 93")
                else:
                  print("Your number is 97, little one")
    else:
      print("What should the upper bound be?")
      upper_bound=int(input())
      GuessBound=[0.5*(upper_bound),upper_bound]
      Guessr=0.5*upper_bound
      trying=1
      while True:
          print(f"Is your number >= {Guessr}, <= {Guessr}, or = {Guessr}")
          sign=input()
          diff_new=int(0.5*(abs(GuessBound[0]-GuessBound[1])))
          if sign == ">=":
            Guessr=Guessr+diff_new
            if GuessBound[0]<GuessBound[1]:
              del GuessBound[0]
              GuessBound.append(Guessr)
            else:
              del GuessBound[1]
              GuessBound.append(Guessr)
          if sign == "<=":
            Guessr=Guessr-diff_new
            if GuessBound[0]>GuessBound[1]:
              del GuessBound[0]
              GuessBound.append(Guessr)
            else:
              del GuessBound[1]
              GuessBound.append(Guessr)
          if sign == "=":
            print(f"Your number is {Guessr}, it took me {trying} tries, which should be about log2({upper_bound}) or {log2(upper_bound)}")
            print("Good game fool. I have won, and you are my pawn. You are but a cog in my machine, a simple variable in my expression. Hahahahahahahahahahahaha :P")
            break
          trying+=1
      
  if determine == 1:
    print("Guess my number!")
    print("")
    print("What should the upper bound of my number be?")
    a_choose=int(input())
    print("Start(yes/no)?")
    b=input()
    if b=="yes":
      h=1
      a=Random(a_choose)
      Prime=PrimeList(a+1)
      Even=Even(a+1)
      Square=Square(a)
      while True:
        for i in range(41):
          print("")
        print(f"My number is between 1 and {a_choose}")
        print("")
        print("Allowed Qs:")
        print("is a less than your number / greater than a")
        print("is a greater than your number / less than a")
        print("is your number prime / is prime")
        print("is your number even / is even")
        print("is your number square / is square")
        print("")
        if h == 1:
          print("If you want to see the operation each question applies, type 'definition'(this is recommended)")
          print("")
          definition=input()
        if definition == "definition" and h == 1:
          print("For ease:")
          print("let m be my number")
          print("let P denote the set of primes")
          print("let S denote the set of square numbers")
          print("let E denote the set of even numbers")
          print("you are assumed to have some understanding of sets, their correlated notation, and inequalities")
          print("")
          print("greater than a -> m>=a")
          print("less than a -> m<=a")
          print(f"is prime -> m \u2208 P")
          print(f"is even -> m \u2208 E")
          print(f"is square -> m \u2208 S")
        if len(Num_Props)>=1:
          print("My number is:")
          if "p" in Num_Props:
            print("prime")
          if "c" in Num_Props or "e" in Num_Props:
            print("composite")
          if "e" in Num_Props:
            print("even")
          if "o" in Num_Props:
            print("odd")
          if "s" in Num_Props:
            print("square")
          if "ns" in Num_Props:
            print("not square")
          if "g" in Num_Props:
            print(f"greater than {LBound[0]}")
          if "l" in Num_Props:
            print(f"less than {UBound[0]}")
          print("")
        elif definition == "debug":
          print(a)
          print(Prime)
          print(Even)
          print(Square)
        print("Question?")
        c=input()
        if c=="greater than a" or c=="is a less than your number":
          print("a?")
          d=int(input())
          if a>d:
            t="Yes"
            print(t)
            Num_Props.append("g")
            if len(LBound)==0:
              LBound.append(d)
            else:
              if d>LBound[0]:
                LBound.clear()
                LBound.append(d)
              elif d==LBound[0]:
                What_Is_Necessary=choice(High_IQ)
                if What_Is_Necessary==0:
                  print("Ya know what, yo stupid. You know dat, right? You asked a meaningless question, why, ya monsta?")
                if What_Is_Necessary==1:
                  if h==1:
                    print("You shall see me only once. I have rested for eternity and have awaken to forewarn you. The path you follow is a treacherous one that will lead to destruction, but if you stay loyal young one you shall succeed. Now go on my fellow rage-baiter")
                  else:
                    print("You know, at this point I can't tell. 'Tell what?' you ask. I can't tell if you're a dimwit, or have an iq too high. Just leave me be.")
                if What_Is_Necessary==2:
                  print("Ya know what, I don't believe ya. I just can't get behind this. Quit. QUIT! I mean it. Asking useless questions leads to nothing, fool. Just quit. Quit.")
                if What_Is_Necessary==3:
                  print("You're unreasonable, but yet not. Is not the beauty of the human immense. Btw you just wasted your life fooling a machine, kinda lame")
          else:
            t="No"
            print(t)
        elif c=="is prime" or c=="is your number prime":
          if a in Prime:
            t="Yes"
            print(t)
            Num_Props.append("p")
          else:
            t="No"
            print(t)
            Num_Props.append("c")
        elif c=="is even":
          if a in Even:
            t="Yes"
            print(t)
            Num_Props.append("e")
          else:
            t="No"
            print(t)
            Num_Props.append("o")
        elif c=="is square":
          if c in Square:
            t="Yes"
            print(t)
            Num_Props.append("s")
          else:
            t="No"
            print(t)
            Num_Props.append("ns")
        elif c=="less than a" or c=="is a greater than your number":
          print("a?")
          v=int(input())
          if v>a:
            t="Yes"
            print(t)
            Num_Props.append("l")
            if len(UBound)==0:
              UBound.append(v)
            else:
              if l<UBound[0]:
                UBound.clear()
                UBound.append(l)
              elif l==LBound[0]:
                What_Is_Unnecessary=choice(High_IQ)
                if What_Is_Unnecessary==0:
                  print("Why?! Why?! You low iq moron, I pity you. Just, why?!")
                if What_Is_Unnecessary==1:
                  print("If Magnus Carlsen can lose a tournament, I can believe that you're not trolling me")
                if What_Is_Unnecessary==2:
                  print("Nah, nah. You just playing with me, right? Right? Ahh, come on man. No way. You actually asked the same question twice. Nah bro, that's just sad. Not even disappointing")
                if What_Is_Unnecessary==3:
                  print("I give up. You're kidding me. You failed first grade, right. Yeah, that's what I thought")
          else:
            t="No"
            print(t)
        else:
          print("Nice try...That's illegal")
        print("")
        if h==1:
          print(f"You're at {h} try")
        else:
          print(f"You're at {h} tries")
        print("Ready to guess?(yes/no)")
        q=input()
        if q=="yes":
          print("Guess?")
          p=int(input())
          if p==a:
            if h==1:
              if God_Has_Need==0:
                print("Nah bro, you cheated, you had to. Let me guess, the Niemann method. Beads? Really? I'm disappointed. Truly")
                break
              else:
                print("Ayo, you cheated...but, you pass me 100 dollas and we keep it real civil. Like gentlemen, ain't no need for conflict")
                break
            elif h==2:
              print("Bro thinks he's Hikaru...", end="")
              sleep(0.5)
              print("You guessed in 2 tries")
              break
            else:
              print(f"Good job, you guessed my number in {h} tries")
              break
          else:
            print(f"You're at {h} tries, maybe you'll get it next try...punk")
            sleep(1.5)
        h+=1
    else:
      print("")
      print("Ahh man")
  print("Play again(yes/no)")
  The_Final_Answer=input()
  if The_Final_Answer == "no" or The_Final_Answer != "yes":
    print("See ya later pal, right? ;)")
    print("Game ending...", end="")
    sleep(0.75)
    print("Session ended")
    break
  else:
    print("Got ya :)")
    sleep(0.5)
    for i in range(41):
      print("")
    continue
  Next_Update_Is_5_Hours=True
