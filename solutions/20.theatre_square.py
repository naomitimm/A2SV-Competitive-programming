def theatreSquare(m, n, a):
    m += m%a if m%a !=0 else 0
    n += n%a if n%a !=0 else 0
    
    flagstones = (m*n)// (a*a) 
    print(flagstones)

theatreSquare(6, 6, 4)