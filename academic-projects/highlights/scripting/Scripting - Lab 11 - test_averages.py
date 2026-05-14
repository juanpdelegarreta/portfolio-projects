import pytest

def average(*nums):
    try:         
        for num in nums:
            if type(num)==int:
                continue
            else: 
                raise TypeError
    except TypeError:
        return "Error"
    else:
        return sum(nums)/len(nums)

def test_all_ints():
    assert average(1,3) == 2.0

#The following test will fail, as there is a check for an int type, and this attempt has floats. The other tests pass.
def test_floats_and_ints():
    assert average(1, 4.3, 5.9, 2) == 3.3
    
def test_bad_input():
    assert average("a", 3) == "Error"