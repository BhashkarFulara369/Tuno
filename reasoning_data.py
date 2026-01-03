import random

OUTPUT_FILE = "reasoning_sft.txt"
TOTAL_SAMPLES = 7000

random.seed(42)

def generate_addition():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    total = a + b
    return f"""<doc>
Question: {a} + {b}?

Reasoning:
Step 1: Add {a} and {b}
Step 2: {a} + {b} = {total}

Answer: {total}
</doc>
"""

def generate_multiplication():
    a = random.randint(12, 99)
    b = random.randint(2, 9)

    tens = (a // 10) * 10
    ones = a % 10

    part1 = tens * b
    part2 = ones * b
    total = part1 + part2

    return f"""<doc>
Question: {a} × {b}?

Reasoning:
Step 1: Decompose {a} into {tens} and {ones}
Step 2: Multiply {tens} × {b} = {part1}
Step 3: Multiply {ones} × {b} = {part2}
Step 4: Add {part1} + {part2} = {total}

Answer: {total}
</doc>
"""

def generate_division():
    b = random.randint(2, 9)
    result = random.randint(3, 20)
    a = b * result

    return f"""<doc>
Question: {a} ÷ {b}?

Reasoning:
Step 1: Recognize that {a} is divisible by {b}
Step 2: Divide {a} by {b}
Step 3: {a} ÷ {b} = {result}

Answer: {result}
</doc>
"""

def generate_comparison():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    greater = max(a, b)

    return f"""<doc>
Question: Which number is greater, {a} or {b}?

Reasoning:
Step 1: Compare the two numbers
Step 2: {greater} is larger than the other number

Answer: {greater}
</doc>
"""

generators = [
    generate_addition,
    generate_multiplication,
    generate_division,
    generate_comparison,
]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for _ in range(TOTAL_SAMPLES):
        gen = random.choice(generators)
        sample = gen()
        f.write(sample + "\n")

print(f"Generated {TOTAL_SAMPLES} Grade-S reasoning samples in {OUTPUT_FILE}")
