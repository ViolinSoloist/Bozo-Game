import random

random.seed(10)
for _ in range(10):
    print(random.random())
random.seed()
print()
for _ in range(10):
    print(random.random())