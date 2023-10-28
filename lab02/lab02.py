
def composer(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> a1 = composer(square, add_one)   # (x + 1) ** 2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = composer(mul_three, a1)     # ((x + 1) ** 2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    a=composer(f,g)
    b=composer(g,f)
    def h(x):
        if (a(x)==b(x)):
            return True
        else:
            return False
    return h


def sum_digits(y):
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***" 
    def g(n):
        sum,i=0,1
        while(i<=n):
            if(condition(n,i)):
                sum+=1
                i+=1
            else:
                i+=1
        return sum
    return g


def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    k=a
    l=b
    if(a>b):
        while(b!=0):
            c=a%b
            a=b
            b=c
        d=(k*l)//a
        return d
    elif(a<b):
        while(a!=0):
            c=b%a
            b=a
            a=c
        d=(k*l)//b
        return d
    return d




def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"

    def h(k):
        def g(x):
            if(k>=3):
                a=k//3
                while(a>0):
                    x=f1(x)
                    x=f2(x)
                    x=f3(x)
                    a-=1
                if(k%3==1):
                    x=f1(x)
                elif(k%3==2):
                    x=f1(x)
                    x=f2(x)
                return x
            elif(k<3&k>0):
                if(k%3==1):
                    x=f1(x)
                    return x
            elif(k%3==2):
                    x=f1(x)
                    x=f2(x)
                    return x
            elif(k==0):
                return x
            return x
        return  g
    return h
"""
#alternative choice
def h(k):
        def g(x):
            if(k==0):
                return x
            i=1
            while(i<=k):
                if(i%3==1):
                    x=f1(x)
                if(i%3==2):
                    x=f2(x)
                if(i%3==0):
                    x=f3(x)
                i+=1
            return x
        return g
    return h
"""
        
                    

            







        
        

    


