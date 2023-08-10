def LongestWord(sen):

  # code goes here
  res = ""
  arr = sen.split(' ')
  length = 0
  # print(arr)
  for ar in arr:
    if len(ar)>length:
      res =ar
  return res

# keep this function call here 
print(LongestWord("fun&!! time"))