# 18. Convert (7) to lambda function
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

foo = lambda x, y: x if x < y else y



# 19*. Convert (8) to regular function
# foo = lambda x, y, z: z if y < x and x > z else y

def foo (x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
