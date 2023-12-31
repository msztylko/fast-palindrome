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

### V3
[c_palindrome_3.c](https://github.com/msztylko/fast-palindrome/blob/master/c_palindrome_3.c) - simplified conditional checks.

`gcc -O1 c_palindrome_3.c -o c_palindrome_3`

```bash
./test.sh ./c_palindrome_3                                                                                     ok

real	0m20.565s
user	0m19.821s
sys	0m0.425s
```

`gcc -O3 c_palindrome_3.c -o c_palindrome_3`

```bash
./test.sh ./c_palindrome_3                                                                                    
ok

real	0m20.603s
user	0m19.477s
sys	0m0.404s
```

### V4

[c_palindrome_4.c](https://github.com/msztylko/fast-palindrome/blob/master/c_palindrome_4.c) - even simpler conditional logic.

`gcc -O1 c_palindrome_4.c -o c_palindrome_4`

```bash
./test.sh ./c_palindrome_4                                                                                     ok

real	0m19.061s
user	0m18.357s
sys	0m0.407s
```

`gcc -O3 c_palindrome_4.c -o c_palindrome_4`

```bash
./test.sh ./c_palindrome_4                                                                                    
ok

real	0m19.074s
user	0m18.367s
sys	0m0.398s
```

## Why?

In a [python-extensions](https://github.com/msztylko/python-extensions/tree/master) project I was working on Assembly extension to Python for the same palindrome problem.
It turned out that I cannot directly translate [straightforward palindrome](https://github.com/msztylko/fast-palindrome/blob/master/c_palindrome_1.c) to Assembly (yet).   

I documented my process for translating [C to Assembly](https://github.com/msztylko/python-extensions/blob/master/C2Assembly.md), creating a couple C programs along the way. This gave me the idea for this project where I no longer try to get to hand-written Assembly, but simply get the fastest implementation of palindrome algorithm. 

Most optimizations are described in [C2Assembly](https://github.com/msztylko/python-extensions/blob/master/C2Assembly.md).
I got the idea for [version 4](https://github.com/msztylko/fast-palindrome/blob/master/c_palindrome_4.c) when I was staring for too long at `man ascii` table.
Final optimizations come from the binary representation of ascii characters we are checking here:
1. All the whitespace characters I want to ignore have value lower than '@' and I used this fact to skip them.
2. Lower- and uppercase latters differ by a single bit `0b00100000` and I used it to simplify conditional logic.
