def show_cards(cards, message):
    print(message)
    for card in cards:
        print("\t", card['suit'], card['rank'])