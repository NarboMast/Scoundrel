from cards.CardDeck import CardDeck
from Weapon import Weapon

DEFAULT_HEALTH = 20

def record_card(picked_card, weapon, health):
    suit = picked_card.suit
    val = picked_card.val

    if suit == 'hearts':
        health = min(health + val, DEFAULT_HEALTH)
    elif suit == 'diamonds':
        weapon.damage = val
        weapon.last_enemy_rank = 15
    else:
        weapon, health = battle(weapon, health, val)

    return weapon, health

def battle(weapon, health, curr_enemy_rank):
    #absence of weapon OR lack of rank
    if weapon.damage == 0 or curr_enemy_rank >= weapon.last_enemy_rank:
        health -= curr_enemy_rank
        return weapon, health

    battle_type = int(input('0 - barehanded fight | 1 - with weapon: '))

    if battle_type == 1:
        health -= max((curr_enemy_rank - weapon.damage), 0)
        weapon.last_enemy_rank = curr_enemy_rank
    else:
        health -= curr_enemy_rank

    return weapon, health


def skip_dungeon(cards, n):
    moved = cards[:n]
    del cards[:n]
    cards.extend(moved)
    return cards

def display_stats(dungeon_cards, health, cards_left_num, weapon):
    print()
    print('Health:', health, '| Cards left:', cards_left_num)
    print('Weapon:', weapon)
    print(dungeon_cards)


class Scoundrel:
    def __init__(self):
        self.card_deck = CardDeck()

    def start(self):
        health = DEFAULT_HEALTH
        weapon = Weapon(0,15)
        cards = self.card_deck.get_shuffled_card_deck()
        skip_dungeon_available = True

        dungeon = cards[0:4]

        while len(cards) >= 4:
            if skip_dungeon_available:
                display_stats(dungeon, health, len(cards), weapon)
                enter_dungeon = int(input('-1 to skip, 0 to enter: '))

                if enter_dungeon == -1:
                    skip_dungeon(cards, len(dungeon))

                    dungeon = cards[0:4]
                    skip_dungeon_available = False
                    continue

            while len(dungeon) > 1:
                display_stats(dungeon, health, len(cards), weapon)
                picked_card_index = int(input('Pick a card: '))
                picked_card = dungeon[picked_card_index]

                weapon, health = record_card(picked_card, weapon, health)

                if health <= 0:
                    print('Death')
                    break

                dungeon.pop(picked_card_index)
                cards.pop(picked_card_index)

            dungeon.extend(cards[1:4])
            skip_dungeon_available = True