class Solution:
    def isValid(self, s):
        #Dictionary to map closing brace to opening brace
        bracket_map = {')':'(', '}':'{', ']':'['}
        
        #A stack to store the parentheses
        #In our case we will use the stack cause of its Last-in-First-in principle
        stack = []

        for char in s:
            if char in bracket_map: #If its a closing bracket
                #pop from stack if its not empty otherwise use a dummy value '#'

                top_element = stack.pop() if stack else '#'

                #check if the popped element is the correct opening bracket
                if bracket_map[char] != top_element:
                    return False
                
            else:
                #It's an opening brace, push it onto the stack
                stack.append(char)

        #Check if stack is empty at the end
        return not stack
    
soln = Solution()
print(soln.isValid("()"))
print(soln.isValid("()[]{}"))
print(soln.isValid("[)"))