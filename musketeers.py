# Your code here# Your code here
from itertools import permutations
import sys

# Read three symbols (one per line)
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()

names = ["Gladden", "Kunal", "Animay"]

def satisfies(rel, left, right, order):
    # rel is '<' or '>'
    pos_left = order.index(left)
    pos_right = order.index(right)
    if rel == '<':
        return pos_left < pos_right
    else:
        return pos_left > pos_right

valid_orders = []
for perm in permutations(names):
    if (satisfies(a, "Gladden", "Kunal", perm) and
        satisfies(b, "Gladden", "Animay", perm) and
        satisfies(c, "Kunal", "Animay", perm)):
        valid_orders.append(perm)

if len(valid_orders) == 1:
    # print the middle brother (index 1)
    print(valid_orders[0][1])
else:
    print("Impossible")
