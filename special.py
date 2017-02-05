import sys

def main():
 n = input()
 for j in range(n):
  n1 = input()
  sum=0
  x=n1
  while n1>0:
   num=n1%10
   sum = sum + fact(num)
   n1=n1/10
  if x==sum:
   print "The number %s is Special!" % x
  else:
   print "The number %s is not Special!" % x
  
def fact(n1):
  p = 1
  for i in range(1,n1+1):
    p=p*i
  return p

if __name__ == '__main__':
 sys.exit(main())





