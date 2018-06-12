# -*- coding:utf-8 -*-
import monkey
import sys

def print_palmtrees(num):
    for i in range(num):
        sys.stdout.write(' /|\\')
        sys.stdout.write('\n')
    for i in range(num):
        sys.stdout.write('  | ')
        sys.stdout.write('\n\n')

def print_rabbit_range(num):
    for i in range(num):
        sys.stdout.write(" \\/")
    sys.stdout.write("\n")
    for i in range(num):
        sys.stdout.write(" 00 ")
    sys.stdout.write("\n")
    for i in range(num):
        sys.stdout.write(" ** ")
    sys.stdout.write("\n")

if __name__ == "__main__":
    print("Bye monkeys")
    print("Starting to understand some git, this is already my second commit!")
    print("Hellow world again")
    print("i think i already udnerstood the basic concept of add and commit")
    monkey.print_monkeys([0,1,2,3,4,5])
    print_palmtrees(5)
    print_rabbit_range(5)