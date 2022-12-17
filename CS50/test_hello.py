from hello_1 import hello

def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Hermione", "Harry", "ROn"]:
        assert hello(name) == f"hello, {name}"

# test_argument()