def power(input_list):
    '''
    return square of number if even and cube of number of if odd
    '''
    output_list = []
    for num in input_list:
        if num % 2 == 0:
            output_list.append(num ** 2)
        else:
            output_list.append(num**3)
    return output_list


input_list = [25, 9, 8, 3, 6]

output_list = power(input_list)
print(output_list)

