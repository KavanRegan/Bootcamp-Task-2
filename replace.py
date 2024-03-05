# - Create variable with ! to remove
word = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
# - Using .replace swap the ! for a space
word = word.replace("!", " ")
print(word)
# - Change the word to upper case
word = word.upper()
print(word)
# - Print the word
print(word[::-1])