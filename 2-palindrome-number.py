"""
Palindrome Number

Given an integer x, return true if x is a palindromeand false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        number = str(x)
        lenght= len(number)
        
        print(lenght)
        print(lenght // 2)
        
        for i in range(lenght // 2):
            print(number[i])
            print(number[lenght - i - 1])
            if number[i] != number[lenght - i - 1]: # 0 != 3
            
                return False
            
        return  True
        

if __name__ == "__main__":
    x = 133
    print(Solution().isPalindrome(x))