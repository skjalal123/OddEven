def oddEven(n,what):
  num = int(n / 2)
  if what == "odd":
    for i in range(num):
      print( 2 * i + 1 )
      
  if what == "even":
    for i in range(1, num+1):
      print( 2 * i)

oddEven(50,"even")
