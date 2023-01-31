''' 
Напишите функцию, которая принимает
строку от пользователя и печатает 
все перестановки этой строки.
?????????????
'''

import itertools

s = input()
    
nums = list(s)
permutations = list(itertools.permutations(nums))
 
print([''.join(permutation) for permutation in permutations])