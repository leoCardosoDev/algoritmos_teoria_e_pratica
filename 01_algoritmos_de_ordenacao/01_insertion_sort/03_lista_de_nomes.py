def insertion_short(names):
  for i in range(1, len(names)):
    name = names[i]
    j = i - 1
    while j>=0 and name < names[j]:
      names[j+1] = names[j]
      j -= 1
    names[j+1] = name

names = ['João', 'José', 'Maria', 'Augusto', 'Robson', 'Wesley', 'Leo']
print('Nomes: ', names)
insertion_short(names)
print('Nomes ordenados', names)

