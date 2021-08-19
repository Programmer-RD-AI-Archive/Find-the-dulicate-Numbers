pop = [0, 0, 5, 5, 5, 9, 8, 7, 6]


def x(a):
    q = {}
    p = []
    o = []
    a = list(a)
    for i in a:
        q[i] = 0
    for x in a:
        if x in o:
            q[x] = q[x] + 1
            if x in p:
                pass
            else:
                p.append(x)
        else:
            q[x] = q[x] + 1
            o.append(x)
    dulicate = q.copy()
    for x in list(dulicate):
        if dulicate[x] == 1:
            del dulicate[x]
        else:
            pass
    print(f"Before list : {a}")
    print(f"Amount of iturations : {dulicate}")
    print(f"Dulicating Numbers {p}")
    print(f"List with out duplicates {o}")


x(a=pop)
