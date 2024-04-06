def recuersion(n):
    if n<1:
        print("done")
    else:
        recuersion(n-1)
        print(n)
recuersion(4)

# output
# done
# 1
# 2
# 3
# 4