# Spending five minutes a day in Python, a language that I didn’t practise a lot. A purpose like any other.
# Today we will split phrases in words. The goal is processing those words one by one.

phrase = "la bella y graciosa moza"
words = phrase.split()
numofwords = len(words)

print("got " + str(numofwords) + " words")

i = 1

for word in words:
    print("word # " + str(i) + " is '" + word + "'")
    i += 1
    
#
# You may also use a range for smaller and faster code.
#

for i in range(1, numofwords):
    print("word # " + str(i) + " is '" + words[i] + "'")
    
#
# See the usage of single quotes in a string delimited by double quotes.
#
