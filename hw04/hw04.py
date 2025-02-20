def filter(condition, lst):
    """Filters lst with condition using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"
    """    
    i=0
    while i<len(lst):
        if not condition(lst[i]):
            lst.pop(i)
        else:
            i+=1
    return lst
    """
    i=len(lst)-1
    while i>=0 :
        if not condition(lst[i]):
            lst.pop(i)
        i-=1
    return None
            



def deep_map_mut(func, lst):
    """Deeply maps a function over a list, replacing each item
    in the original list object.
    Does NOT return the mutated list object.

    >>> l = [1, 2, [3, [4], 5], 6]
    >>> deep_map_mut(lambda x: x * x, l)
    >>> l
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map_mut(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"

    """   
    wrong solution
    t=tree(lst[0],lst[1:])
    if is_leaf(t):
        func(label(t))
    else:
        func(label(t))
        for branch in branches(t):
            func(label(branch))
    """
    for i in range(len(lst)):
        if isinstance(lst[i],list):
            deep_map_mut(func,lst[i])
        else:
            lst[i]=func(lst[i])



HW_SOURCE_FILE=__file__


def max_path_sum(t):
    """Return the maximum root-to-leaf path sum of a tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) # 1, 10
    11
    >>> t2 = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
    >>> max_path_sum(t2) # 5, 2, 10
    17
    """
    "*** YOUR CODE HERE ***"
    lst=[]
    def new_max_path_sum(t,lst,total):
        if is_leaf(t):
            total+=label(t)
            lst.append(total)
        else:
            total+=label(t)
            for branch in branches(t):
                new_max_path_sum(branch,lst,total)
        return max(lst)
    return new_max_path_sum(t,lst,total=0)
            



HW_SOURCE_FILE=__file__


def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    
    def new_has_path(t,path,result):
        if is_leaf(t):
            path+=[label(t)]
            result.append("".join(path))
        else:
            path+=[label(t)]
            for branch in branches(t):
                return  new_has_path(branch,path,result)
        if len(word) == 1:
            return word==label(t)
        for i in result:
            if word not in i and word[0] != label(t):
                return  True
    return new_has_path(t,path=[],result=[])
    
    """    
def new_has_path(t, path):
        if is_leaf(t):
            return path == word
        else:
            path += label(t)
            for branch in branches(t):
                if new_has_path(branch, path):#还可以在这里递归，哎，真是
                    return True
            return False
    return new_has_path(t, '')
    """




def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """