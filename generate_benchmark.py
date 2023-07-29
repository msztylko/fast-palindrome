from random import randint, choice, random
from string import ascii_letters

NUM_TESTCASES = 100_000_000

def randomize_case(string):
    new_string = list(string)
    for i in range(len(new_string)):
        if random() < 0.5:
            new_string[i] = new_string[i].lower()
        else:
            new_string[i] = new_string[i].upper()

    return ''.join(new_string)

def break_single_char(string):
    length = len(string)
    mid = length // 2
    mid_char = string[mid]

    # only replace letters, not chars like ',' etc.
    i = 0
    while mid_char not in ascii_letters:
        i += 1
        mid_char = string[mid+i]
        
    new_string = list(string)
    new_string[mid+i] = choice(list(set(ascii_letters) - set(mid_char)))
    return ''.join(new_string)

def random_string(length=None):
    if length is None:
        length = randint(20, 40)

    return ''.join(choice(ascii_letters) for _ in range(length))

def main():
    global NUM_TESTCASES
    valid_palindromes = open('palindromes.txt').read().splitlines()
    l = len(valid_palindromes)
    generated_valid_palindromes = []
   
    idx = 0
    while NUM_TESTCASES > 0: 
        palindrome = valid_palindromes[idx]
        print(palindrome)
        generated_valid_palindromes.append(palindrome)
        print(randomize_case(palindrome))
        print(break_single_char(palindrome))
        print(random_string())
        NUM_TESTCASES -= 4
        idx = (idx + 1) % l

    with open('expected_palindromes.txt' ,'w') as f:
        for p in generated_valid_palindromes:
            f.write(p + '\n')

if __name__ == '__main__':
    main()
