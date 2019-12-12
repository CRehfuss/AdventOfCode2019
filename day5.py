import sys, math, copy

# Read from the file
inFile = sys.argv[1]

f = open(inFile,'r') 
contents = f.read()
opcode = []

for content in contents.split(','):
    opcode.append(int(content))

# Change the positions!
# opcode[1] = 12
# opcode[2] = 2

i = 0
# loop through the codes
input = 5
numTest = 0
while i < len(opcode):
    thirdParam = 0
    secondParam = 0
    firstParam = 0
    strOp = str(opcode[i])
    if len(strOp) > 1:
        instruction = int(strOp[len(strOp)-2:])
    else:
        instruction = opcode[i]
    if len(strOp) == 5:
        thirdParam = int(strOp[0])
        secondParam = int(strOp[1])
        firstParam = int(strOp[2])
    elif len(strOp) == 4:
        secondParam = int(strOp[0])
        firstParam = int(strOp[1])
    elif len(strOp) == 3:
        firstParam = int(strOp[0])

    # 1: add the two
    if instruction == 1:
        if firstParam:
            first = opcode[i+1]
        else:
            first = opcode[opcode[i+1]]
        if secondParam:
            second = opcode[i+2]
        else:
            second = opcode[opcode[i+2]]
        if thirdParam:
            opcode[i+3] = first + second
        else:
            opcode[opcode[i+3]] = first + second

        i = i+4
    # 2: multiply the two    
    elif instruction == 2:
        if firstParam:
            first = opcode[i+1]
        else:
            first = opcode[opcode[i+1]]
        if secondParam:
            second = opcode[i+2]
        else:
            second = opcode[opcode[i+2]]
        if thirdParam:
            opcode[i+3] = first * second
        else:
            opcode[opcode[i+3]] = first * second

        i = i+4
    # 3: input
    elif instruction == 3:
        if firstParam:
            opcode[i+1] = input
        else:
            opcode[opcode[i+1]] = input
        i = i+2    
    # 4: outputs
    elif instruction == 4:
        print("Test number ", numTest)
        if firstParam:
            print(opcode[i+1])
        else:
            print(opcode[opcode[i+1]])
        numTest+=1
        i = i+2
    #5: jump-if-true
    elif instruction == 5:
        if firstParam:
            first = opcode[i+1]
        else:
            first = opcode[opcode[i+1]]
        if secondParam:
            second = opcode[i+2]
        else:
            second = opcode[opcode[i+2]]
        if first:
            i = second
        else:
            i += 3
    #6: jump-if-false
    elif instruction == 6:
        if firstParam:
            first = opcode[i+1]
        else:
            first = opcode[opcode[i+1]]
        if secondParam:
            second = opcode[i+2]
        else:
            second = opcode[opcode[i+2]]
        if first == 0:
            i = second
        else:
            i += 3
    #7: less than
    elif instruction == 7:
        if firstParam:
            first = opcode[i+1]
        else:
            first = opcode[opcode[i+1]]
        if secondParam:
            second = opcode[i+2]
        else:
            second = opcode[opcode[i+2]]
        if thirdParam:
            opcode[i+3] = int(first<second)
        else:
            opcode[opcode[i+3]] = int(first<second)
        i+=4
    #8: equals
    elif instruction == 8:
        if firstParam:
            first = opcode[i+1]
        else:
            first = opcode[opcode[i+1]]
        if secondParam:
            second = opcode[i+2]
        else:
            second = opcode[opcode[i+2]]
        if thirdParam:
            opcode[i+3] = int(first==second)
        else:
            opcode[opcode[i+3]] = int(first==second)

        i+=4
    # Exit the loop
    elif instruction == 99:
        i = len(opcode)+1
    # something wrong 
    else:
        print(i)
        print(opcode[i])
        print("something else ", instruction)
        break