from Solver import Solver


def solver(n, grid):
    """
    :param n: length of the n*n grid
    :param grid: n*n list
    :return: number of words
    """
    return Solver(n, grid).get_number_of_words()
