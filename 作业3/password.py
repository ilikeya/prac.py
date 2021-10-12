def main():
    print("Enter 1 continues,Enter 0 exist")
    continues =int(input("Enter your choice: "))
    numbert=int(input("Enter your user number: "))
    while numbert>0:
        get_password=input("\nEnter your password: ")
        length=len(get_password)
        print_asterisks(length)
        numbert-=1
def print_asterisks(number):
    for i in range(number):
        print('*',end='')
main()