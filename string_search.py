#!python

def in_string(super_str, sub_str):
    assert isinstance(super_str, str)
    assert isinstance(sub_str, str)

    return in_string_iterative(super_str, sub_str)
    # return in_string_recursive(super_str, sub_str)

def in_string_iterative(super_str, sub_str):
    # sub_l = len(sub_str)
    # sub_index = 0
    # for super_index in range(0, len(super_str)-1):
    #     last_index = super_index + sub_l - 1
    #     while last_index <= len(super_str) - 1:
    #         for sub_index in range(super_index, last_index):
    #             print super_str[sub_index]
    #         last_index+=1

    # sub_l = len(sub_str)
    # sup_l = len(super_str)
    # sub_index = 0
    # super_index = 0
    # last = sup_l - 1
    # for super_index in range(0, last):
    #     while super_index<=last:
    #         for sub_index in range(super_index, super_index + sub_l - 1):
    #             print super_str[super_index]
    #         super_index += 1

    sup_l = len(super_str)
    sub_l = len(sub_str)
    first = 0
    last = sub_l
    while last is not sup_l - 1:
        for super_index in range(0, sup_l - sub_l):
            for sub_index in range(first, last):
                print super_str[sub_index]
        first += 1
        last += 1

    return True

def in_string_recursive(super_str, sub_str):
    return True

def main():
    import sys
    if len(sys.argv) > 1:
        super_str = sys.argv[1]
        args = sys.argv[2:]
        if len(args) > 0:
            for arg in args:
                in_str = in_string(super_str, arg)
                result = 'PASS' if in_str else 'FAIL'
                str_in = 'in' if in_str else 'not in'
                print('{}: {} is {} {}'.format(result, repr(arg), str_in, repr(super_str)))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('The program checks if string2..stringN are sub strings of string1')

if __name__ == '__main__':
    main()
