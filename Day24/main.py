# Create a Mail Merge Project

with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as final_letter:
            final_letter.write(new_letter)
