def sum_array(array):
    '''Return sum of all items in array'''
    n = len(array)-1
    if n == 0:
        return array[n]
    return array[n] + sum_array(array[:n])



def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    '''Return n!'''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def reverse(word):
    '''Return word in reverse'''
    if len(word) == 0:
        return word ##word must be a string
    else:
        return reverse(word[1:]) + word[0]
