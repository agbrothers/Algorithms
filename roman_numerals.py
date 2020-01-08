# In 20 minutes, write a code that can convert integers to Roman numerals 
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


def conv_to_roman(x):
    ans = ''
    
    char = [ 'M', 'D', 'C', 'L', 'X','V', 'I']
    val  = [1000, 500, 100,  50,  10,  5,  1 ]
    
    while x > 0:
        
        for i in range(7):
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

    """
    RULES
    
    298   CCXCVIII
    999   CMXCIX
    
    *
    IF    ->    100 < x < 190
          ->    C + remainder

    IF    ->    90  ≤ x < 100
          ->    X + C + remainder
          
    *      
    IF    ->    50 ≤ x < 90
          ->    L + remainder

    IF    ->    40 ≤ x < 50
          ->    X + L + remainder  
          
     
    *      
    IF    ->    10 < x < 19
          ->    C + remainder

    IF    ->    9  ≤ x < 10
          ->    I + X + remainder
    
    
    X
    XX
    XXX
    XL
    L
    LX
    LXX
    LXXX
    XC
    CX
    CXX
    CXXX
    CXL
    CL
    CLX
    CLXX
    CLXXX
    CXC
    CC
    CCX
    
    
    I
    II
    III
    IV
    V
    VI
    VII
    VIII
    IX
    X
    XI
    XII
    XIII
    XIV
    XV
    XVI
    XVII
    XVIII
    XIX
    XX
    """