"""
내적
https://programmers.co.kr/learn/courses/30/lessons/70128
"""


def solution(a, b):
    return sum([a[val]*b[val]  for val in range(len(a))])