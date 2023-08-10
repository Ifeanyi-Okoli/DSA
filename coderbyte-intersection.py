def FindIntersection(strArr):

  # code goes here
  res = []
  res1 = ", "
  strA = strArr[0].split(", ")
  strB = strArr[1].split(", ")
  for i in range(len(strA)):
    for j in range(len(strB)):
      if strA[i] == strB[j]:
        res.append(strA[i])
  result = res1.join(res)
  return result

inputA = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# keep this function call here 
print(FindIntersection(inputA))