def even_numbers(lisa):
    katya = []
    for p in lisa:
      if p%2 == 0:
        katya.append(p)
    return katya

parancem = [5, 6, 89, 1, 14, 86, 4938]

print(even_numbers(parancem))
      