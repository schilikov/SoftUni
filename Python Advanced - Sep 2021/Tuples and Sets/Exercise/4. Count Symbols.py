# Store unique letters and print how many times we found them in text
text = input()
histogram = {}

for letter in text:
    histogram[letter] = histogram.get(letter, 0) + 1

for letter in sorted(histogram):
    print(f"{letter}: {histogram[letter]} time/s")