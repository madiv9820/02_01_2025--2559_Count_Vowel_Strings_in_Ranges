from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Define the set of vowels for quick lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Create a list `if_Vowel_String` that will store whether each word
        # starts and ends with a vowel. Each entry will be True or False.
        # The list comprehension checks if the first and last characters of each word are vowels.
        if_Vowel_String = [
            True if word[0] in vowels and word[-1] in vowels else False 
            for word in words
        ]
        
        # Initialize an empty list to store the result for each query
        vowel_String_Count = []
        
        # Iterate through each query (which contains a range [l, r])
        for l, r in queries:
            count = 0  # Initialize count for the current query range
            
            # Loop through the indices in the range [l, r] (inclusive)
            for i in range(l, r + 1):
                # If the word at index i starts and ends with vowels, increment the count
                if if_Vowel_String[i]:
                    count += 1
            
            # Append the count for this query to the result list
            vowel_String_Count.append(count)

        # Return the list of counts for each query
        return vowel_String_Count