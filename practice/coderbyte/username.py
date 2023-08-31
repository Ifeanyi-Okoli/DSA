import re

input = str(input('please enter your username: '))

def CodelandUsernameValidation(str):
  pattern = re.compile(r"^[a-zA-Z][\w_]{4,25}[^_]$")
  res = pattern.match(str)
  str = "true" if res else "false"
  return str

# keep this function call here 
  # if len(str) < 4 or len(str) > 25: return "false"
  
  # for i in range(len(str)):
  #   if str[0].isalpha() and str[-1] != "_" and str[i].isalnum() or str[i] == "_":
  #     return "true"
  # else: "false"
      



print(CodelandUsernameValidation(input))