import csv


f = open("temp.txt", "r")
T = list(map(float, f.readline().split()))
f = open("pressure.txt", "r")
P = list(map(float, f.readline().split()))
f = open("density.txt", "r")
D = [list(map(float, line.split())) for line in f.readlines()]
f = open("data.txt", "w")
for i in range(len(P)):
    for j in range(len(T)):
        Temperature = str(round(T[j] + 273.15, 2))
        Presure = str(P[i])
        Density = str(D[i][j])
        line = Temperature + "," + Presure + "," + Density + "\n"
        f.write(line)
f.close()

with open('data.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('../data.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Temperature', 'Pressure', 'Density'))
        writer.writerows(lines)        
