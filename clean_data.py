
to_be_cleaned = "L1_5N1_12.txt"

output_cleaned = "cleaned_data2.txt"



cleaned = open(output_cleaned, "w")

with open(to_be_cleaned) as file:
    header = file.readline()
    cleaned.write(header)
    while True:


        line = file.readline()

        if (line == ""):
            break

        numbers = line.split()
        roundedLine = [round(float(num), 4) for num in numbers]

        roundedLine[0] += 1
        ''' adding 1 here because by default the neural
        network has 1 hidden layer and I started from zero
        in the for loop
        '''
        [cleaned.write(str(x) + " ") for x in roundedLine]

        cleaned.write("\n")
