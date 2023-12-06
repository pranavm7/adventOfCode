import re


# Solution for Advent of Code 2023 Day 1 

# For a given string, return a digit made up of first and last digits
def soln( input : str ) -> int:
    digits = re.findall(r'\d', input)
    # if no digits, return 0
    if len(digits) == 0:
        return 0
    # if only one digit, new digit is the same digit twice
    if len(digits) == 1:
        return int(f'{digits[0]}{digits[0]}')
    # otherwise, return first and last digits
    return int(f'{digits[0]}{digits[-1]}')
    pass


# Read the input and return the contents as a list of strings
def getInput():
    with open('../input.txt', 'r') as f:
        return f.read().splitlines()
    pass

# Format output (Print all the answers, and metadata, plus sum total of the answers)
def formatOutput( input : list[str], answers : list[int] ):
    for key, answer in enumerate(answers):
        print(f"{input[key]} : {answer}")
    pass
    print(f"\nTotal Input Length: {len(answers)}")
    # Final submission
    print(f"Total Sum: {sum(answers)}")
    return

# Main
if __name__ == '__main__':
    input = getInput()
    answers = list(map(soln, input))
    formatOutput(input, answers)
    pass