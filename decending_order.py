def descending_order(num):
    if isinstance(num,int) and num>=0:
        return int(''.join(sorted(list(str(num))[::-1])))
    else:
        raise ValueError("num is not a non-negtive int")

descending_order(134)