from dns.dnssec import validate
import pytest

def test_example():
    assert 3==3

def test_example2():
    assert isinstance("This is an example sentence", str)
    assert not isinstance("This is an example sentence", int)

def test_example3():
    validated = True
    assert validated is True
    assert isinstance("This is an example sentence", str) is True

class Student:
    def __init__(self, first_name:str, last_name:str, major: str, year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year

def test_student_initialization(default_student):
    #p = Student(first_name="John", last_name="Smith", major="A", year=2020)
    assert default_student.first_name == "John"
    assert default_student.last_name == "Smith"
    assert default_student.major == "A"
    assert default_student.year == 2020

@pytest.fixture(scope="module")
def default_student():
    return Student("John", "Smith", "A", 2020)