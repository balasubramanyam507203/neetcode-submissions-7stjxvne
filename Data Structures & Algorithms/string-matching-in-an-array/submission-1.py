class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        words.sort(key=len) #as #mass #hero #superhero
        res = [] #as
        for i in range(len(words)): 
            word = words[i] #as
            for j in range(i + 1, len(words)): #mass
                if word in words[j]:
                    res.append(word)
                    break
        return res

        