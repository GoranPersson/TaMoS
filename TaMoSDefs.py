from random import randrange

def main():
    txt = open("defs.txt").read().split('\n')
    txt = txt[:-1]
    lengthtxt = len(txt)
    name = []
    defi = []
    for item in txt:
        temp = item.split(':')
        name.append(temp[0])
        defi.append(temp[1])

    for item in range(0,21):
        rand = randrange(lengthtxt)

        print(name[rand])
        input()
        print(defi[rand])
        input( '\n')

if __name__ == "__main__":
    main()
