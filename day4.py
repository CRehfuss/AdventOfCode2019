#Day 4
#Range is 134564-585159


#Part 1
i = 134564
numPasswords = 0
firstwave = []
while i < 585159:
    j = 1
    rep = False
    notDec = True
    while j < len(str(i)):
        if str(i)[j] < str(i)[j-1]:
            notDec = False
        if str(i)[j] == str(i)[j-1]:
            rep = True
        j+=1
    if notDec == True and rep == True:
        firstwave.append(i)
        numPasswords+=1
    i +=1


#part 2

numPasswords = 0


for i in firstwave:
    twoDigits = False
    if str(i)[0]==str(i)[1] and str(i)[1]!= str(i)[2]:
        twoDigits = True
    if str(i)[0]!=str(i)[1] and str(i)[1]==str(i)[2] and str(i)[2]!= str(i)[3]:
        twoDigits = True
    if str(i)[1]!=str(i)[2] and str(i)[2]==str(i)[3] and str(i)[3]!= str(i)[4]:
        twoDigits = True
    if str(i)[2]!=str(i)[3] and str(i)[3]==str(i)[4] and str(i)[4]!= str(i)[5]:
        twoDigits = True
    if str(i)[3]!=str(i)[4] and str(i)[4]==str(i)[5]:
        twoDigits = True
    if twoDigits==True:
        numPasswords +=1

print(numPasswords)