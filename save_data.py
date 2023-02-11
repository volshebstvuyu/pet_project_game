file = open("save.txt", "w", encoding="utf-8")
file.write("Hello, world")
file.close()
print("the end")

file = open("save.txt", "r", encoding="utf-8")
text = file.read()
file.close
print(text)

file = open("save.txt", "a", encoding="utf-8")
file.write("/nnew text")
file.close()
print("the end")

file = open("save.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
print(lines)