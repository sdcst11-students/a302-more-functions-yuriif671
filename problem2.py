#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
    #if a2+b2>c2, the triangle is acute,
    #if a2+b2=c2, the triangle is a right triangle,
    #if a2+b2<c2, the triangle is obtuse,
def triangle(a, b, c):
    sa = pow(a, 2)
    sb = pow(b, 2)
    sc = pow(c, 2)

    if (a > c + b or b > a + c or c > a + b):
        return 0

    if (sa == sc + sb or sb == sa + sc or sc == sa + sb):
        return 2
    elif (sa > sc + sb or sb > sa + sc or sc > sa + sb):
        return 3
    elif (sa < sc + sb or sb < sa + sc or sc < sa + sb):
        return 1

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0

if __name__== "__main__":
    tests()