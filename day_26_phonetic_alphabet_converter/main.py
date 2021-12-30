#student_dict = {
 #   "student": ["Angela", "James", "Lily"],
  #  "score": [56, 76, 98]
#}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
  #  pass

import pandas as pd
#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)
dict = {}
for (index,row) in data.iterrows():
    dict.update({row.letter:row.code})
print(dict)
user_input = input("Input the word to be converted to phonetic alphabet:\n")
word_list = []
for letter in user_input:
    word_list.append(dict.get(letter.upper()))
print(word_list)






