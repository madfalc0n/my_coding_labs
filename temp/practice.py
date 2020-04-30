#append
a = [1,2,3,4,5]
b = [1,2,3]
a.append(b)
print(a)
#[1, 2, 3, 4, 5, [1, 2, 3]]

a = [1,2,3,4,5]
b = [[1,2,3]]
a.append(b)
print(a)
#[1, 2, 3, 4, 5, [[1, 2, 3]]]

a = [1,2,3,4,5]
b = 'apple'
a.append(b)
print(a)
#[1, 2, 3, 4, 5, 'apple']


#extend
a = [1,2,3,4,5]
b = [1,2,3]
a.extend(b)
print(a)
#[1, 2, 3, 4, 5, 1, 2, 3]

#extend
a = [1,2,3,4,5]
b = [[1,2,3]]
a.extend(b)
print(a)
#[1, 2, 3, 4, 5, [1, 2, 3]]

#extend
a = [1,2,3,4,5]
b = 'apple'
a.extend(b)
print(a)
#[1, 2, 3, 4, 5, 'a', 'p', 'p', 'l', 'e']

#extend
a = [1,2,3,4,5]
b = ['apple']
a.extend(b)
print(a)
#[1, 2, 3, 4, 5, 'apple']