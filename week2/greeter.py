# prints __main__ as executed in main
# print(__name__)

def greet():
    print(a)
    print("Hello, World")

"""
# this is an executable but you can't call it in main.py as name is "greeter" in main
if __name__ == '__main__':
    a = 42
    greet()
"""

# fixed by define main
def main():
    a = 42
    greet()

if __name__ == '__main__':
    greet()