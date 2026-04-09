class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word.lower()))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word.lower())
        return [anagrams[key] for key in anagrams]

