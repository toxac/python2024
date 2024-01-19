def binaryConverter (num: int) -> list:
    """outputs binary for a given integer

    """
    output = []
    while num >= 1:
        # insert value at beginning to the list
        output.insert(0, num % 2) 
        num = num // 2
    
    return output


print(binaryConverter(591))