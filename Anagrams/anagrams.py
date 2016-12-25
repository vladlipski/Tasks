def get_anagrams(word):
    if len(word) <= 1:
        return word
    else:
        result = []
        for anagram in get_anagrams(word[1:]):
            for i in range(len(word)):
                result.append(anagram[:i] + word[0:1] + anagram[i:])
        return result

print (get_anagrams("biro"))