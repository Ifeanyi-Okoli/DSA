""" 
You will be given an array of objects (hashes in ruby) representing data about developers who have signed up to attend the coding meetup that you are organising for the first time.

Your task is to return the number of JavaScript developers coming from Europe.

For example, given the following list:

lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]
"""

# def count_developers(lst):
#     # Your code here
#     count=0
#     for i in lst:
#         if i["continent"] == "Europe" and i["language"] == "JavaScript":
#             count += 1
#     return count
# or


def count_developers(lst):
    # Your code here
    #    return sum(1 for i in lst if i["continent"] == "Europe" and i["language"] == "JavaScript")
    return sum(i["continent"] == "Europe" and i["language"] == "JavaScript" for i in lst)


list1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland',
        'continent': 'Europe', 'age': 19, 'language': 'JavaScript'},
    {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti',
        'continent': 'Oceania', 'age': 28, 'language': 'JavaScript'},
    {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan',
        'continent': 'Asia', 'age': 35, 'language': 'HTML'},
    {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan',
        'continent': 'Asia', 'age': 30, 'language': 'CSS'}
]

list2 = [
    {'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia',
        'continent': 'Oceania', 'age': 19, 'language': 'HTML'},
    {'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria',
        'continent': 'Europe', 'age': 89, 'language': 'HTML'}
]


print(count_developers(list1), 1)
print(count_developers(list2), 0)
