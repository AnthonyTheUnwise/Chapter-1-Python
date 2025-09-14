#Brainstorm 04/09/25
import random
P1_t = 1000
P2_t = 1000
P3_t = 1000
P4_t = 1000
Pot = 0
P1 = []
P2 = []
P3 = []
P4 = []
HangingNum = []
CardsMain=["HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
          "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
          "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",
          "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK"]
Cards=["HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
       "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
       "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",
       "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK"]

WinningList = []

def WinCalc(P0):
    HandValue = 0
    Club = P0.count("C")
    Spade = P0.count("S")
    Heart = P0.count("H")
    Diamond = P0.count("D")
    if Club == 5:
        HandValue = 4
        return HandValue
    elif Spade == 5:
        HandValue = 4
        return HandValue
    elif Heart == 5:
        HandValue = 4
        return HandValue
    elif Diamond == 5:
        HandValue = 4
        return HandValue
    for y in range(2, 11):
        Count = P0.count(str(y))
        if Count == 2:
            HandValue = 2
            return HandValue
        elif Count == 3:
            HandValue = 3
            return HandValue
        elif Count == 4:
             HandValue = 5
             return HandValue
        elif Count > 0:
             HandValue = (y/10)
    Ace = P0.count("A")
    King = P0.count("K")
    Queen = P0.count("Q")
    Jack = P0.count("J")
    if Ace > 0:
        HandValue = 1.75
        return HandValue
    elif King > 0:
        HandValue = 1.5
        return HandValue
    elif Queen > 0:
        HandValue = 1.25
        return HandValue
    elif Jack > 0:
        HandValue = 1.1
        return HandValue
    else:
        return HandValue
def GamblingRound1(P0, Num): # I want player to decide to gamble if cards are good enough
    GoIn = 0
    Value = 0
    Club = P0.count("C")
    Spade = P0.count("S")
    Heart = P0.count("H")
    Diamond = P0.count("D")
    if Club == 2:
        GoIn += 1
    elif Spade == 2:
        GoIn += 1
    elif Heart == 2:
        GoIn += 1
    elif Diamond == 2:
        GoIn += 1 #If same suit they SHOULD bet
    for y in range(2, 11):
        Count = P0.count(str(y))
        Value += (Count*y) #Count value of cards, if 15 or higher we go bet
        if Count == 2:
            GoIn += 5
    Count = P0.count("J")
    Value += (Count*10)
    if Count == 2:
        GoIn += 5 #Same thing but face cards
    Count = P0.count("Q")
    Value += (Count*10)
    if Count == 2:
        GoIn += 6
    Count = P0.count("K")
    Value += (Count*15)
    if Count == 2:
        GoIn += 7
    Count = P0.count("A")
    Value += (Count*20)
    if Count == 2:
        GoIn += 10
    if Value > 14:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif GoIn > 0:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif random.randint(1,2) == 1:
        print("Player", Num, "is betting with:", P0)
        return Num
    else:
        print("Player", Num, "Folded.")

def GamblingRound2(P0, Num): # I want player to decide to gamble if cards are good enough
    GoIn = 0
    Value = 0
    Club = P0.count("C")
    Spade = P0.count("S")
    Heart = P0.count("H")
    Diamond = P0.count("D")
    if Club > 2:
        GoIn += 2
    elif Spade > 2:
        GoIn += 2
    elif Heart > 2:
        GoIn += 2
    elif Diamond > 2:
        GoIn += 2 #If same suit they SHOULD bet
    for y in range(2, 11):
        Count = P0.count(str(y))
        Value += (Count*y) #Count value of cards, if 15 or higher we go bet
        if Count == 2:
            GoIn += 5
        elif Count > 2:
            GoIn += 15
    Count = P0.count("J")
    Value += (Count*10)
    if Count == 2:
        GoIn += 5 #Same thing but face cards
    elif Count > 2:
            GoIn += 30
    Count = P0.count("Q")
    Value += (Count*10)
    if Count == 2:
        GoIn += 6
    elif Count > 2:
        GoIn += 30
    Count = P0.count("K")
    Value += (Count*15)
    if Count == 2:
        GoIn += 7
    elif Count > 2:
        GoIn += 35
    Count = P0.count("A")
    Value += (Count*20)
    if Count == 2:
        GoIn += 10
    elif Count > 2:
        GoIn += 50
    if Value > 20:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif GoIn > 1:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif random.randint(1,3) == 1:
        print("Player", Num, "is betting with:", P0)
        return Num
    else:
        print("Player", Num, "Folded.")

