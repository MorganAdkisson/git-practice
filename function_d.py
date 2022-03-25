def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    max = numbers[2]

    for num in numbers:
        if num > max:
            max = num

    return max
=======
    return max(numbers)
>>>>>>> 1e34030df25ae0b9b726a2d80956871ea891ab51


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
