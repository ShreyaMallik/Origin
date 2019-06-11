def closestp(p,k):
    p.sort(key=lambda k:k[0]**2+k[1]**2)
    return p[:k]
p=[[3,2],[5,0],[6,7],[8,3],[6,1]]
k=4
print(closestp(p,k))
