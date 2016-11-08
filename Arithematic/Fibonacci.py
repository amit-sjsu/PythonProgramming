known={0:0,1:1}

def fibonaci(n):
    if n in known:
        return known[n]

    res= fibonaci(n-1)+fibonaci(n-2)
    known[n]=res
    return res


fibonaci(8)
for key in known:
    print known[key],