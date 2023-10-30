with open("Python\\novieFajl.txt",mode="w") as myFile:
    myFile.write("\nnovie red")

with open("Python\\novieFajl.txt",mode='r') as myFile:
    content=myFile.read()


print(content)