import re

input = str(input('please enter your password: '))

def CodelandUsernameValidation(str):
  pattern = re.compile(r"^[a-zA-Z][\w_]{2,23}[^_]$")
  res = pattern.match(str)
  str = "true" if res else "false"
  return str

# keep this function call here 



print(CodelandUsernameValidation(input))