# Even Fibonacci Numbers
import projecteuler as pe

term_a_fib = 1
term_b_fib = 2
sum = 0
while term_a_fib < 4000000:
    term_a_fib, term_b_fib = pe.fib_num(term_a_fib, term_b_fib)
    if term_a_fib % 2 == 0:
        sum = sum + term_a_fib
print(sum)
