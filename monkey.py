def print_monkeys(a):
    s = t = u = '\n'
    i = 0
    for i in range(len(a)):
        s += (("_,o=+#-\
*|_)(x@(>'^)\\&_,o=+#**|/)(x_(X*^||&_,o=+#~*|7)"
+ "(x__<`^(/&")[a[i]::21]
+ "*-" * (a[i] == 6)).center(14)
        t += "\
        (o o)\
        "
        u += "ooO--(_)--Ooo-"
    print(s + t + u[:-1])