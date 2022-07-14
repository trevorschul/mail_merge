#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as file:
    list_of_names = file.readlines()
list_of_names = [s.rstrip() for s in list_of_names]
with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    starting_letter = file.read()

for person in list_of_names:
    new_letter = starting_letter.replace(PLACEHOLDER, person)
    with open(f"./Output/ReadyToSend/{person}_letter.txt", mode="w") as file:
        file.write(new_letter)
