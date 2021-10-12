def main():
    Strings_a=[]
    Strings_b=[]
    String=[]
    finished=False
    while not finished:
        String = []
        String = input("Please enter your strings:")
        if String in Strings_a:
            Strings_b.append(String)
        elif not String:
            print(Strings_b)
            finished=True
        Strings_a.append(String)

main()

