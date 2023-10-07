def f(x):
    return x

# from now on I will use if __name__ == '__main__' to start the main part of the script.
# it looks cryptic for now, but later when you learn about import and modules it will be clear.
# here, using if __name__ == '__main__' is just a convention.
if __name__ == '__main__':
    print(f) # function f: takes x, which can be any data types, and returns exactly the same x
    print(f(f)) # function f: takes f, which is a function, and returns exactly the same function f, you
                # can see that the two printing results are the same: <function f at ...>, thus f and f(f) are
                # the same object in your computer memory
    print(f(3)) # function f: takes 3, which is an integer, and returns 3
    print(f(f)(f(3))) # let's parse the syntax: [ f(f) ] (f(3)) -> [f] (f(3)) -> f( [f(3)] ) -> f( [3] ) -> f(3) -> 3,
                # so f(3) and f(f)(f(3)) give the same results. if you print(id(f(3)), id(f(f)(f(3)))), you
                # will see that they refer to the same object in your computer memory
