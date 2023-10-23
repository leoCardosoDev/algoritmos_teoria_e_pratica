def insertion_sort(cards):
  for i in range(1, len(cards)):
    card = cards[i] # Carta atual a ser inserida na mão ordenada
    j = i -1
    while j>= 0 and card < cards[j]:
      cards[j+1] = cards[j]
      j -= 1
    cards[j+1] = card

def play_card_game():
  hand = [7, 2, 5, 10, 9, 3, 8, 4, 6, 1]
  print('Mão inicial: ', hand)
  insertion_sort(hand)
  print('Mão ordenada: ', hand)

play_card_game()
