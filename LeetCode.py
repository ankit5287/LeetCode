#  4.Median of two sorted array
a = [1,3]
b = [2]

c = sorted(a+b)
print(c)

end = len(c)
first = 0

mid = int((end-first)/2)
print(mid)
if len(c)%2 == 0:
    print((c[mid]+c[mid-1])/2)
else:
    print(c[mid])

# 26 Remove duplicate from sorted array

def remove(nums):
    s1 = set(nums)
    l1 = list(s1)

    nums[0:len(l1)] = l1
    return l1

print(remove([3,4,5,5,6,6]))


a1 = [1,2,3,4,5,5]
value = 5

a1.remove(value)
print(sorted(a1))

