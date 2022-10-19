# Prints out a triangle of user-defined size.

def triangle(n):
    for i in range(n):
        print((i+1)*'*')


if __name__ == '__main__':
    triangle(5)
