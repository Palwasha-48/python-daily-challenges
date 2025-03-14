# Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 🔢💡

# User se number input lena
num = int(input("Enter a number: "))

# Prime number check karne ka function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Output print karna
if is_prime(num):
    print("Yes, it's a prime number!")
else:
    print("No, it's not a prime number!")
