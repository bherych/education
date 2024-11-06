args = [1,2,1,2,4]



def find_single_int(args):
    single_int = 0
    for i in args:
        single_int = i ^ single_int
    return single_int

print(find_single_int(args))