def GamblingRound3(P0, Num): # I want player to decide to gamble if cards are good enough
    GoIn = 0
    Value = 0
    Club = P0.count("C")
    Spade = P0.count("S")
    Heart = P0.count("H")
    Diamond = P0.count("D")
    if Club > 2:
        GoIn += 2
    elif Spade > 2:
        GoIn += 2
    elif Heart > 2:
        GoIn += 2
    elif Diamond > 2:
        GoIn += 2 #If same suit they SHOULD bet
    for y in range(2, 11):
        Count = P0.count(str(y))
        Value += (Count*y) #Count value of cards, if 15 or higher we go bet
        if Count == 2:
            GoIn += 1
        elif Count > 2:
            GoIn += 15
    Count = P0.count("J")
    Value += (Count*10)
    if Count == 2:
        GoIn += 5 #Same thing but face cards
    elif Count > 2:
            GoIn += 30
    Count = P0.count("Q")
    Value += (Count*10)
    if Count == 2:
        GoIn += 6
    elif Count > 2:
        GoIn += 30
    Count = P0.count("K")
    Value += (Count*15)
    if Count == 2:
        GoIn += 7
    elif Count > 2:
        GoIn += 35
    Count = P0.count("A")
    Value += (Count*20)
    if Count == 2:
        GoIn += 10
    elif Count > 2:
        GoIn += 50
    if Value > 18:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif GoIn > 1:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif random.randint(1,4) == 1:
        print("Player", Num, "is betting with:", P0)
        return Num
    else:
        print("Player", Num, "Folded.")

def GamblingRound4(P0, Num): # I want player to decide to gamble if cards are good enough
    GoIn = 0
    Value = 0
    Club = P0.count("C")
    Spade = P0.count("S")
    Heart = P0.count("H")
    Diamond = P0.count("D")
    if Club > 3:
        GoIn += 2
    elif Club == 2:
        GoIn += 1
    elif Spade > 3:
        GoIn += 2
    elif Spade == 2:
        GoIn += 1
    elif Heart > 3:
        GoIn += 2
    elif Heart == 2:
        GoIn += 1
    elif Diamond > 3:
        GoIn += 2
    elif Diamond == 2:
        GoIn += 1#If same suit they SHOULD bet
    for y in range(2, 11):
        Count = P0.count(str(y))
        Value += (Count*y) #Count value of cards, if 15 or higher we go bet
        if Count == 2:
            GoIn += 1
        elif Count > 2:
            GoIn += 15
    Count = P0.count("J")
    Value += (Count*10)
    if Count == 2:
        GoIn += 5 #Same thing but face cards
    elif Count > 2:
            GoIn += 30
    Count = P0.count("Q")
    Value += (Count*10)
    if Count == 2:
        GoIn += 6
    elif Count > 2:
        GoIn += 30
    Count = P0.count("K")
    Value += (Count*15)
    if Count == 2:
        GoIn += 7
    elif Count > 2:
        GoIn += 35
    Count = P0.count("A")
    Value += (Count*20)
    if Count == 2:
        GoIn += 10
    elif Count > 2:
        GoIn += 50
    if Value > 22:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif GoIn > 1:
        print("Player", Num, "is betting with:", P0)
        return Num
    elif random.randint(1,4) == 1:
        print("Player", Num, "is betting with:", P0)
        return Num
    else:
        print("Player", Num, "Folded.")

for y in range(0, 8):
    CurrentCard = random.randint(0, (len(Cards)-1))
    CurrentCard = Cards[CurrentCard]
    HangingNum.append(CurrentCard)
    Cards.remove(CurrentCard)
P1.append(HangingNum[0])
P1.append(HangingNum[1])
P2.append(HangingNum[2])
P2.append(HangingNum[3])
P3.append(HangingNum[4])
P3.append(HangingNum[5])
P4.append(HangingNum[6])
P4.append(HangingNum[7])
P1Str = str(P1)
P2Str = str(P2)
P3Str = str(P3)
P4Str = str(P4)

HangingNum.clear()

# Now lets go do the game ;D

