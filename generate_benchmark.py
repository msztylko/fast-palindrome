from random import randint, choice, random, randrange
from string import ascii_letters, ascii_lowercase

NUM_TESTCASES = 200_000_000


def randomize_case(string):
    new_string = list(string)
    for i in range(len(new_string)):
        if random() < 0.5:
            new_string[i] = new_string[i].lower()
        else:
            new_string[i] = new_string[i].upper()

    return "".join(new_string)


def break_single_char(string):
    """Replace single char in the first or last quater of the string."""
    length = len(string)
    new_string = list(string)

    if random() < 0.5:
        idx = randrange(0, length // 4)
    else:
        idx = randrange(length // 4 * 3, length)

    new_string[idx] = choice(list(set(ascii_lowercase) - set(new_string[idx].lower())))
    return "".join(new_string)


def random_string(length=None):
    if length is None:
        length = randint(20, 40)

    return "".join(choice(ascii_letters) for _ in range(length))


def main():
    global NUM_TESTCASES
    valid_palindromes = open("palindromes.txt").read().splitlines()
    l = len(valid_palindromes)
    generated_valid_palindromes = []

    idx = 0
    while NUM_TESTCASES > 0:
        palindrome = valid_palindromes[idx]
        print(palindrome)
        generated_valid_palindromes.append(palindrome)
        random_case_palindrome = randomize_case(palindrome)
        print(random_case_palindrome)
        generated_valid_palindromes.append(random_case_palindrome)
        for _ in range(49):
            print(break_single_char(palindrome))
            print(random_string())
        NUM_TESTCASES -= 100
        idx = (idx + 1) % l

    with open("expected_palindromes.txt", "w") as f:
        for p in generated_valid_palindromes:
            f.write(p + "\n")


if __name__ == "__main__":
    main()
