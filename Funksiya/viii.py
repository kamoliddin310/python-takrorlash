# def isAnagram(a, b):
#     return sorted(a) == sorted(b)

# print(isAnagram("nagaram", "anagram"))


d = lambda s, n: sorted(s) == sorted(n)

print(d("anagram", "nagaram"))