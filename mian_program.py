inp="ABCDFFFFQWERTYUIOPDDDDDDDD"
s = inp.lower()
a = 0
b = 0
c = set()
longest_substring = ""
for i in range(len(s)):
    while s[i] in c:
        c.remove(s[a])
        a += 1
    c.add(s[i])
    if len(c) > b:
        b = len(c)
        longest_substring = s[a:i+1]
print("Length:",b,"\n"+"Substring:",longest_substring)