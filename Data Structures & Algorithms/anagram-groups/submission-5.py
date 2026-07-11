class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for word in strs:
            sorted_words = " ".join(sorted(word))
            if sorted_words not in group:
                group[sorted_words] = []
            group[sorted_words].append(word)
        return list(group.values())                

            
            
        