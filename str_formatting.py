# String formatting:
# Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."


# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(1, 2))


# 6. By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches.".format(3, 4))


# 7. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=5, peaches=6))


# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:.5} apples and {1:.3} peaches.".format("seven hundred", "two hundred"))


# 9. With f-strings and variables
a=12
b=11
print (f"Anna has {a} apples and {b} peaches.")


# 10. With % operator
print("Anna has %s apples and %s peaches." % (a, b))



# 11*. With variable substitutions by name (hint: by using dict)
fruits = {'apples': 22, 'peaches':17}
print("Anna has %(apples)s apples and %(peaches)s peaches." % fruits)
