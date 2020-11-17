def my_f(s_1, s_2):
    sub = s_1 - s_2
    return f"Sub: {sub}"

print(my_f(int(input("s_1:")), int(input("s_2: "))))

def my_f1(*args):
    return args

print (my_f1(2, 3.4, False, [1,2]))

my_f2 = lambda s_1, s_2: s_1 - s_2
print (my_f2(55,8))