# [2559. Count Vowel Strings in Ranges](https://github.com/madiv9820/02_01_2025--2559_Count_Vowel_Strings_in_Ranges/tree/main) (All Approaches)

- ## Approach 1: Check For Each String One by One

    - ### Intuition
        The problem asks us to count how many words in a given range of indices in the list `words` start and end with a vowel. A word is considered a "vowel string" if both its first and last characters are vowels (i.e., one of 'a', 'e', 'i', 'o', 'u').

        Given multiple queries, each specifying a range `[left, right]` of indices, we need an efficient way to check if the words in the range start and end with vowels. Instead of repeatedly checking each word for each query, we preprocess the list of words to quickly determine which words are vowel strings, allowing us to answer each query efficiently.

    - ### Approach
        1. **Preprocess the List of Words**:
            - Create a boolean list `if_Vowel_String` where each entry corresponds to whether the corresponding word in `words` is a vowel string (True if it starts and ends with a vowel, otherwise False).
        
        2. **Answer the Queries**:
            - For each query, which contains a range `[left, right]`, count how many `True` values exist in `if_Vowel_String` within that range. This can be done by simply iterating through the range and counting the number of `True` values.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
                    // Create a set of vowels for quick lookup (both lowercase vowels)
                    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};   
                    
                    // A vector to store whether each word starts and ends with a vowel
                    vector<bool> if_Vowel_String(words.size(), false);

                    // Iterate over all words to check if they start and end with a vowel
                    for (int index = 0; index < words.size(); ++index) {
                        // Get the first and last character of the current word
                        char firstCharacter = words[index][0];
                        char lastCharacter = words[index][words[index].size() - 1];
                        
                        // Check if both the first and last characters are vowels
                        if (vowels.find(firstCharacter) != vowels.end() && 
                            vowels.find(lastCharacter) != vowels.end()) {
                            // If both are vowels, mark this word as a vowel string
                            if_Vowel_String[index] = true;
                        }
                    }

                    // A vector to store the results for each query
                    vector<int> vowel_String_Count;
                    
                    // Iterate over each query, which is a range [left, right]
                    for (vector<int>& query : queries) {
                        int left = query[0], right = query[1], count = 0;
                        
                        // Iterate through the words in the range [left, right]
                        for (int index = left; index <= right; ++index) {
                            // If the word at this index is a vowel string, increment the count
                            if (if_Vowel_String[index]) ++count;
                        }

                        // Push the count for this query to the result vector
                        vowel_String_Count.push_back(count);
                    }

                    // Return the final result with counts for each query
                    return vowel_String_Count;
                }
            };
            ```

    - ### Time Complexity
        1. **Preprocessing**:
            - We iterate over the list of words to determine whether each word starts and ends with a vowel. This takes **$O(n)$** time, where $n$ is the number of words.

        2. **Query Processing**:
            - For each query, we iterate through the range `[left, right]` and count how many `True` values exist in the `if_Vowel_String` list within that range. The time complexity for each query is **$O(k)$**, where $k$ is the length of the query range (`right - left + 1`).
            - If there are $m$ queries, the total time complexity for answering all queries is **$O(m \times k)$**, where $m$ is the number of queries and $k$ is the average query range length.

    - ### Space Complexity
        1. **`if_Vowel_String` List**:
            - We use a list of size $n$ to store whether each word is a vowel string, which takes **$O(n)$** space, where $n$ is the number of words.

        2. **Result List**:
            - We store the result for each query in a list, which requires **$O(m)$** space, where $m$ is the number of queries.

            Thus, the total space complexity is **$O(n+m)$**, where $n$ is the number of words and $m$ is the number of queries.

- - ## Approach 2: Prefix Sum

    - ### Intuition
        The task is to determine how many words, within a specific range of indices, start and end with a vowel. For each query, which provides a range `[left, right]`, we need to count how many words in that range satisfy the condition of starting and ending with a vowel.

        To make this process efficient, we preprocess the list of words and calculate a cumulative count of words that satisfy the condition (i.e., start and end with a vowel). Once this preprocessing is done, each query can be answered in constant time by using the cumulative count data.

    - ### Approach
        1. **Preprocessing Phase**:
            - We first iterate over the list of words and check if each word starts and ends with a vowel. We store this information in a boolean list (`if_Vowel_String`), where each entry is `True` if the word starts and ends with a vowel and `False` otherwise.
        
        2. **Prefix Sum Array**:
            - We construct a cumulative sum array (`vowel_String_Till_Index`), where each entry at index `i` represents the total number of vowel strings from index `0` to index `i`. This allows us to efficiently calculate the number of vowel strings in any range `[left, right]` by taking the difference `vowel_String_Till_Index[right] - vowel_String_Till_Index[left-1]`.
        
        3. **Query Processing**:
            - For each query, the result is computed in constant time by using the cumulative count array. For a query range `[left, right]`, we calculate how many vowel strings are in this range using the precomputed cumulative counts.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
                    // Create a set of vowels for quick lookup (both lowercase vowels)
                    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};   
                    
                    // A vector to store whether each word starts and ends with a vowel
                    vector<bool> if_Vowel_String(words.size(), false);

                    // Iterate over all words to check if they start and end with a vowel
                    for (int index = 0; index < words.size(); ++index) {
                        // Get the first and last character of the current word
                        char firstCharacter = words[index][0];
                        char lastCharacter = words[index][words[index].size() - 1];
                        
                        // Check if both the first and last characters are vowels
                        if (vowels.find(firstCharacter) != vowels.end() && 
                            vowels.find(lastCharacter) != vowels.end()) {
                            // If both are vowels, mark this word as a vowel string
                            if_Vowel_String[index] = true;
                        }
                    }

                    // A vector to store the cumulative count of vowel strings up to each index
                    vector<int> vowel_String_Till_Index(words.size(), 0);
                    
                    // Initialize the first element of the cumulative count array
                    vowel_String_Till_Index[0] = (if_Vowel_String[0]) ? 1 : 0;

                    // Fill the cumulative count array by summing up the number of vowel strings
                    for (int index = 1; index < words.size(); ++index) {
                        vowel_String_Till_Index[index] = vowel_String_Till_Index[index - 1] + 
                                                        ((if_Vowel_String[index]) ? 1 : 0);
                    }

                    // A vector to store the results for each query
                    vector<int> vowel_String_Count;
                    
                    // Iterate over each query, which specifies a range [left, right]
                    for (vector<int>& query : queries) {
                        int left = query[0], right = query[1]; 
                        
                        // Calculate the count of vowel strings in the range [left, right]
                        // The result is the difference between the cumulative counts at index `right` and `left-1`
                        // Special handling is done for when `left` is 0.
                        int count = vowel_String_Till_Index[right] - vowel_String_Till_Index[left] + 
                                    ((if_Vowel_String[left]) ? 1 : 0);
                        
                        // Append the count for this query to the result vector
                        vowel_String_Count.push_back(count);
                    }

                    // Return the final result with counts for each query
                    return vowel_String_Count;
                }
            };
            ```

    - ### Time Complexity
        1. **Preprocessing**:
            - The preprocessing phase involves checking each word to see if it starts and ends with a vowel. This takes **$O(n)$** time, where $n$ is the number of words.
            - After that, constructing the cumulative sum array takes **$O(n)$** time as well.

        2. **Query Processing**:
            - Each query is answered in **$O(1)$** time, since we simply take the difference between two values in the cumulative sum array.
            - If there are $m$ queries, answering all queries takes **$O(m)$** time.

            Thus, the total time complexity is **$O(n + m)$**, where $n$ is the number of words and $m$ is the number of queries.

    - ### Space Complexity
        1. **`if_Vowel_String` List**:
            - We need an auxiliary list `if_Vowel_String` of size $n$ to store whether each word starts and ends with a vowel. This takes **$O(n)$** space.

        2. **`vowel_String_Till_Index` List**:
            - We also need an auxiliary list `vowel_String_Till_Index` of size $n$ to store the cumulative count of vowel strings. This also takes **$O(n)$** space.

        3. **Result List**:
            - The result list `vowel_String_Count` stores the count for each query, which takes **$O(m)$** space, where $m$ is the number of queries.

            Thus, the total space complexity is **$O(n + m)$**, where $n$ is the number of words and $m$ is the number of queries.