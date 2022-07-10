import numpy as np


def generate_data():
    seqs = dict()
    idx = 1
    while idx < 1024:
        base = np.arange(1, idx+1)
        seqs[idx] = np.concatenate([base+idx*n for n in range(0, int(1024/idx), 2)])
        idx += idx
    return seqs


def check_solution(seqs):
    for i in range(1, 1024):
        lst = [2**j for j in range(10) if i in seqs[2**j]]
        amount = np.sum(lst)
        if i == 6:
            print(lst)
        if 1024 - amount != i:
            print(i)


if __name__ == '__main__':
    seqs = generate_data()
    print(seqs[2**3])
    check_solution(seqs)

