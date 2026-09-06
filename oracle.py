import random
import sys

QUOTES = {
    "wisdom": [
        "Overfitting is just passionate memorization.",
        "A clean dataset today keeps CUDA errors away.",
    ],
    "chaos": [
        "Deploying to prod on a Friday builds character.",
        "Zero warnings in compiler log means the linter is broken.",
    ],
}


def speak(category="wisdom"):
    options = QUOTES.get(category, QUOTES["wisdom"])
    print(f"Oracle [{category.upper()}]: {random.choice(options)}")


if __name__ == "__main__":
    cat = sys.argv[1] if len(sys.argv) > 1 else "wisdom"
    speak(cat)
