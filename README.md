# fast-palindrome
On a quest for the fastest palindrome algorithm.

[`palindromes.txt`](https://github.com/msztylko/fast-palindrome) contains examples of valid [palindromes](https://en.wikipedia.org/wiki/Palindrome). For instance:
> Won’t lovers revolt now?

## benchmark

Script [generate_benchmark.py](https://github.com/msztylko/fast-palindrome/blob/master/generate_benchmark.py) is used to generate 200 million test cases where:
 - 1% are correct palindromes
 - 1% are palindromes with cases randomly changed to lower or upper
 - 49% are broken palindromes with character in the first or last quater of the string changed to a different letter
 - 49% are random strings of letters

You can generate benchmark with:

```bash
python generate_benchmark.py > cases.txt
```
this will also create a file `expected_palindromes.txt` to verify that tested programs produce expected output.

[`test.sh`](https://github.com/msztylko/fast-palindrome/blob/master/test.sh) can be used to run the benchmark like: `./test.sh ./c_palindrome_1`

## Results

### V1
[c_palindrome_1.c](https://github.com/msztylko/fast-palindrome/blob/master/c_palindrome_1.c) - straightforward implementation with calls to standard library.

`gcc -O1 c_palindrome_1.c -o c_palindrome_1`

```bash
./test.sh ./c_palindrome_1                                                                                      ok

real	0m22.617s
user	0m21.928s
sys	0m0.359s
```

`gcc -O3 c_palindrome_1.c -o c_palindrome_1`

```bash
./test.sh ./c_palindrome_1                                                                                      
ok

real	0m21.255s
user	0m20.455s
sys	0m0.418s
```

### V2
[c_palindrome_2.c](https://github.com/msztylko/fast-palindrome/blob/master/c_palindrome_2.c) - no calls to standard library.

`gcc -O1 c_palindrome_2.c -o c_palindrome_2`

```bash
./test.sh ./c_palindrome_2                                                                                     ok

real	0m20.334s
user	0m19.527s
sys	0m0.404s
```

`gcc -O3 c_palindrome_2.c -o c_palindrome_2`

```bash
./test.sh ./c_palindrome_2                                                                                    
ok

real	0m20.229s
user	0m19.450s
sys	0m0.412s
```
