
seenValues = set()

r1 = 0
r5 = -1

while r1 not in seenValues:
      lastSeen = r1
      seenValues.add(r1)


      r5 = r1 | 65536
      r1 = 8595037


      while True:
            r3 = r5 & 255
            r1 += r3
            r1 = r1 & 16777215
            r1 *= 65899
            r1 = r1 & 16777215

            r5 = r5 // 256

            if r5 < 1:
                break

      print(r1)


print(f'lowest number of iterations for {r1}')
print(f'highest number of iterations for {lastSeen}')





# if r1 == r0:
#       exit
# else:
#       goto 6

