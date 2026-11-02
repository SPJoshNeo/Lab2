import Lab2 as x

def test_find_min_max():
    expected_result=[1.0,3.0]
    Num_List=[1.0, 2.0, 3.0]
    result=x.find_min_max(Num_List)
    assert (result==expected_result)

def test_calc_ave():
    Num_List=[1.0,2.0,3.0]
    expected_result=2.0
    result = x.calc_average(Num_List)
    assert (result==expected_result)

def test_median_temperature():
    Num_List=[1.0,2.0,3.0,4.0,5.0]
    expected_result=3.0
    result = x.calc_median_temperature(Num_List)
    assert (result==expected_result)