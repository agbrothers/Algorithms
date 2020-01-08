# Coding Challenge: In 20 minutes, write an algorithm that can convert integers to Roman Numerals 
# from 1 through 1000, where
# 
#  I = 1
# IV = 4
#  V = 5
# IX = 9
#  X = 10
# XI = 11
#  L = 50
#  C = 100
#  D = 500
#  M = 1000

# IDEA - Iteratively add characters to our roman numeral string while reducing the integer value of our input
def conv_to_roman(x):
    ans = ''
    
    char = [ 'M', 'D', 'C', 'L', 'X','V', 'I']
    val  = [1000, 500, 100,  50,  10,  5,  1 ]
    
    while x > 0:
        
        for i in range(len(char)):
            if x >= val[i]:
                x -= val[i]
                ans += char[i]
                break
                
            elif i%2 == 0 and x < val[i] and x >= val[i] - val[i+2]:
                x -= val[i] - val[i+2]
                ans += char[i+2] + char[i]
                break
                
            elif i%2 == 1 and x < val[i] and x >= val[i] - val[i+1]:
                x -= val[i] - val[i+1]
                ans += char[i+1] + char[i]
                break
    
    return(ans)
    
    # Runtime ~ O(nm)
    # where n = 7, the number of numerals we have
    #       m = number of reductions to get x to 0
