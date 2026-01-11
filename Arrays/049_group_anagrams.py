#here, cant use the technique of single anagram
#in single anagram the length of both words can be checked but, here it cannot be checked
#set cannot be used here, (for eg. "aab" and "ab" produce same set but their length is differenr) and hence tuple is used which is sorted (for same order of letters) and it act as the key.
#whichever str get the same order of letters it is mapped with the key
#to store multiple words, a defaultdict(list) is used. (for eg. (a,e,t)->["eat","ate","tea"]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash=defaultdict(list)
        for i in strs:
            key=tuple(sorted(i))
            hash[key].append(i)
        return list(hash.values())    

        