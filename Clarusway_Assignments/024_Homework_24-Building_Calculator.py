"""
Building a Calculator using dict with lambda expression
"""

calculator = {"+": (lambda x, y: x + y),
              "-": (lambda x, y: x - y),
              "/": (lambda x, y: x / y),
              "*": (lambda x, y: x * y)}

calculator["+"](3, 5)
