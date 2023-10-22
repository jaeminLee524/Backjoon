import sys
from itertools import combinations

input = sys.stdin.readline


N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_combi = combinations(cards, 3)
sum_cards = [sum(c) for c in cards_combi if sum(c) <= M]

print(max(sum_cards))