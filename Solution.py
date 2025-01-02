from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Define the set of vowels for quick lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Create a list `if_Vowel_String` that stores whether each word
        # starts and ends with a vowel. Each entry will be True or False.
        # The list comprehension checks if the first and last characters of each word are vowels.
        if_Vowel_String = [
            True if word[0] in vowels and word[-1] in vowels else False 
            for word in words
        ]
        
        # Initialize the `vowel_String_Till_Index` list to store the cumulative count
        # of vowel strings up to each index. This list helps to answer range queries efficiently.
        vowel_String_Till_Index = [0] * len(words)
        
        # For the first word, we directly set whether it is a vowel string or not
        vowel_String_Till_Index[0] = 1 if if_Vowel_String[0] else 0

        # Compute the cumulative count of vowel strings up to each index
        for index in range(1, len(words)):
            vowel_String_Till_Index[index] = vowel_String_Till_Index[index-1] + (1 if if_Vowel_String[index] else 0)

        # Initialize an empty list to store the result for each query
        vowel_String_Count = []
        
        # Iterate through each query (which contains a range [l, r])
        for l, r in queries:
            # For each query, compute the number of vowel strings in the range [l, r].
            # This is done using the difference of cumulative counts: 
            # (vowel_String_Till_Index[r] - vowel_String_Till_Index[l]) 
            # gives the count in the range [l, r]. We also need to handle the case when l is 0.
            count = vowel_String_Till_Index[r] - vowel_String_Till_Index[l] + (1 if if_Vowel_String[l] else 0)
            
            # Append the result of the query to the `vowel_String_Count` list
            vowel_String_Count.append(count)

        # Return the list of counts for all queries
        return vowel_String_Count
