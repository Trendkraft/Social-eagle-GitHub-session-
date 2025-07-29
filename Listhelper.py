def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Main block to test the functions
if __name__ == "__main__":
    # Input: list of numbers from user
    input_str = input("Enter numbers separated by spaces: ")
    number_list = [float(num) for num in input_str.split()]

    print(f"List: {number_list}")
    print(f"Maximum: {find_max(number_list)}")
    print(f"Minimum: {find_min(number_list)}")
    print(f"Sum: {calculate_sum(number_list)}")
    print(f"Average: {calculate_average(number_list)}")
