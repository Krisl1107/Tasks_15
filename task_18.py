def simmetr(string: str, ind_min: int, ind_max: int) -> bool:
    """
    Recursively checks whether the substring of 'string' 
    from index 'ind_min' to 'ind_max' is a palindrome.

    Args:
        string (str): The string in which to check the substring.
        ind_min (int): The starting index of the substring.
        ind_max (int): The ending index of the substring.

    Returns:
        bool: True if the substring is symmetric (a palindrome), False otherwise.
    """
    if ind_min >= ind_max:
        return True
    if string[ind_min] != string[ind_max]:
        return False
    return simmetr(string, ind_min + 1, ind_max - 1)

def main():
    """
    Prompts the user to input a string and indices, then checks
     whether the specified substring is a palindrome.
    Handles invalid inputs and recursion errors gracefully.
    """
    try:
        str_input = input("Enter your string: ")
        ind_min_input = input("Enter min index: ")
        ind_max_input = input("Enter max index: ")

        ind_min = int(ind_min_input)
        ind_max = int(ind_max_input)

        result = simmetr(str_input, ind_min, ind_max)
        print("Result:", result)

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")
        
        
if __name__ == "__main__":
    main()
