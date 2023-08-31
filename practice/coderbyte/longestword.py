""" 
LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
"""
import re
pattern = re.compile(r"\W+")  #used for splitting strings by a non-word(not alphabets or numbers) character
def LongestWord(sen):

  # code goes here
  res = pattern.split(sen)
  return max(res, key=len)

# keep this function call here 
print(LongestWord("Hello world123 567"))