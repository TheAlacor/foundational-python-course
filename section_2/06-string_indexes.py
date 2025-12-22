
name = 'Álvaro' # 0-Á,1-l,2-v,...


'''
print(name[0]) # Á
print(name[4]) # r
print(name[3]) # a

# how to get the last letter
#siempre el ultimo con [-1]
print(name[-1])

#another way
#[start:stop]
print(name[0:3])

# [start:stop:stepover]
print(name[0:3:2]) '''

#change order from the name
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])

full_name = name[-1] + name[-2] + name[-3] + name[-4] + name[-5] + name[-6]
print(full_name)

# correct form
print(name[::-1])




