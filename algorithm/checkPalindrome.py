"""
정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오.
팰린드롬이란 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다.
단, 정수를 문자열로 바꾸면 안됩니다.
"""


def checkPalindrome(num):
    if num<0:
        return False
    
    num_each = []
    
    while not num==0:
        num_each.append(num%10)
        num /= 10
    
    left = 0
    right = len(num_each)-1
    
    while left<=right:
        if not num_each[left]==num_each[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

def checkPalindrome2(num):
    if num<0:
        return False
    
    i = 0
    left = 1
    while num>left:
        left *= 10
        i += 1
        
    right = 10
    
    while left>=10:
        l_val = (num%left)/(left/10)
        r_val = (num%right)/(right/10)
        
        if not l_val==r_val:
            return False
            
        left /= 10
        right *= 10
    
    return True
    
    
if __name__ == "__main__":
    while True:
        num = int(input())
        print(num)
        print(checkPalindrome(num))
        print(checkPalindrome2(num))
        
