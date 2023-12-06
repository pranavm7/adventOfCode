import re


# Solution for Advent of Code 2023 Day 1 : Part 2

# Dictionary mapping spelled out numbers to digits
wordsToNumbers:dict = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

# For a given string, return a digit made up of first and last digits
def soln( input : str ) -> int:
    # use regex to find all digits in the string (including spelled out)
    # use re.compile to create a regex pattern that matches any digit or spelled out number
    # regex string: (\d|one|two|three|four|five|six|seven|eight|nine) with list comprehension
    pattern = re.compile(fr'(?=(\d|{"|".join(list(wordsToNumbers))}))')
    digits = re.findall( pattern= pattern, string= input )
    # if no digits, return 0
    if len(digits) == 0:
        return 0
    # if only one digit, new digit is the same digit twice
    if len(digits) == 1:
        # if the digit is spelled out, use the dictionary to get the digit
        if digits[0] in wordsToNumbers:
            return int(f'{wordsToNumbers[digits[0]]}{wordsToNumbers[digits[0]]}')
        return int(f'{digits[0]}{digits[0]}')
    # otherwise, convert if the first or last digit is spelled out
    firstAndLastDigits:list = [digits[0], digits[-1]]
    firstAndLastDigits = list(map(lambda x: wordsToNumbers[x] if x in wordsToNumbers else x,firstAndLastDigits))
    return int(f'{firstAndLastDigits[0]}{firstAndLastDigits[1]}')


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