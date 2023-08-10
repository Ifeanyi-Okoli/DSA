"""
You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return:

true if at least one Ruby developer has signed up; or
false if there will be no Ruby developers.
For example, given the following input array:

list1 = [
    { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
    { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
    { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
    ] 
"""


def is_ruby_coming(lst):
    # your code here
    return any(d['language'] == 'Ruby' for d in lst)


list1 = [
    {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina',
        'continent': 'Americas', 'age': 35, 'language': 'Java'},
    {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia',
        'continent': 'Europe', 'age': 35, 'language': 'Python'},
    {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States',
        'continent': 'Americas', 'age': 32, 'language': 'Ruby'}
]
print(is_ruby_coming(list1), True)

list2 = [
    {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina',
        'continent': 'Americas', 'age': 35, 'language': 'Java'},
    {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia',
        'continent': 'Europe', 'age': 35, 'language': 'Python'}
]
print(is_ruby_coming(list2), False)
