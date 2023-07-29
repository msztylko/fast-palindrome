# fast-palindrome
On a quest for the fastest palindrome algorithm.

[`palindromes.txt`](https://github.com/msztylko/fast-palindrome) contains examples of valid [palindromes](https://en.wikipedia.org/wiki/Palindrome). For instance:
> Won’t lovers revolt now?

## benchmark

Script [generate_benchmark.py](https://github.com/msztylko/fast-palindrome/blob/master/generate_benchmark.py) is used to generate 100 million test cases where:
 - 25% are correct palindromes
 - 25% are palindromes with cases randomly changed to lower or upper
 - 25% are broken palindromes with character in the middle changed to a different letter
 - 25% are random strings of letters

You can generate benchmark with:

```bash
python generate_benchmark.py > cases.txt
```
this will also create a file `expected_palindromes.txt` to verify that tested programs produce expected output.
