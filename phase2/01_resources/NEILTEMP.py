import password_handler

valid_values = 'abcdefghijklmnopqrstuvwxyz0123456789'
expected_hash = b'$\xed\xb8v\x10\x1f\xe2\xa6\xc2\x0f\xaf[\x98|\xc7\x84l\xe1H\x02"\xed\xbf\xde\xd7>/;.\x9bI\xdf'

for c1 in valid_values:
    for c2 in valid_values:
        for c3 in valid_values:
            for c4 in valid_values:
                if password_handler.check_password(expected_hash, c1 + c2 + c3 + c4):
                    print("Password is " + c1 + c2 + c3 + c4)

# import password_handler
# import time

# def find_password():
#     valid_values = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     expected_hash = b'$\xed\xb8v\x10\x1f\xe2\xa6\xc2\x0f\xaf[\x98|\xc7\x84l\xe1H\x02"\xed\xbf\xde\xd7>/;.\x9bI\xdf'
#     for c1 in valid_values:
#         for c2 in valid_values:
#             for c3 in valid_values:
#                 for c4 in valid_values:
#                     if password_handler.check_password(expected_hash, c1 + c2 + c3 + c4):
#                         return c1 + c2 + c3 + c4

# t1 = time.perf_counter()
# password = find_password()
# t2 = time.perf_counter()
# print(f"Found password {password} in {t2 - t1:0.4f} seconds")

# ... NI script
import random 

with open('ni_numbers.txt', 'w') as file:
    for _ in range(1000):

        prefix_valid = False
        valid_first_characters = 'ABCEGHJKLMNOPRSTWXYZ'
        valid_second_characters = 'ABCEGHJKLMNPRSTWXYZ'
        digits = ""

        while not prefix_valid:
            c1 = random.choice(valid_first_characters)
            c2 = random.choice(valid_second_characters)
            if c1 + c2 not in ("BG","GB","NK","KN","TN","NT", "ZZ"):
                prefix_valid = True

        d1 = str(random.randrange(10))
        d2 = str(random.randrange(10))       
        d3 = str(random.randrange(10))        
        d4 = str(random.randrange(10))       
        d5 = str(random.randrange(10))
        d6 = str(random.randrange(10))

        suffix = random.choice("ABCD")

        add_spaces = random.randint(0,1)
        if add_spaces > 0:
            file.write(c1 + c2 + " " + d1 + d2 + " " + d3 + d4 + " " + d5 + d6 + " " + suffix + "\n")
        else:
            file.write(c1 + c2 + d1 + d2 + d3 + d4 + d5 + d6 + suffix + "\n")