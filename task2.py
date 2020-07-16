number = float(input(" Please Enter any numeric Value : "))
square = number ** 2
print("The Square of a Given Number {0}  = {1}".format(number, square))




def test_square_number () :
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
#test_square_number()