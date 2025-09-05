# Write a Python program that uses a custom iterator to iterate over a list of integers.

# Custom Iterator Class
class MyIterator:
    def _init_(self, data):
        self.data = data
        self.index = 0

    def _iter_(self):
        return self  # iterator object

    def _next_(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# Using the custom iterator
numbers = [10, 20, 30, 40, 50]
my_iter = MyIterator(numbers)

for num in my_iter:
    print(num)