import sys, math
inFile = sys.argv[1]
# take its mass, divide by three, round down, and subtract 2

#Read from a file and write to a list, stripping the new lines
f = open(inFile,'r') 
contents = f.read()
file_as_list = contents.splitlines()

int_list = []
for strMass in file_as_list:
    int_list.append(int(strMass))

fuel = 0
for mass in int_list:
    fuel += math.floor(mass/3)-2



# # Part two
sum2 = 0
for fuel in int_list:
    while(fuel>0):
        print("mass level: ", fuel, "requires ", math.floor(fuel/3)-2, " fuel")
        fuel = math.floor(fuel/3)-2
        if(fuel>0):
            sum2 += fuel

print(sum2)