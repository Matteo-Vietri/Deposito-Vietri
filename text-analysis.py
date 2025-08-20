try:
    with open("input.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found: input.txt")
    raise SystemExit(1)

def conta_righe(text):
    count = len(text.splitlines())
    return count

print(conta_righe(content))