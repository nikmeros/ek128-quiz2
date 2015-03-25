def pack_crayons(a,L=6):
    a.append(10000000) 
    l = len(a);
    i = 0;
    R = -1;
    N = 0;
    Ltemp = L;
    total = 0;
    while i < l:
        if a[i] > L:
            R+=1;
            i+=1;
        else:
            total+=a[i];
            Ltemp-=a[i];
            if a[i+1] > Ltemp:
                N+=1;
                i+=1;
                Ltemp = L;
            else:
                i+=1;
    
    used = total/(L*N);
    return(N,used,R)
