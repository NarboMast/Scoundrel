from cards.CardDeck import CardDeck

def record_card(picked_card, weapon, health):
    suit = picked_card.suit
    val = picked_card.val

    if suit == 'hearts':
        health = heal(health, val)
    elif suit == 'diamonds':
        weapon = [val, weapon[1]]
    else:
        weapon, health = battle(weapon, health, val)

    return weapon, health

def heal(health, val):
    health += val

    if health > 20:
        health = 20

    return health

def battle(weapon, health, curr_enemy_rank):
    weapon_damage = weapon[0]
    prev_enemy_rank = weapon[1]
    battle_type = input('0 - barehanded fight | 1 - with weapon: ')

    if battle_type == 1:
        if curr_enemy_rank >= prev_enemy_rank:
            health -= curr_enemy_rank
        else:
            health -= max(curr_enemy_rank - weapon_damage, 0)
            weapon[1] = curr_enemy_rank
    else:
        health -= curr_enemy_rank

    return weapon, health


class Scoundrel:
    def __init__(self):
        self.card_deck = CardDeck()

    def start(self):
        health = 20
        weapon = [0, 0] #damage, previous enemy rank
        cards = self.card_deck.get_shuffled_card_deck()

        dungeon = cards[0:4]

        while len(cards) >= 4:
            print('Weapon:', weapon, '| Health:', health, '| Cards left:', len(cards))
            print(dungeon)

            picked_card = dungeon[int(input('Pick a card: '))]

            weapon, health = record_card(picked_card, weapon, health)

            cards.pop()