def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    print("Sum:", add(5, 7))
