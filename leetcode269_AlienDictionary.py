""" 
Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

You may assume all letters are in lowercase.
The dictionary is invalid, if string a is prefix of string b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order.
The letters in one string are of the same rank by default and are sorted in Human dictionary order.
Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"

"""


from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(words: List[str]) -> str:
        """ 
        This line initializes a dictionary named adj. Each character c in each word w is added as a key in the dictionary with an empty set as its value. This dictionary will be used to represent the adjacency relationships between characters.
        """
        adj = { c:set() for w in words for c in w }
        
        """ 
        This block of code iterates through adjacent pairs of words in the words list. It compares each corresponding character in the current word w1 with the next word w2 to determine their ordering relationship.

If the length of w1 is greater than w2 and the shared prefix of w1 and w2 is equal, it means that the ordering is invalid. In such a case, an empty string is returned.
Otherwise, it finds the first differing character between w1 and w2 and adds an adjacency relationship between them in the adj dictionary.
        """
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                
                """ 
                These lines initialize an empty dictionary visit and an empty list res. These variables will be used in the depth-first search (DFS) algorithm that follows.
                """
            visit = {}
            res = []
            
            """ 
            This code defines a recursive helper function dfs that performs a depth-first search on the characters in the adj dictionary. The function takes a character c as input and performs the following steps:

If the character c has already been visited, it returns the corresponding value from the visit dictionary.
It marks the character c as visited by setting visit[c] = True.
It recursively calls dfs on each neighbor (nei) of c in the adj dictionary.
If a cycle is detected during the DFS traversal, it returns True.
After visiting all neighbors, it marks the character c as unvisited (visit[c] = False) and appends it to the res list.
            """
            def dfs(c):
                if c in visit:
                    return visit[c]
                
                visit[c] = True
                for nei in adj[c]:
                    if dfs(nei):
                        return True
                visit[c] = False
                res.append(c)
                
            for c in adj:
                if dfs(c):
                    return ""
            res.reverse()
            return "".join(res)