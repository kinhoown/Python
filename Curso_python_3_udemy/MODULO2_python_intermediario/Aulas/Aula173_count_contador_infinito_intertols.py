#count é um contador sem fim

from itertools import count

c = count() #como o range vc pode passar o start e o step mas não pode passar o stop

for i in c:
    print(i)