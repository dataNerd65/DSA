class Solution(object):
    def isValid(self, s):
        #dictionary to map closing bracket to opening bracket
        bracket_map = {')':'(', '}':'{', ']':'['}
        #Initializing a stack to keep track of opening braces
        stack = []

        for char in s:
            if char in bracket_map: #if is a closing brace
                #pop from the stack if its not empty, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'

                #Check if the popped element is the correct opening brace
                if bracket_map[char] != top_element:
                    return False
                
            else:
                #If an opening brace push it onto a stack
                stack.append(char)

        #check if stack is empty at the end
        return not stack
    
soln = Solution()
print(soln.isValid("()"))
print(soln.isValid("()[]{}"))
print(soln.isValid("[)"))
