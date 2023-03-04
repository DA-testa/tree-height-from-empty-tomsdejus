# python3

import sys
import threading
import numpy


def compute_height(n, parents):

    children = {i: [] for i in range(n)}
    for i, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(i)

    def compute_height_helper(node):
        if not children[node]:
            return 1
        else:
            return 1 + max(compute_height_helper(child) for child in children[node])

    root = parents.index(-1)

    return compute_height_helper(root)


def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the name of the input file: ")

    if 'a' in file_name:
        print("File name cannot contain the letter 'a'")
        exit()

    with open("test/" + file_name, "r") as input_file:
        n = int(input_file.readline())
        parents = list(map(int, input_file.readline().split()))

    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
