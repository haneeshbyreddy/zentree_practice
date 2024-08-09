with open("text_file.txt", 'r') as file:
    message = file.read()

with open("text_file.txt", 'w') as file:
    file.write(message)
    print(file.tell())

with open("text_file.txt", 'r') as file:
    print(file.read())

