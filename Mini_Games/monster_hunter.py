import random


class Player:
    def __init__(self, name="player1", hp=100, dmg=15, pot=3):
        self.name = name
        self._hp = hp
        self.damage = dmg
        self.potions = pot
        self.gold = 0
        self.kills = 0

    def use_potions(self):
        if self.potions > 0:
            self._hp = min(self._hp + 30, 100)
            self.potions -= 1
        print(f"1 potion consumed, {self.name}'s hp increased to {self._hp}")

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

    def __str__(self):
        res = f"A Wild {self.name} Appeared:\nHP: {self._hp}\nDamage: {self.damage}\nReward: {self.reward} Gold"
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
        res = "What You Want to do?\n"

        for num, opt in enumerate(self.player_options):
            res += f"{num + 1}. {opt}\n"

        print(res)
        user_input = int(input())
        return user_input - 1

    def spawn_monster(self):
        monsters = [
            Monster("Goblin", 80, 8, 50),
            Monster("Slime", 30, 4, 20),
            Monster("Dragon", 150, 20, 200),
        ]
        monster = random.choice(monsters)
        print(monster)
        return monster

    def start(self):
        monster = self.spawn_monster()
        self.monster = monster

        self.combat()

    def combat(self):

        while self.player._hp > 0 and self.monster._hp > 0:
            # player turn
            opt = self.give_options()
            print(f"{self.player.name} used {self.player_options[opt]}\n")
            if self.player_options[opt] == "Attack":
                self.monster._hp = max(self.monster._hp - self.player.damage, 0)
                print(f"{self.monster.name}'s HP decreased to {self.monster._hp}\n")
            elif self.player_options[opt] == "Use Potion":
                self.player.use_potions()
                print(f"Your HP Increased to {self.player._hp}\n")
            elif self.player_options[opt] == "Run":
                break

            # monster turn
            if self.monster._hp != 0:
                print(f"{self.monster.name} used Attack\n")
                self.player._hp = max(self.player._hp - self.monster.damage, 0)
                print(f"Your HP decreased to {self.player._hp}\n")

        if self.player._hp == 0:
            print("Sad News, You Died!")
        elif self.monster._hp == 0:
            self.player.gold += self.monster.reward
            self.player.kills += 1
            print(
                f"WooHoo! You Killed a {self.monster.name}, You Won {self.monster.reward} Gold"
            )


player = Player("John")
battle = Battle(player)

battle.start()
