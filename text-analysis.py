try:
    with open("input.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found: input.txt")
    raise SystemExit(1)

def conta_righe(text):
    line_count = len(text.splitlines())
    return line_count

def conta_parole(text):
    word_count = len(text.split())
    return word_count


print(conta_righe(content))
print(conta_parole(content))