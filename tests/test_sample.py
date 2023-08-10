# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()

def hello_func(name: str):
    return f"Hello, {name}!"


def test_answer():
    assert hello_func('Todd') == "Hello, Todd!"
