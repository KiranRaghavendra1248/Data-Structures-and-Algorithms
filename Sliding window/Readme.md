# Sliding Window :
# Modified Hashmap Sliding window algorithm: 
Instead of generating the hashmap afresh for every window considered, we can create the hashmap just once for the first window . Then, later on when we slide the window, we know that we remove one preceding character and add a new succeeding character to the new window considered. Thus, we can update the hashmap by just updating the indices associated with those two characters only. Sliding windows can be of two types. 

**Fixed length sliding windows :**
When we have to find something like, find if string A is a substring of string B OR find if any permutations of string A is a substring of string B etc etc. It can be used in substring based questions.

**Varying length substrings :** 
When we have to find the length of the smallest substring of B that consists of all characters in string A etc
