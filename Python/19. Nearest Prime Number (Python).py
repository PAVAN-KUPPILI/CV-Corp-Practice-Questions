while not prime(upper):
        upper+=1
    if lower<2:
        print(upper)
    else:
        diff_low=x-lower
        diff_upp=upper-x
        if diff_low<diff_upp:
            print(lower)
        elif diff_upp<diff_low:
            print(upper)
        else:
            print(lower)
            print(upper)