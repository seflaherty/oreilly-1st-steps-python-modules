"""My module that is purposed to learn about modules!

🆒
"""

list_of_testing = [6, 5, 3, 1, 2, 4, 8, 6]


def solution(A):
    """From incoming array of INTs, return the first lowest positive INT not included in the array.
    """
    my_set = {i for i in A if i > 0}
    if not my_set:
        return 1
    else:
        for counter in range(1, len(my_set)+1):
            # print(f'counter value: {counter}')
            # print(counter in my_set)
            if counter in my_set:
                +counter
            else:
                break
        return counter