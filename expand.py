bases = [
    "python error",
    "python exception",
    "python traceback",
    "javascript error",
    "javascript exception",
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
    "how to fix",
    "troubleshooting",
    "step by step",
    "examples",
    "common reasons",
    "best solution",
    "quick fix",
    "error message",
    "resolution",
    "debugging",
    "stack trace",
    "root cause",
    "why it happens",
    "how to resolve",
    "permanent fix"
]

with open("data/keywords.txt", "w", encoding="utf-8") as f:
    for b in bases:
        for m in modifiers:
            f.write(f"{b} {m}\n")

print("Mass keyword expansion completed.")
