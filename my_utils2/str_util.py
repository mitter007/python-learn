def str_reverse(s):
   l=len(s)
   x=''
   i=1
   while i<=l:
       x= x+s[l-i]
       i+=1
   return x

# 取出下标为x,y的元素
def substr(s,x,y):
    return s[x:y:1]


def main():
   print(str_reverse('abcdefg'))
   print(substr('abcdefg',1,3,))
main()