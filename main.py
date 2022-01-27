print("================================================")

# Program 6:
N = int(input("Enter the Number"))
for I in range(N, 0, -1):
    for J in range(N, I, -1):
        print(end=" ")
    for K in range(0, I):
        print('* ', end="")
    print()

print("================================================")

# Program 7:
N = int(input("Enter the Number"))
for I in range(N, 0, -1):
    for J in range(N, I, -1):
        print(end=" ")
    for K in range(0, I):
        print('* ', end="")
    print()
for I in range(1, N):
    for J in range(0, N - I - 1):
        print(end=" ")
    for K in range(0, I + 1):
        print('* ', end="")
    print()

print("================================================")

# Program 8:
N = int(input("Enter the Number:"))
for I in range(0, N):
    for S in range(0, N - I - 1):
        print(end=" ")
    for J in range(0, I + 1):
        print('* ', end="")
    print()
for I in range(N - 1, 0, -1):
    for S in range(N, I, -1):
        print(end=" ")
    for J in range(0, I):
        print('* ', end="")
    print()

print("================================================")

# Program 9:
N = int(input("Enter the Number:"))
for I in range(0, N):
    for S in range(0, N - I - 1):
        print(end=" ")
    for J in range(0, I + 1):
        if ((I >= 2 and I < N - 1) and (J > 0 and J < I)):
            print(end="  ")
        else:
            print('*', end=" ")
    print()

print("================================================")

# Program 10:
N = int(input("Enter the Number:"))
for I in range(N, 0, -1):
    for J in range(N, I, -1):
        print(end=" ")
    for K in range(0, I):
        if ((I < N and I > 2) and (K > 0 and K < I - 1)):
            print(end="  ")
        else:
            print('*', end=" ")
    print()

print("================================================")