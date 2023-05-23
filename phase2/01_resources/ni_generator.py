import random

def generate_ni_number():
    alphabet = 'ABCDEFGHJKLMNPRTWXYZ'
    digits = '0123456789'
    ni_numbers = []

    for _ in range(1000):
        first_letter = random.choice(alphabet.replace('D', '').replace('F', '').replace('I', '').replace('Q', '').replace('U', '').replace('V', ''))
        second_letter = random.choice(alphabet.replace('O', ''))
        numbers = ''.join(random.choices(digits, k=6))
        suffix = random.choice(alphabet)

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