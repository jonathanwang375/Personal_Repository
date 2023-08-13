import projecteuler as pe

fact_list_2 = []
prime_num_list = []
prime_num_list.append(2)
prime_num_list.append(3)
a = 3
while len(prime_num_list) != 10001:
    a = a + 2
    fact_list_2 = find_factors(a)
    if len(fact_list_2) == 2:
        prime_num_list.append(a)
print("The 10001st prime is: " + str(a))


fact_list_3 = []
sum = 5
current = 3
while current < 2000000:
    current = current + 2
    fact_list_3 = find_factors(current)
    if len(fact_list_3) == 2:
        sum = sum + current
print("The sum is: " + str(sum))

tri_fact_list = []
a = 1
test = 0
while len(tri_fact_list) < 500:
    test = triangle(a)
    tri_fact_list = find_factors(test)
    a = a + 1
print(test)

print(find_factors(6))
