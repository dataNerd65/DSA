class Solution:
    def word_pattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
                
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
                

            char_to_word[char] = word
            word_to_char[word] = char

        return True
    
soln = Solution()
print(soln.word_pattern("abba", "dog cat cat dog"))
print(soln.word_pattern("abba", "dog cat cat fish"))
print(soln.word_pattern("aaaa", "dog cat cat dog"))
