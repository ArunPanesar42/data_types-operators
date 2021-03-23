# # Strings and Casting
#
#
# # Lets have a look at some industry practice
# greetings = "Hello World"
# single_quotes = 'Single Quotes \`WOW\` '
# double_quotes = "Double Quotes 'WOW' "
# print(greetings)
# print(single_quotes)
# print(double_quotes)

# # String Slicing
# greetings = "Hello world!" # String
# # Indexing on python starts from 0
# # H e l l o   w o r l  d  !
# # 0 1 2 3 4 5 6 7 8 9 10 11

# # To find out the length of this statement we do len()
# greetings = "Hello World!"
# print(len(greetings))
# # For INDEXING we use [] to slice
# print(greetings[0:5]) # This will output Hello
# print(greetings[6:11]) # This will output World
# # Reverse indexing starts with -1
# print(greetings[-1])

# # Lets have a look at some string methods
# white_space = "lots of spaces                  "
# print(len(white_space))
# # strip() helps us get rid of all white spaces
# print(len(white_space.strip()))

# count() counts a number of times a word is mentioned
example_text = "Here is some text with text that has alot of text"
print(example_text)
print(example_text.count("text"))
# To change to Upper case we use .upper()
print(example_text.upper())
# We use .lower() to change to lower
print(example_text.lower())
# To make the first letter in upper case we use .capitalize()
print(example_text.capitalize())
# To replace we use .replace() and put the word we want to get rid of with the word we want
print(example_text.replace("alot","lots"))