
to_be_averaged = "cleaned_data.txt"

output_averaged = "averaged_data.txt"



averaged = open(output_averaged, "w")

uniqueXY = {}

with open(to_be_averaged) as input_file:
    header = input_file.readline()

    averaged.write(header)
    while True:
        line = input_file.readline()

        if (line == ""):
            break

        numbers = line.split() # turns string into list
        nums = [float(num) for num in numbers]

        if uniqueXY.get((nums[0], nums[1]), "empty") == "empty":
            print("new")
            uniqueXY[(nums[0], nums[1])] = [nums]
            print(uniqueXY)
        else:
            print("existing")
            uniqueXY[(nums[0], nums[1])].append(nums) 
            print(uniqueXY)


print(uniqueXY)

'''
[averaged.write(str(x) + " ") for x in roundedLine]

averaged.write("\n")
'''
