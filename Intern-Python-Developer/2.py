ls = ["abc","acb","bac","bca","cab","cba"]

a1 = input()
a2 = input()
a3 = input()

if a1 == ">":
    if "abc" in ls:
        ls.remove("abc")
    if "cab" in ls:
        ls.remove("cab")
    if "acb" in ls:
        ls.remove("acb")
if a1 == "<":
    if "bac" in ls:
        ls.remove("bac")
    if "cba" in ls:
        ls.remove("cba")
    if "bca" in ls:
        ls.remove("bca")
if a1 == "=":
    pass

if a2 == ">":
    if "acb" in ls:
        ls.remove("acb")
    if "abc" in ls:
        ls.remove("abc")
    if "bac" in ls:
        ls.remove("bac")
if a2 == "<":
    if "cab" in ls:
        ls.remove("cab")
    if "cba" in ls:
        ls.remove("cba")
    if "bca" in ls:
        ls.remove("bca")
if a2 == "=":
    pass

if a3 == ">":
    if "bac" in ls:
        ls.remove("bac")
    if "bca" in ls:
        ls.remove("bca")
    if "abc" in ls:
        ls.remove("abc")
if a3 == "<":
    if "cab" in ls:
        ls.remove("cab")
    if "cba" in ls:
        ls.remove("cba")
    if "acb" in ls:
        ls.remove("acb")
if a3 == "=":
    pass

for elem in ls:
    print(elem)
