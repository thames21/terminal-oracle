import random

QUOTES = [
    "Overfitting is just passionate memorization.",
    "A clean dataset today keeps the CUDA out-of-memory errors away.",
    "In production, everything that can fail, fails asynchronously."
]

def speak():
    print(f"Oracle says: {random.choice(QUOTES)}")

if __name__ == "__main__":
    speak()