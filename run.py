from Solver import Solver


def solver(n, grid):
    '''
    >>> n = 3
    >>> grid = [['c', 'j', 'e'], ['e', 'a', 'o'], ['i', 't', 'e']]
    >>> solver(n, grid)
    42
    '''
    return Solver(n, grid).get_number_of_words()
