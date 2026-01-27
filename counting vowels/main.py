def count_vowels(text):
    vowels = set('aeiouAEIOU')

    count = 0

    found = set()

    for ch in text:
        if ch in vowels:
            found.add(ch)
            count += 1
    return count, found