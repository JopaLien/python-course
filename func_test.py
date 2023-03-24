def determine_dis(a=0, b=0, c=0, visualize=True):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Discriminant is negative")
        return
    if visualize:
        print(f"Discriminant = {d}")
    return d

def determine_roots(A=0, B=0, C=0):
    d = determine_dis(A, B, C)
    if not d:
        return
    root1 = (-B + d ** 0.5) / (2 * A)
    root2 = (-B - d ** 0.5) / (2 * A)
    return [root1, root2]
    


result1 = determine_roots(2, 35, 6)
print(f"First result is {result1}")
result2 = determine_roots(342, 35, 5)
print(f"Second result is {result2}")


# def multiple(x, y):
#     return x * y
# 
# def add(x, y):
#     return x + y
# 
# def multiple_add(x, y):
#     sum_mult = multiple(x, y) + add(x,y)
#     #sum_mult = x * y + x + y
#     return sum_mult
# 
# result1 = multiple_add(2, 4)
# print(result1)
# print(type(multiple))
# 
