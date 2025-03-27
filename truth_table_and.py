def and_1(a,b):
    c=a and b
    return c
def or_1(a,b):
    c= a or b
    return c
def not_1(a):
    c=int(not a)
    return c
def nand_1(a,b):
    c=int(not(a and b))
    return c
def nor_1(a,b):
    c=int(not(or_1(a,b)))
    return c
def xor_1(a,b):
    c= a ^ b
    return c
def xnor_1(a,b):
    c = int(not(a ^ b))
    return c
print(f'a b and or not nand nor xor xnor')
print("---------------------------------")
for i in range(0,2):
    for j in range(0,2):
        print(f'{i} {j}  {and_1(i,j)}   {or_1(i,j)}   {not_1(i)}  {nand_1(i,j)}   {nor_1(i,j)}    {xor_1(i,j)}    {xnor_1(i,j)}')