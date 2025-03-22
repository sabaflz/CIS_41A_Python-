# CIS 41A
# ch12, ex2
# Saba Feilizadeh
# Create Fibonacci numbers (1, 1, 2, 3, 5, 8, etc.)
# using an iterator and a generator (Both).

# Iterator implementation
class FibonacciIterator:
    """
    An iterator class that generates Fibonacci numbers up to a specified limit.
    
    Attributes:
        limit (int): The maximum number of Fibonacci numbers to generate
        count (int): Current count of numbers generated
        a (int): Previous number in the sequence
        b (int): Current number in the sequence
    """
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return 1
        if self.count == 1:
            self.count += 1
            return 1
        
        result = self.a + self.b
        self.a = self.b
        self.b = result
        self.count += 1
        return result
# ------------------------------------------------------ 
# Generator implementation
def fibonacci_generator(limit):
    """
    A generator function that yields Fibonacci numbers up to a specified limit.
    
    Args:
        limit (int): The maximum number of Fibonacci numbers to generate
    
    Yields:
        int: The next Fibonacci number in the sequence
    """
    a, b = 0, 1
    count = 0
    while count < limit:
        if count == 0 or count == 1:
            yield 1
        else:
            c = a + b
            yield c
            a = b
            b = c
        count += 1
# ------------------------------------------------------ 
def get_valid_input():
    """
    Gets valid input from the user for the number of Fibonacci numbers to generate.
    
    Returns:
        int: A positive integer representing the number of Fibonacci numbers to generate
    """
    limit = 0
    while limit <= 0:
        try:
            limit = int(input("How many Fibonacci numbers would you like to generate? "))
            if limit <= 0:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid integer!")
    return limit

def main():
    """
    Main function to demonstrate both iterator and generator implementations
    of the Fibonacci sequence using valid user input.
    """
    limit = get_valid_input()
    
    print("\nUsing Iterator:")
    fib_iterator = FibonacciIterator(limit)
    for num in fib_iterator:
        print(num, end=" ")
    
    print("\n\nUsing Generator:")
    fib_generator = fibonacci_generator(limit)
    for num in fib_generator:
        print(num, end=" ")
    print("\n")
# ------------------------------------------------------ 
if __name__ == "__main__":
    main()
# ------------------------------------------------------ 
'''
========================================================
Output 1:
========================================================
How many Fibonacci numbers would you like to generate? 11

Using Iterator:
1 1 1 2 3 5 8 13 21 34 55 

Using Generator:
1 1 1 2 3 5 8 13 21 34 55 
========================================================
Output 2:
========================================================
How many Fibonacci numbers would you like to generate? a
Please enter a valid integer!
How many Fibonacci numbers would you like to generate? -3
Please enter a positive number!
How many Fibonacci numbers would you like to generate? 6

Using Iterator:
1 1 1 2 3 5 

Using Generator:
1 1 1 2 3 5 
'''