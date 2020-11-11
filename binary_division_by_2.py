def by_two(num):
    binary=[]
    while num>0:
        remainder = num%2
        binary.append(remainder)
        num //=2
    # THIS
    # binum=""
    # while binary:
    #     binum+=str(binary.pop())
    # return int(binum)

    # OR THIS
    binary.reverse()
    binum = "".join([str(i) for i in binary])
    return int(binum)
print(by_two(242))
