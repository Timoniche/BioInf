def in_its_place(elem_indexed, i):
    return elem_indexed == i


def d_min_swap(permut):
    sz = len(permut)
    indexed_permut = [*enumerate(permut)]
    indexed_permut = sorted(indexed_permut, key=lambda e: e[1])
    visited = {b: False for b in range(sz)}
    ret = 0
    for i in range(sz):
        if in_its_place(indexed_permut[i][0], i) or visited[i]:
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


def permut_cycles(permut):
    sz = len(permut)
    indexed_permut = [*enumerate(permut)]
    indexed_permut = sorted(indexed_permut, key=lambda e: e[1])
    visited = {b: False for b in range(sz)}
    cnt_cycles = 0
    for i in range(sz):
        if in_its_place(indexed_permut[i][0], i):
            cnt_cycles += 1
            continue
        if visited[i]:
            continue
        traverse = i
        cnt_cycles += 1
        while not visited[traverse]:
            visited[traverse] = True
            traverse = indexed_permut[traverse][0]
    return cnt_cycles
