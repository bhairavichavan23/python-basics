def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def pyramid(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*", end=" ")
        print()

def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def checkerboard(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i + j) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def diagonal_cross(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j or i + j == n + 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Main program
n = 5
print("Choose pattern:")
print("1. Square")
print("2. Pyramid")
print("3. Number Triangle")
print("4. Checkerboard")
print("5. Diagonal Cross")

choice = int(input("Enter choice: "))

if choice == 1:
    square(n)
elif choice == 2:
    pyramid(n)
elif choice == 3:
    number_triangle(n)
elif choice == 4:
    checkerboard(n)
elif choice == 5:
    diagonal_cross(n)
else:
    print("Invalid choice")
