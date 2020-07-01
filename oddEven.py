def oddEven(n,what):
  num = n / 2
  if what == "odd":
    for i in range(n):
      print( 2 * i + 1 )
      
  if what == "even":
    for i in range(1, n+1):
      print( 2 * i)
