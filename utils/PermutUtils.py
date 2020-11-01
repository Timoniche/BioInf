def in_its_place(elem_indexed, i):
    return elem_indexed == i


def d_min_swap(permut):
    sz = len(permut)
    indexed_permut = [*enumerate(permut)]
    indexed_permut = sorted(indexed_permut, key=lambda e: e[1])
    visited = {b: False for b in range(sz)}
    ret = 0
    for i in range(sz):
        if in_its_place(indexed_permut[i][0], i) | visited[i]:
            continue
        cycle_len = 0
        traverse = i
        while not visited[traverse]:
            visited[traverse] = True
            traverse = indexed_permut[traverse][0]
            cycle_len += 1
        if cycle_len > 0:
            ret += cycle_len - 1
    return ret
