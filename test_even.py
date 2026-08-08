from even import is_even

def test_is_even_with_even_number():
	assert is_even(2) == True

def test_is_even_with_odd_numger():
	assert is_even(3) == False

def test_is_even_with_zero():
	assert is_even(0) == True

def test_is_even_with_negative_even():
	assert is_even(-2) == True

def test_is_even_with_negative_odd():
	assert is_even(-3) == False

def test_is_even_bad():
	assert is_even(-123.2) == False
