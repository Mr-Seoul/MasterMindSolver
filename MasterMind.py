PreviousGuesses = []
Allpossible = ["y","r","g","G","b","p","w","o"]
Possible = []
Turn = 0

def CheckValidity(prev, input):
    for i in prev:
        input = str(input)
        i[0] = str(i[0])
        red = int(i[0][0] == input[0]) + int(i[0][1] == input[1]) + int(i[0][2] == input[2]) + int(i[0][3] == input[3])
        yellow = int(i[0][0] in input) + int(i[0][1] in input) + int(i[0][2] in input) + int(i[0][3] in input) - red
        if int(red) != int(i[1]) or int(yellow) != int(i[2]):
            return False
    return True

def UpdatePossible():
    global Possible
    Possible = [i for i in Possible if CheckValidity(PreviousGuesses,i) == True]

def InitializeAllPossible():
    global Allpossible
    global Possible
    for i in Allpossible:
        temp1 = Allpossible.copy()
        temp1.remove(i)
        WithoutI = temp1
        for j in WithoutI:
            temp2 = WithoutI.copy()
            temp2.remove(j)
            WithoutJ = temp2
            for m in WithoutJ:
                temp3 = WithoutJ.copy()
                temp3.remove(m)
                WithoutM = temp3
                for n in WithoutM:
                    addedstring = i + j + m + n
                    Possible.append(str(addedstring))

def Similarity(str1, str2):
    CorrectRate = 1
    AlmostRate = 1
    red = int(str1[0] == str2[0]) + int(str1[1] == str2[1]) + int(str1[2] == str2[2]) + int(str1[3] == str2[3])
    yellow = int(str1[0] in str2) + int(str1[1] in str2) + int(str1[2] in str2) + int(str1[3] in str2) - red
    return red*CorrectRate + AlmostRate*yellow

def GetBestGuess():
    global Possible
    Guesses = []
    for i in Possible:
        sum = 0
        for j in Possible:
            sum += Similarity(i,j)
        Guesses.append([i,sum])
    Guesses.sort(key = lambda x:x[1],reverse=True)
    return Guesses[0][0]

def main():
    global Turn
    global PreviousGuesses
    global Possible
    PreviousGuesses = []
    Turn = 0
    Possible = []
    InitializeAllPossible()
    Done = False
    while not Done:
            if len(Possible) < 1:
                print("There is no possible answer")
                return -1
            
            print("Possible Combinations left: " + str(len(Possible)))

            Guess = ""
            if Turn == 0:
                Guess = "gyor"
            else:
                Guess = GetBestGuess()
            print(f"Turn {Turn + 1} : Try {Guess} and input how many red and yellow ")

            print("\n")

            temp = [[],[],[]]
            temp[0] = Guess

            red = input()
            temp[1] = red

            yellow = input()
            temp[2] = yellow

            PreviousGuesses.append(temp)
            UpdatePossible()
            if len(Possible) != 1 and Guess in Possible: 
                Possible.remove(Guess)
            Turn += 1
            
            if len(Possible) == 1:
                Done = True
                print(f"The answer is {Possible[0]}")
                if Guess != Possible[0]:
                    Turn += 1
    print(f"Done in {Turn} turns")
    return Turn

main()