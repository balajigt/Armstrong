def is_armstrong(num):
    """
    Check if a number is an Armstrong number.
    
    Args:
        num (int): The number to be checked.
    
    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Count number of digits
    num_digits = len(str(num))
    
    # Compute the sum of nth power of its digits
    temp = num
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10
    
    # Check if the number is an Armstrong number
    return num == armstrong_sum

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_armstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")
