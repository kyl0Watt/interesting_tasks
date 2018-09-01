#!/usr/bin/env python3


def kollats(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            count += 1
            print(count, '=> {} \n'.format(num))
            num //= 2
        else:
            count += 1
            print(count, '=> {} \n'.format(num))
            num = (num * 3) + 1
    return count


def main():
    num = int(input('Input number: '))
    c = kollats(num)
    print(c + 1, '=> 1 \n')
    print('_' * 20, '\n', 'Totol turn: {}'.format(c + 1))


if __name__ == '__main__':
    main()
