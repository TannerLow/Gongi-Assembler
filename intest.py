# TODO remove this file

t = "01011a"
v = None

try:
    if len(t) > 2:
        if t[:2] == "0x":
            v = int(t, 16)
        elif t[:2] == "0b":
            v = int(t, 2)
        else:
            v = int(t)
    else:
        v = int(t)
except:
    print("invalid")

print(v)
