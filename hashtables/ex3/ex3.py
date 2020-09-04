def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    inside = {}
    for list_array in arrays:
        for array in list_array:
            if array in inside:
                inside[array] = inside[array] + 1
            else:
                inside[array] = 1
    result = [item for item in inside.keys() if inside[item] == len(arrays)]
    return result


if __name__ == "__main__":
    result = intersection([
                [1,2,3],
                [1,4,5,3],
                [1,6,7,3]
    ])
    print(result)
    result.sort()
    print(result) 

    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
