from main import *



## Feel free to add your own tests here.
def test_multiply():
    
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
    assert quadratic_multiply(BinaryNumber(12), BinaryNumber(4)) == 12 * 4
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(9)) == 8 * 9
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(15)) == 10 * 15
    assert quadratic_multiply(BinaryNumber(20), BinaryNumber(20)) == 20 * 20