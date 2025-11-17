def ind_maxlist(num_list: list, index=0, max_index=0) -> int:
    """
    Recursively finds the index of the maximum element in a list of numbers.

    Args:
        num_list (list of int): The list of integers to search.
        index (int, optional): The current index in the recursion. Defaults to 0.
        max_index (int, optional): The index of the current maximum element found so far. Defaults to 0.

    Returns:
        int or None: The index of the maximum element in the list, or None if the list is empty.
    """
    if len(num_list) == 0:
        return None
    if index == len(num_list):
        return max_index
    if num_list[index] > num_list[max_index]:
        max_index = index
    return ind_maxlist(num_list, index + 1, max_index)

def main():
    """
    Prompts the user to input a list of numbers separated by spaces,
    then finds and displays the index of the maximum element using recursion.
    Handles invalid input and recursion errors gracefully.
    """
    try:
        num_input = input("Enter numbers separated by spaces: ")

        num_input_list = num_input.split()
        num_list = [int(num) for num in num_input_list]

        print("Index of the maximum element:", ind_maxlist(num_list))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
