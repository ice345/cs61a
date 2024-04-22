HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if(n<8):
        return 0
    if(n%10!=8):
        return num_eights(n//10)
    if(n%10==8):
        return 1+num_eights(n//10)
"""
if n==0:
    return 0
last_digit =n%10
count=1 if last_digit==8 else 0
return count+num_eights(n//10)这种也行，但好像在这这里会在他的检测系统有些问题
之前我写的那个，没重复一次，total会自定义为0，这样根本计算不了
"""


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    total = 0
    if(n>=10):
        total=abs(n%10-n//10%10)
        return total+digit_distance(n//10)
    else:
        return total
    


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1 + 2^2 + 3 + 4^2 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1^2 + 2 + 3^2 + 4 + 5^2
    41
    >>> interleaved_sum(4, triple, square) # 1 * 3 + 2^2 + 3 * 3 + 4^2
    32
    >>> interleaved_sum(4, square, triple) # 1^2 + 2 * 3 + 3^2 + 4 * 3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    def interleaved_sum_1(term1, term2,k):
        if(n==k):
            return term1(k)
        return term1(k)+interleaved_sum_1(term2,term1,k+1)
    return interleaved_sum_1(odd_term,even_term,1)


def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(largestcoin,total):
        if total<0 or largestcoin==0 or largestcoin==None:
            return 0
        elif(total==0):
            return 1
        a=helper(largestcoin,total-largestcoin) #递归，你在这里开始调用函数，会直到你结束这次才开始下一个语句
        b=helper(next_smaller_coin(largestcoin),total)
        return a+b
    return helper(25,total)
"""
总体思路就是这个从大往小的理解好，例如30的硬币，你使用最大面值25，或不用就是下一层15，用了15
，剩下的面额通过下面的面额来凑，就是不断往下的意思吧，这整体思路就是通过一个函数搞出总的，以及最大
面额，然后层层往下，直到达到结束语句（就是base case），确实，total==0时就是你已经不用找了，就是
一种方法
"""

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    with_tower=2
    helper(n, start, with_tower,end)

def helper(n, start, with_tower,end):
    if(n>=1):
        helper(n-1,start,end,with_tower)
        print_move(start,end)
        helper(n-1,with_tower,start,end)





from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda g, k: k if k == 1 else mul(k, g(g, sub(k, 1))))
"""
这lambda其实就是套娃,你一个关系写不完就在lambda里面继续写,直到你写完关系了。
这里其实就是外部是里面(lambda f: lambda k: f(f, k))这个lambda表达式的一个参数,(其实就是作为关系函数f),而要传进第二个参数才能
调用这个表达式，第二个参数就是传进去的数字(例如5),这样里面的lambda表达式就可以实现递归f(f, k),通过这个
"""

