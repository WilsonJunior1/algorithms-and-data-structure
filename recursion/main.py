def recursion(i):
    print(f"Called {i} times.")
    i += 1

    if i >= 5:
        return
    else:
        recursion(i)

recursion(0)
