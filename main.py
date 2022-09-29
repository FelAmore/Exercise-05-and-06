# Exercise 05

def point():
    px = int(input('Enter the point px: '))
    py = int(input('Enter the point py: '))
    qx = int(input('Enter the point qx: '))
    qy = int(input('Enter the point qy: '))
    X = qx - px
    Y = qy - py
    r = qx + X, qy + Y
    return r
print(f'The point r  = {point()}')

# Exercise 06

def fixed_profit():
    burger = int(input('Enter burger selling price: '))
    soda = int(input('Enter soda selling price: '))
    combo = int(input('Enter combo meal selling price: '))
    return(burger+soda-combo)

print(f'The fixed price is ${fixed_profit():.2f}')