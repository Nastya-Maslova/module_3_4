def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params(1, "str", False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [34, True, "a"]
values_dict = {"a": 1, "b": "str", "c": False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = 34.45, "b"
print_params(*values_list_2, 42)
