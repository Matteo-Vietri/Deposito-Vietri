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

def parole_frequenti(text):
    for ch in "-.,\n\r!?;:":
        text = text.replace(ch, ' ')
    text = text.lower()
    words = text.split()
    unique_words = {}
    for word in words:
        if word in unique_words:
            unique_words[word] = unique_words[word] + 1
        else:
            unique_words[word] = 1

    sorted_items = sorted(unique_words.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:5]



print(conta_righe(content))
print(conta_parole(content))
print(parole_frequenti(content))