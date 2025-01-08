import re

# Function to process the input file and calculate the sum of valid mul results
def calculate_mul_sum(file_path):
    try:
        with open(file_path, 'r') as file:
            corrupted_memory = file.read()

        # Define regex for valid mul instructions
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

        # Find all matches in the corrupted memory
        matches = re.findall(pattern, corrupted_memory)

        # Calculate the sum of all valid multiplication results
        total_sum = sum(int(x) * int(y) for x, y in matches)

        return total_sum
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == '__main__':
    file_path = "input.txt"  # Replace with your actual input file path
result = calculate_mul_sum(file_path)
if result is not None:
    print(f"The sum of all valid multiplication results is: {result}")



# Function to process the input file and calculate the sum of valid mul results with conditional handling
def calculate_mul_sum(file_path):
    try:
        with open(file_path, 'r') as file:
            corrupted_memory = file.read()

        # Define regex patterns
        mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        do_pattern = r"do\(\)"
        dont_pattern = r"don't\(\)"

        # Split the memory into segments based on instructions
        instructions = re.split(f"({do_pattern}|{dont_pattern})", corrupted_memory)

        # Initialize variables
        mul_enabled = True
        total_sum = 0

        # Process each segment
        for instruction in instructions:
            instruction = instruction.strip()

            # Check for enable/disable instructions
            if re.fullmatch(do_pattern, instruction):
                mul_enabled = True
            elif re.fullmatch(dont_pattern, instruction):
                mul_enabled = False
            else:
                # Process valid mul instructions if enabled
                if mul_enabled:
                    matches = re.findall(mul_pattern, instruction)
                    total_sum += sum(int(x) * int(y) for x, y in matches)

        return total_sum
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == '__main__':
    file_path = "input.txt"  # Replace with your actual input file path
result = calculate_mul_sum(file_path)
if result is not None:
    print(f"The sum of all valid multiplication results is: {result}")


def count_x_mas_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            grid = [list(line.strip()) for line in file.readlines()]

        rows = len(grid)
        cols = len(grid[0])

        # Define the pattern of an X-MAS
        def is_x_mas(x, y):
            # Check boundaries for both diagonals
            if not (0 <= x - 1 < rows and 0 <= x + 1 < rows and 0 <= y - 1 < cols and 0 <= y + 1 < cols):
                return False

            # Check X-MAS pattern top-left to bottom-right diagonal
            if (
                    grid[x - 1][y - 1] == 'M' and grid[x][y] == 'A' and grid[x + 1][y + 1] == 'S' and
                    grid[x - 1][y + 1] == 'M' and grid[x + 1][y - 1] == 'S'
            ):
                return True

            # Check X-MAS pattern top-right to bottom-left diagonal
            if (
                    grid[x - 1][y - 1] == 'S' and grid[x][y] == 'A' and grid[x + 1][y + 1] == 'M' and
                    grid[x - 1][y + 1] == 'S' and grid[x + 1][y - 1] == 'M'
            ):
                return True

            return False

        count = 0
        # Traverse the grid
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if is_x_mas(i, j):
                    count += 1

        return count
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == '__main__':

    file_path = "input.txt"  # Replace with your actual input file path
result = count_x_mas_occurrences(file_path)
if result is not None:
    print(f"The pattern 'X-MAS' appears {result} times in the grid.")
