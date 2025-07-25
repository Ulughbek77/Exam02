names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']

max_length = max(len(name) for name in names)

longest_names = [name for name in names if len(name) == max_length]

print(", ".join(longest_names))

