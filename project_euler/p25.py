# 1000-digit Fibonacci Number
import projecteuler as pe

found = False
fib_term_a = 1
fib_term_b = 1
index = 1
while not found:
    fib_term_a, fib_term_b = pe.fib_num(fib_term_a, fib_term_b)
    index = index + 1
    if len(str(fib_term_a)) == 1000:
        found = True
print(index)
