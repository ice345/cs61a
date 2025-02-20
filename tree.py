def tree(root_label, branches=[]):
        for branch in branches:
                assert is_tree(branch), 'branches must be trees'
        return [root_label] + list(branches)


def label(tree):
        return tree[0]


def is_tree(tree):
        if type(tree) != list or len(tree) < 1:
                return False
        for branch in branches(tree):
                if not is_tree(branch):
                        return False
        return True


def branches(tree):
        return tree[1:]


def is_leaf(tree):
        return not branches(tree)



def count_leaves(tree):
        if is_leaf(tree):
                return 1
        else:
                branch_counts = [count_leaves(b) for b in branches(tree)]
                return sum(branch_counts)
def fib_tree(n):
        if n == 0 or n == 1:
                return tree(n)
        else:
                left, right = fib_tree(n-2), fib_tree(n-1)
                fib_n = label(left) + label(right)
                return tree(fib_n, [left, right])
def print_parts(tree, partition=[]):
        if is_leaf(tree):
                if label(tree):
                        print(' + '.join(partition))
        else:
                left, right = branches(tree)
                m = str(label(tree))
                print_parts(left, partition + [m])
                print_parts(right, partition)