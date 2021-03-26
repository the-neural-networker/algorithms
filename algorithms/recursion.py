def countdown(n):
    """Counts down from n to 1 recursively"""
    print(n)
    if n > 1:
        countdown(n - 1)
    else:
        return

def factorial(n):
    """Returns n! computed recursively."""
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == "__main__":
    n = 10
    print("T minus...")
    countdown(n)
    print("Blast Off!")