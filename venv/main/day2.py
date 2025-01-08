def is_safe(report):

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are between -3 and -1 (decreasing) or 1 and 3 (increasing)
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


def count_safe_reports(file_path):

    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1
    return safe_count


# File path to the input data
file_path = 'input.txt'

# Calculate and print the number of safe reports
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")


def is_safe(report):

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are between -3 and -1 (decreasing) or 1 and 3 (increasing)
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


def count_safe_reports(file_path):

    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1
    return safe_count


if __name__ == '__main__':
    # File path to the input data
    file_path = 'input.txt'

    # Calculate and print the number of safe reports
    safe_reports = count_safe_reports(file_path)
    print(f"Number of safe reports: {safe_reports}")

#second pazzle

def is_safe(report):

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are between -3 and -1 (decreasing) or 1 and 3 (increasing)
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


def is_safe_with_dampener(report):

    if is_safe(report):
        return True

    # Try removing each level and check if it becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False


def count_safe_reports_with_dampener(file_path):

    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1
    return safe_count


if __name__ == '__main__':
    # File path to the input data
    file_path = 'input.txt'

    # Calculate and print the number of safe reports with the Problem Dampener
    safe_reports = count_safe_reports_with_dampener(file_path)
    print(f"Number: {safe_reports}")