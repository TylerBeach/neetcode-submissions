class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # convert every word into a dict and append the word if the key is in the dict else we add it to the dict


        ans_dict = defaultdict(list)


        for word in strs:
            letter_array = [0] * 26  # this is an array of 26 0's for the count of each letter
            for letter in word:
                letter_array[ord(letter) - ord("a")] += 1  # "a" - "a" = 0     "b" - "a" = 1 ... etc -> add for each one

            # word is finished we can add the word to that key in the ans_dict]
            ans_dict[tuple(letter_array)].append(word)
        
        # return the values in the dict only 
        return ans_dict.values()

