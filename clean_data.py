
cleaned = open("cleaned_data.txt", "w")

with open("layers0_5_nodes1_20.txt") as file:
    header = file.readline()
    cleaned.write(header)
    while(1):


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
