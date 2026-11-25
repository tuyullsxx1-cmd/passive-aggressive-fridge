"""One passive-aggressive note from a smart fridge."""

import os

LINE = "I kept your leftovers cold for four days. You thanked the microwave."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
