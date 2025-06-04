from src.main import greet
def test_greet():
 assert greet('Anry') == 'Hello, Anry'

def test_add():
  assert add(2,3) == 5

def test_substract():
  assert substract(5, 2) == 3
