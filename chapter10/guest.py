filename = 'guest.txt'
name = input("Enter your name for our guest book: ")

with open(filename, 'a') as file_object:
    file_object.write(name + '\n')

print("Thanks for signing the guest book!")
