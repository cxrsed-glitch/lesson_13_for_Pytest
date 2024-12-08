from functions import salary,hello_who


def test_hello_who_max():
    assert hello_who('Max') == 'Hello,Max'




def test_salary():
    assert(2,2) != 8
    assert(3,1) != 6