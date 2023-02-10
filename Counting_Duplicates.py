#Return the maximum duplicates of any letters in a string regardless of case

def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

print(duplicate_count('aabbbcccc'))
