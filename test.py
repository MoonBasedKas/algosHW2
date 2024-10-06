def main():
    for i in range(5, 101):
        # print(sum(i), )
        if i*(i -1)/ 2 != sum(i):
            print("f")
    pass

def sum(x):
    ans = 0
    for z in range(1, x):
        ans += (x - z)
    return ans


if __name__ == "__main__":
    main()