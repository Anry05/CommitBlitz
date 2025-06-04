from src.main import greet
def test_greet():
 assert greet('Anry') == 'Hello, Anry'

def test_add():
  assert add(2,3) == 5

def test_substract():
  assert substract(5, 2) == 3

def test_multiply():
  assert multiply(3, 4) == 12

def test_divide():
 assert divide(10, 2) == 5

def test_divide_zero():
 assert divide(5, 0) == 'Cannot divide by zero'

def test_square():
 assert square(4) == 16
