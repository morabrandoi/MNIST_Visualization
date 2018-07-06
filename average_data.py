
to_be_averaged = "cleaned_data.txt"

output_averaged = "averaged_data.txt"



averaged = open(output_averaged, "w")

uniqueXY = {}

# put data lists into dictionary where keys are the nodes and layers (first 2)
# value is a list of the different list of scores with the same nodes and layers
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
            uniqueXY[(nums[0], nums[1])] = [nums]
        else:
            uniqueXY[(nums[0], nums[1])].append(nums)


# at this point each data list is grouped by nodes and layers in the dictionary
averaged_dict = {}
for key in uniqueXY.keys():
    num_of_points = len(uniqueXY[key])
    if num_of_points > 1:
        averaged_vals = [key[0],key[1],0,0,0,0]
        for common_i in range(2, len(uniqueXY[key][0])): #first two el guaranteed to be the same
            for data_list in uniqueXY[key]:
                averaged_vals[common_i] += data_list[common_i]
            averaged_vals[common_i] = round(averaged_vals[common_i] / num_of_points, 4)
        averaged_dict[key] = averaged_vals

    else:
        averaged_dict[key] = uniqueXY[key]

for key in averaged_dict.keys():
    averaged_list = averaged_dict[key]
    [averaged.write(str(x) + " ") for x in averaged_list]
    averaged.write("\n")