"""BREAK TO SHOW THAT ACTUAL GAME IS BELOW!!!
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
This is for my sanity """
while True:
    print("Round 1:\n")
    WinningList.append(GamblingRound1(P1Str, 1))
    WinningList.append(GamblingRound1(P2Str, 2))
    WinningList.append(GamblingRound1(P3Str, 3))
    WinningList.append(GamblingRound1(P4Str, 4))
    
    for y in range (0, 4):
        if WinningList.count(None) > 0:
            WinningList.remove(None)
    if len(WinningList) == 1:
        print()
        print("Player", WinningList, "won!")
        Winner = WinningList[0]
        if Winner == 1:
            Pot = ((Pot // 10) * 9)
            P1_t += Pot
        if Winner == 2:
            Pot = ((Pot // 10) * 9)
            P2_t += Pot
        if Winner == 3:
            Pot = ((Pot // 10) * 9)
            P3_t += Pot
        if Winner == 4:
            Pot = ((Pot // 10) * 9)
            P4_t += Pot
        break
    elif len(WinningList) == 0:
        print()
        print("The house wins!")
        Pot = 0
        break

    for y in range(0, 3):
        CurrentCard = random.randint(0, (len(Cards)-1))
        CurrentCard = Cards[CurrentCard]
        HangingNum.append(CurrentCard)
        Cards.remove(CurrentCard)

    if WinningList.count(1) == 1:
        P1.append(str(HangingNum))
        P1_t -= 10
        Pot += 10
    if WinningList.count(2) == 1:
        P2.append(str(HangingNum))
        P2_t -= 10
        Pot += 10
    if WinningList.count(3) == 1:
        P3.append(str(HangingNum))
        P3_t -= 10
        Pot += 10
    if WinningList.count(4) == 1:
        P4.append(str(HangingNum))
        P4_t -= 10
        Pot += 10

    """ROUND TWO CODE
    --------------------------------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------------------------------
    SPACE"""



    print("\nRound 2:\nTable's Flop:", HangingNum, "\n")
    
    P1Str = str(P1)
    P2Str = str(P2)
    P3Str = str(P3)
    P4Str = str(P4)

    if WinningList.count(1) == 1:
        WinningList.remove(1)
        WinningList.append(GamblingRound2(P1Str, 1))
    if WinningList.count(2) == 1:
        WinningList.remove(2)
        WinningList.append(GamblingRound2(P2Str, 2))
    if WinningList.count(3) == 1:
        WinningList.remove(3)
        WinningList.append(GamblingRound2(P3Str, 3))
    if WinningList.count(4) == 1:
        WinningList.remove(4)
        WinningList.append(GamblingRound2(P4Str, 4))
        
    for y in range (0, 4):
        if WinningList.count(None) > 0:
            WinningList.remove(None)
    if len(WinningList) == 1:
        print()
        print("Player", WinningList, "won!")
        Winner = WinningList[0]
        if Winner == 1:
            Pot = ((Pot // 10) * 9)
            P1_t += Pot
        if Winner == 2:
            Pot = ((Pot // 10) * 9)
            P2_t += Pot
        if Winner == 3:
            Pot = ((Pot // 10) * 9)
            P3_t += Pot
        if Winner == 4:
            Pot = ((Pot // 10) * 9)
            P4_t += Pot
        break
    elif len(WinningList) == 0:
        print()
        print("The house wins!")
        Pot = 0
        break


    HangingNum1 = list(HangingNum)
    HangingNum.clear()
    CurrentCard = random.randint(0, (len(Cards)-1))
    CurrentCard = Cards[CurrentCard]
    HangingNum.append(CurrentCard)
    Cards.remove(CurrentCard)
    HangingNum1 = HangingNum1 + HangingNum

    if WinningList.count(1) == 1:
        P1.append(str(HangingNum))
        P1_t -= 30
        Pot += 30
    if WinningList.count(2) == 1:
        P2.append(str(HangingNum))
        P2_t -= 30
        Pot += 30
    if WinningList.count(3) == 1:
        P3.append(str(HangingNum))
        P3_t -= 30
        Pot += 30
    if WinningList.count(4) == 1:
        P4.append(str(HangingNum))
        P4_t -= 30
        Pot += 30


    """ THIRD ROUND SO CLOSE !!!
    --------------------------------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------------------------------
    YIPPEE!!!"""

    print("\nRound 3:\nTable's Flip:", HangingNum1, "\n")

    P1Str = str(P1)
    P2Str = str(P2)
    P3Str = str(P3)
    P4Str = str(P4)

    if WinningList.count(1) == 1:
        WinningList.remove(1)
        WinningList.append(GamblingRound3(P1Str, 1))
    if WinningList.count(2) == 1:
        WinningList.remove(2)
        WinningList.append(GamblingRound3(P2Str, 2))
    if WinningList.count(3) == 1:
        WinningList.remove(3)
        WinningList.append(GamblingRound3(P3Str, 3))
    if WinningList.count(4) == 1:
        WinningList.remove(4)
        WinningList.append(GamblingRound3(P4Str, 4))
    
    for y in range (0, 4):
        if WinningList.count(None) > 0:
            WinningList.remove(None)
    if len(WinningList) == 1:
        print()
        print("Player", WinningList, "won!")
        Winner = WinningList[0]
        if Winner == 1:
            Pot = ((Pot // 10) * 9)
            P1_t += Pot
        if Winner == 2:
            Pot = ((Pot // 10) * 9)
            P2_t += Pot
        if Winner == 3:
            Pot = ((Pot // 10) * 9)
            P3_t += Pot
        if Winner == 4:
            Pot = ((Pot // 10) * 9)
            P4_t += Pot
        break
    elif len(WinningList) == 0:
        print()
        print("The house wins!")
        Pot = 0
        break


    HangingNum2 = list(HangingNum1)
    HangingNum.clear()
    CurrentCard = random.randint(0, (len(Cards)-1))
    CurrentCard = Cards[CurrentCard]
    HangingNum.append(CurrentCard)
    Cards.remove(CurrentCard)
    HangingNum2 = HangingNum2 + HangingNum

    if WinningList.count(1) == 1:
        P1.append(str(HangingNum))
        P1_t -= 50
        Pot += 50
    if WinningList.count(2) == 1:
        P2.append(str(HangingNum))
        P2_t -= 50
        Pot += 50
    if WinningList.count(3) == 1:
        P3.append(str(HangingNum))
        P3_t -= 50
        Pot += 50
    if WinningList.count(4) == 1:
        P4.append(str(HangingNum))
        P4_t -= 50
        Pot += 50

    """FINAL ROUND !!!
    --------------------------------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------------------------------
    YIPPEE!!!"""

    print("\nRound 4:\nTable's River:", HangingNum2, "\n")

    P1Str = str(P1)
    P2Str = str(P2)
    P3Str = str(P3)
    P4Str = str(P4)

    if WinningList.count(1) == 1:
        WinningList.remove(1)
        WinningList.append(GamblingRound4(P1Str, 1))
    if WinningList.count(2) == 1:
        WinningList.remove(2)
        WinningList.append(GamblingRound4(P2Str, 2))
    if WinningList.count(3) == 1:
        WinningList.remove(3)
        WinningList.append(GamblingRound4(P3Str, 3))
    if WinningList.count(4) == 1:
        WinningList.remove(4)
        WinningList.append(GamblingRound4(P4Str, 4))
    
    for y in range (0, 4):
        if WinningList.count(None) > 0:
            WinningList.remove(None)

    """
    Now its the hard part oh no...#
    we gotta compare winners (nil)
    wish me luck cause its 5pm on a sunday and i got so much other hw !!!
    """


    if len(WinningList) > 1:
        if WinningList.count(1) == 1:
            P1 = WinCalc(P1)
        if WinningList.count(2) == 1:
            P2 = WinCalc(P2)
        if WinningList.count(3) == 1:
            P3 = WinCalc(P3)
        if WinningList.count(4) == 1:
            P4 = WinCalc(P4)
        break

    if len(WinningList) == 1:
        print()
        print("Player", WinningList, "won!")
        Winner = WinningList[0]
        if Winner == 1:
            Pot = ((Pot // 10) * 9)
            P1_t += Pot
        if Winner == 2:
            Pot = ((Pot // 10) * 9)
            P2_t += Pot
        if Winner == 3:
            Pot = ((Pot // 10) * 9)
            P3_t += Pot
        if Winner == 4:
            Pot = ((Pot // 10) * 9)
            P4_t += Pot
        break
    elif len(WinningList) == 0:
        print()
        print("The house wins!")
        Pot = 0
        break   

    if WinningList.count(1) == 1:
        P1.append(str(HangingNum))
        P1_t -= 100
        Pot += 100
    if WinningList.count(2) == 1:
        P2.append(str(HangingNum))
        P2_t -= 100
        Pot += 100
    if WinningList.count(3) == 1:
        P3.append(str(HangingNum))
        P3_t -= 100
        Pot += 100
    if WinningList.count(4) == 1:
        P4.append(str(HangingNum))
        P4_t -= 100
        Pot += 100
    break
    