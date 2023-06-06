import random

def generate_ni_number():
    alphabet = 'ABCEGHJKLMNPRTWXYZ'
    digits = '0123456789'
    first2letters = False
    ni_numbers = []

        # Create the NI number, removing letters that aren't used. 
    for _ in range(1000):
        first_letter = random.choice(alphabet)
        second_letter = random.choice(alphabet.replace('O', ''))
        numbers = ''.join(random.choices(digits, k=6))
        suffix = random.choice("ABCD")

        while not first2letters:
            first_letter = random.choice(alphabet)
            second_letter = random.choice(alphabet.replace('O', ''))
            if first_letter + second_letter not in ("BG","GB","NK","KN","TN","NT", "ZZ"):
                first2letters = True

        # Randomly choose the format for the NI number
        if random.choice([True, False]):
            ni_number = f'{first_letter}{second_letter} {numbers[:2]} {numbers[2:4]} {numbers[4:6]} {suffix}'
        else:
            ni_number = f'{first_letter}{second_letter}{numbers}{suffix}'

        ni_numbers.append(ni_number)

    return ni_numbers

def write_ni_numbers_to_file(ni_numbers):
    with open('ni_numbers.txt', 'w') as file:
        for ni_number in ni_numbers:
            file.write(ni_number + '\n')

ni_numbers = generate_ni_number()
write_ni_numbers_to_file(ni_numbers)