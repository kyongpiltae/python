

import unittest
#https://hsp1116.tistory.com/33
# 분해 , 자연어표현 , 구현/수정보완 , 평가
# 특성 
'''
입/출력 , 
명확성, 
유한성, 
효율성 : 시간,공간
'''


input = [1,10,30,50,60,2,7,8]
print(input)

#Time complexity (O(N^2))
#space complextity O(N)

def swap(input,start=0):
    i=start
    temp = input[i]
    input[i] = input[i+1]
    input[i+1] = temp




def selection(input):
    N=len(input)
    print([*range(N)])
    for i in range(N):
        temp = input[i]
        for j in range(i,N):
            if(input[j] < temp ):
                temp1 = temp
                temp = input[j]
                input[j] = temp1
                print(input)
        input[i] = temp
    return input

                
            
    pass

# bubule
def buble(input):
    N= len(input)
    print("size = {0} ".format(N))
    print(input)
    for start in range(N):
        for i in range(N-1):
            print(i)
            if( input[i] > input[i+1]):
                swap(input,i)
    print(input)
    return input
    
#insertion
def insertion(input):
    pass



#complexity (O(NlogN))
#merge
#quick
# heap

# Linear Time
#complexity (O(N))

output=selection(input[:])
print(output[:])

