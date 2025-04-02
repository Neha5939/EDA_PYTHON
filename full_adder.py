def full_adder_sum(a,b,c):
    s=(a and (not b) and (not c)) or ((not a) and b and (not c)) or ((not a) and (not b) and c) or (a and b and c)
    return int(s)
def full_adder_carry(a,b,c):
    c = (b and c) or (a and c) or (a and b)
    return int(c)
print(f'A B C  Sum Carry')
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f'{i} {j} {k}  {full_adder_sum(i,j,k)}   {full_adder_carry(i,j,k)}')
