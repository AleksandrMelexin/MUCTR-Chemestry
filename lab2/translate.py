f = open("temp.txt", "r")
numbers = map(float, f.readline().split())
print(*numbers)