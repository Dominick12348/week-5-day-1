# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
magic = "abracadabra"
print(magic[5:6])
print(magic[9:10])
print(magic.find("c"))


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[7:10])
print(alphabet[::2])
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy."
print(quote[83:98])


# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
info = "Phtyon is fun. Fun is good. Good is subjective"
print(info.find("subjective"))
print(info[36:])
print(info[::3])
info2 = " ".join(["subjective" , "is" , "good" , ".good" , "is" , "Fun" , ".fun" , "is" , "Python" ])
print(info2)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
lowercase = "MAY THE FORCE BE WITH YOU."
print(lowercase.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
list = "Make" , "haste" , "slowly"
list2 = " ".join(list)
print(list2.split("a"))

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
replace = "Life is what happens when you are busy making other plans."
print(replace.replace("busy" , "distracted"))
print(replace.replace("plans" , "mistakes"))
# Problem Set 4: String Properties and Advanced Operations
Repetition = "Iteration Iteration Iteration Iteration Iteration Iteration Iteration" 
print(Repetition)
# Concatenate the word "Iteration" 7 times.