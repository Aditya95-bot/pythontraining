def twoSumSimple(num, target):
         x = 0
         len = len(num)
         while x < len:
                 z =x+1
                 while z < len:
                         if num[] + num[z] == target:
                                 return [x, z]
                         z += 1
                    x += 1
                 return []
         
n = [2, 7, 11, 15]
print(twoSumSimple(n, 9))        