#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names_list = []
with open("Input/Names/invited_names.txt") as names:
    for name in names:
        names_list.append(name.strip())
names.close()
print(names_list)
with open("Input/Letters/starting_letter.txt","r") as letter:
    for name in names_list:
        current_file = open(f"letter_to_{name}.txt","w+")
        for line in letter:
            current_file.write(line.replace('[name]',name))







