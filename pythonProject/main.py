


file = open("test.txt", "w")

file.write("ahoj svet akosa mas")

file.close()

a = input()
file = open("test.txt", "r")
data = file.read()
file.close()

print("data zo suboru")
print(data)