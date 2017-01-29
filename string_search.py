#!python


def main():
    import sys
    super_string = sys.argv[1]
    print super_string
    args = sys.argv[2:]
    if len(args) > 0:
        for arg in args:
            print arg



if __name__ == '__main__':
    main()
