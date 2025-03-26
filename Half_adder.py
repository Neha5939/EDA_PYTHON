def half_adder_sum(a,b):
    s= a ^ b
    return s
def half_adder_carry(a,b):
    c= a and b
    return c
print(f'A B Sum Carry')
for i in range(0,2):
    for j in range(0,2):
        print(f'{i} {j}  {half_adder_sum(i,j)}   {half_adder_carry(i,j)}')

