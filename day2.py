import sys, math, copy

# Read from the file
inFile = sys.argv[1]

f = open(inFile,'r') 
contents = f.read()
opcode = []

for content in contents.split(','):
    opcode.append(int(content))

# Change the positions!
opcode[1] = 12
opcode[2] = 2

i = 0
# loop through the codes

while i < len(opcode):
    # 1: add the two
    if opcode[i] == 1:
        opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
        i = i+4
    # 2: multiply the two    
    elif opcode[i] == 2:
        opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
        i = i+4
    # Exit the loop
    elif opcode[i] == 99:
        i = len(opcode)+1
    # Catch all    
    else:
        print("Opcode at ", i, " is no 1,2, or 99, it is: ", opcode[i])
        exit

print('OPCODE AFTER \n')
print(opcode[0])



#PART 2
inFile = sys.argv[1]

f = open(inFile,'r') 
contents = f.read()
opcode = []
reset_memory = []
for content in contents.split(','):
    opcode.append(int(content))
    reset_memory.append(int(content))


j=0
k=0
while(j<100):
    while(k<100):
        opcode = copy.deepcopy(reset_memory)
        opcode[1] = j
        opcode[2] = k
        i = 0
        while i < len(opcode):
            # 1: add the two
            if opcode[i] == 1:
                opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
                i = i+4
            # 2: multiply the two    
            elif opcode[i] == 2:
                opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
                i = i+4
            # Exit the loop
            elif opcode[i] == 99:
                i = len(opcode)+1
            # Catch all    
            else:
                print("Something was wrong with opcode ", opcode[i], "for i ", i)
                print(j, k)
                

        if(opcode[0] == 19690720):
            print("IT HIT")
            print(j,k)
            print(100*j+k)
        k = k+1
    j = j+1
    k = 0


