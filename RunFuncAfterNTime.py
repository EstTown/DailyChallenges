# Implement a job scheduler which takes in a function f and an integer n, 
# and calls f after n milliseconds.
from time import sleep

def schedule(func, args, delay):
    sleep(delay/1000)
    func(args)

def someFunc(arg):
    print("Executing function...")
    print(arg)

# Schedule the function, to run after 2 seconds
schedule(someFunc, "hello", 2000)