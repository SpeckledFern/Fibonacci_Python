def get_num_at(x):
   x1 = 0
   x2 = 1
   count = 0

   if x == 0:
      return 0
   else:
      while count < x:
         num = x1 + x2
         x1 = x2
         x2 = num
         count += 1
      return x1

def factorial(n):
   x = 1
   for i in range(1, n+1):
      x = x*i
   return x

