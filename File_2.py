with open(r"C:\Users\Yevhen\Desktop\Name.txt", "a") as file:
    file.write('Євген')
    file.write(' Данильченко')
    file.write(' 51 рік')
    file.write(' студент у ITStep Academy')

file.close()

with open(r"C:\Users\Yevhen\Desktop\Name.txt", "r") as file:
    print(file.read())

file.close()