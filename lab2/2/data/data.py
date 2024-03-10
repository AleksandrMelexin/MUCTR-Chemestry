import pandas as pd
import csv

f = open("temperature.txt", "r")
T = list(map(float, f.readlines()))
f = open("bara.txt", "r")
P = list(map(float, f.readlines()))
f = open("visc.txt", "r")
D = list(map(float, f.readlines()))
f = open("data.txt", "w")
for i in range(len(T)):
        Temperature = str(T[i])
        Presure = str(P[i])
        Density = str(D[i])
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
        
