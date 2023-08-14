import projecteuler as pe

fact_list_3 = []
sum = 5
current = 3
while current < 2000000:
    current = current + 2
    fact_list_3 = pe.find_factors(current)
    if len(fact_list_3) == 2:
        sum = sum + current
print("The sum is: " + str(sum))

tri_fact_list = []
a = 1
test = 0
while len(tri_fact_list) < 500:
    test = pe.triangle(a)
    tri_fact_list = find_factors(test)
    a = a + 1
print(test)

print(find_factors(6))
