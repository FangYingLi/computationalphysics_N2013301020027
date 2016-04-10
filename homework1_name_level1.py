pre=['#     ', '#     ', '#     ', '#     ', '#     ', '####  ']
suf=['#   ', '#   ', '#   ', '#   ', '#   ', '#   ']
i=0

# while i<len(pre):
#     print pre[i]+suf[i]
#     i=i+1

for i in zip(pre,suf):
    print i[0]+i[1]

# why do I use for-loop instead of while?
# because it reduces number of python operation. The backend of python is C or
# fortran, both faster than python. So if we can, we'd like to reduce the
# number of operations in python. 
#
# Use while loop only when there is no clean data structure to iterate with,
# like your guessing game program.
# [When to use while or for in python](http://stackoverflow.com/questions/920645/when-to-use-while-or-the-for-in-python)
