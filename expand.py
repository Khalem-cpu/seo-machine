bases = [
    "python error",
    "javascript error",
    "windows error code",
    "linux error",
    "git error",
    "docker error",
    "npm error",
    "pip error"
]

modifiers = [
    "explained",
    "meaning",
    "fix",
    "solution",
    "causes",
    "how to resolve",
    "troubleshooting",
    "step by step"
]

with open("data/keywords.txt", "w", encoding="utf-8") as f:
    for b in bases:
        for m in modifiers:
            f.write(f"{b} {m}\n")

print("Expanded keyword list.")
