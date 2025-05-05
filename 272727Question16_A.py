# Question 16(a)
# Student name: Anthony Frtus

#function definition used in part (v)
def is_anagram(w1,w2):
    if (sorted(w1)==sorted(w2)):
        print(word1, "is an anagram of", word2)
    else:
        print(word1, "is not an anagram of", word2)
def is_phrase(w1,w2):
    if (sorted(w1)==sorted(w2)):
        print(word1, "is an anagram of", phrase)
    else:
        print(word1, "is not an anagram of", phrase)
        
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
low_word1 = word1.upper()
low_word2 = word2.upper()
if (sorted(low_word1)==sorted(low_word2)):
    print(word1, "is an anagram of", word2)
else:
    print(word1, "is not an anagram of", word2)
is_anagram(low_word1, low_word2)

phrase = input("Enter a phrase:")
low_phrase = phrase.upper()
low_phrase = low_phrase.replace(" ", "")
is_phrase(low_word1, low_phrase)
if (sorted(low_word2)==sorted(low_phrase)):
    print(word2, "is an anagram of", phrase)
else:
    print(word2, "is not an anagram of", phrase)
