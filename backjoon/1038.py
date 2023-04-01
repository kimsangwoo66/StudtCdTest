"""
감소하는 수
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = []


def add_digit(digit, num):
    if digit == 1:
        arr.append(num)

    for i in range(num % 10):
        add_digit(digit - 1, num * 10 + i)


def backtrack(digit):
    for i in range(digit - 1, 10):
        add_digit(digit, i)


for i in range(1, 11):
    backtrack(i)

if n < len(arr):
    print(arr[n])

else:
    print(-1)

