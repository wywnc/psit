def main():
    cat = []
    while True:
        name = input()
        if name.find(",") > -1:
            name = name.split(", ")
        if name == "IT'S A DOG":
            cat.pop(-1)
            continue
        elif name == "END":
            break
        cat.append(name)
    cat_new = []
    for i in cat:
        if type(i) == "list":
            for j in i:
                cat_new.append(j)
        else:
            cat_new.append(i)
    print(cat_new)


main()
