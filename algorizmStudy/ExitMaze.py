from collections import Counter
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
tan = Counter(tangerine).most_common()

print(tan)