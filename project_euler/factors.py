import projecteuler as pe

tri_fact_list = []
a = 1
test = 0
while len(tri_fact_list) < 500:
    test = pe.triangle(a)
    tri_fact_list = find_factors(test)
    a = a + 1
print(test)

print(find_factors(6))
