
cleaned = open("cleaned_data.txt", "w")

with open("layers0_5_nodes1_20.txt") as file:
    line = file.readline()
    numbers = line.split()
    roundedLine = [round(float(num), 4) for num in numbers]
    [cleaned.write(str(x)) for x in roundedLine]
