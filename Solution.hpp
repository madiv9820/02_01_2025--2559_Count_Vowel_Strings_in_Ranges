#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

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