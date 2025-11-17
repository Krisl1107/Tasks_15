def even_list(num_list: list, count_list: int) -> list:
    """
    Recursively creates a list of even numbers from the input list.

    Args:
        num_list (list of int): The list of integers to process.
        count_list (int): The number of elements to consider from the list (initially the length of the list).

    Returns:
        list of int: A list containing all even numbers from the original list.
    """
    if count_list == 0:
        return []
    result = even_list(num_list, count_list - 1)
    if num_list[count_list - 1] % 2 == 0:
        result.append(num_list[count_list - 1])
    return result

def main():
    """
    Prompts the user to input a list of numbers, then finds and displays all even elements
    using a recursive function. Handles invalid input and recursion errors gracefully.
    """
    try:
        num_input = input("Enter numbers separated by spaces: ")

        num_input_list = num_input.split()
        num_list = [int(num) for num in num_input_list]

        print("Even elements:", even_list(num_list, len(num_list)))

    except ValueError:
        print("Invalid input, program terminated.")
    except RecursionError:
        print("Recursion error occurred.")

if __name__ == "__main__":
    main()
