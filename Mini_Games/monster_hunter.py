import random


class Player:
    def __init__(self, name="player1", hp=100, dmg=15, pot=3):
        self.name = name
        self._hp = hp
        self._max_hp = 100
        self.damage = dmg
        self.potions = pot
        self.gold = 0
        self.kills = 0

    def use_potions(self):
        if self.potions > 0:
            self._hp = min(self._hp + 30, self._max_hp)
            self.potions -= 1
            print(f"1 potion consumed, {self.name}'s hp increased to {self._hp}")
            return True
        else:
            print("You Ran Out Of Potions!")
            return False

    def take_damage(self, hp):
        self._hp = max(self._hp - hp, 0)

    @property
    def inventory(self):
        res = f"{self.name}'s Inventory:\nPotions: {self.potions}\nGold: {self.gold}\nKills: {self.kills}"
        return res

    @property
    def hp(self):
        return self._hp


class Monster:
    def __init__(self, name, hp, dmg, reward):
        self.name = name
        self._hp = hp
        self.damage = dmg
        self.reward = reward

    def take_damage(self, hp):
        self._hp = max(self._hp - hp, 0)

    @property
    def hp(self):
        return self._hp

    def __str__(self):
        res = f"\nA Wild {self.name} Appeared:\nHP: {self._hp}\nDamage: {self.damage}\nReward: {self.reward} Gold"
        return res


class Battle:
    def __init__(self, player):
        self.player = player
        self.monster = None
        self.player_options = [
            "Attack",
            "Use Potion",
            "Run",
        ]

    def give_options(self):
        res = "\nWhat You Want to do?"

        for num, opt in enumerate(self.player_options):
            res += f"\n{num + 1}. {opt}"

        print(res)
        user_input = int(input())
        return user_input - 1

    def spawn_monster(self):
        monsters = [
            Monster("Goblin", 60, 8, 30),  # fast/normal
            Monster("Slime", 40, 5, 20),  # small
            Monster("Orc", 120, 15, 80),  # heavy attack
            Monster("Vampire", 90, 12, 100),  # heals itself
            Monster("Dragon", 200, 25, 300),  # powerfull Attack
        ]
        monster = random.choice(monsters)
        print(monster)
        return monster

    def start(self):
        self.monster = self.spawn_monster()
        return self.combat()

    def combat(self):

        while self.player.hp > 0 and self.monster.hp > 0:
            # player turn
            opt = self.give_options()
            print(f"\n{self.player.name} used {self.player_options[opt]}")
            if self.player_options[opt] == "Attack":
                self.monster.take_damage(self.player.damage)
                print(f"{self.monster.name}'s HP decreased to {self.monster.hp}")
            elif self.player_options[opt] == "Use Potion":
                if not self.player.use_potions():
                    continue
                # print(f"Your HP Increased to {self.player.hp}\n")
            elif self.player_options[opt] == "Run":
                break

            # monster turn
            if self.monster.hp != 0:
                print(f"\n{self.monster.name} used Attack")
                self.player.take_damage(self.monster.damage)
                print(f"Your HP decreased to {self.player.hp}")

        if self.player.hp == 0:
            print("Sad News, You Died!")
            return False
        elif self.monster.hp == 0:
            self.player.gold += self.monster.reward
            self.player.kills += 1
            print(
                f"WooHoo! You Killed a {self.monster.name}, You Won {self.monster.reward} Gold"
            )
            return True
        return True


class Game:
    def __init__(self, player):
        self.player = player

    def start(self):
        while self.player.hp > 0:
            battle = Battle(self.player)
            result = battle.start()

            if not result:
                break
        print("Game Over!")


player = Player("John")
game = Game(player)

game.start()
