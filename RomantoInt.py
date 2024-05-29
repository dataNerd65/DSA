class Solution:
    def RomanToInt(self, s):
        #Defining the dctionary mapping Roman Numerals to their values.
        roman_to_int = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M': 1000
        }

        #Step 2: Initialize the total to 0.
        total = 0
        #Iterate through the strings
        length = len(s)
        for i in range(length):
            #If the current value is less than the next value, subtract it
            if i < length -1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            #Otherwise, add the current value
            else:
                total += roman_to_int[s[i]]

        #Step 4: Return the total value
        return total
    
solution = Solution()
print(solution.RomanToInt('MCMXCIV'))

