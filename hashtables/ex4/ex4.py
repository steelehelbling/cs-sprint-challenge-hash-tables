def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = [] 
    inside = {} 

    for number in a: 
        inside[number] = number

        if - number in inside and number is not 0:
            result.append(abs(number))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, 2, 1, -2, 3, 4,  -4, -8, -5, 2, 5, -3, -9, 9]))
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
