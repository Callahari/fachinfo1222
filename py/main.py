def do_something(a,b):
  if isinstance((a,b),(int,float)):
    print(a+b)
  else:
    print(a,b,sep=' & ')

do_something(1,2)
do_something('alpha','omega')
