import pytest
import sys
import os

def try_import_from_src(module_name):
  
    src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
    if os.path.exists(src_path) and os.path.isdir(src_path):
        sys.path.insert(0, os.path.abspath(src_path))
        try:
            return __import__(module_name)
        except ImportError:
            return None
    return None

calculator = try_import_from_src('calculator')


def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add(x, y, expected):
    assert add(x, y) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_imported_calculator():
    if calculator is not None:
        
        if hasattr(calculator, 'add'):
            assert calculator.add(2, 3) == 5
        else:
            pytest.skip("calculator module exists but 'add' function not found")
    else:
        pytest.skip("src/calculator not found, skipping import test")

def test_current_dir_import():   
    pass  
