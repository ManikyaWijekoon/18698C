import cmath
p=2
q=3
c=7
e=(q**2)-(4*p*c)
ans1=(-q-cmath.sqrt(e))/(2*p)
ans2=(-q+cmath.sqrt(e))/(2*p)
print('The answers are:[0] and [1]'.format(ans1,ans2))