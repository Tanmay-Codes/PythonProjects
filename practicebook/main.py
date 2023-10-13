n = int(input())
l = []
for _ in range(n):
    command = input().split(" ")
    cmd = command[0]
    args = command[1:]
    if cmd != 'print':
        cmd += "(" + ",".join(args) + ")"
        eval('l.' + cmd)
    else:
        print(l)

