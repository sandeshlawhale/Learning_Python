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

    def attack(self, target):
        target.take_damage(self.damage)
        print(f"\n{self.name} used Attack")
        print(f"{self.name} delt {self.damage} damage")

    @property
    def inventory(self):
        res = f"{self.name}'s Inventory:\nPotions: {self.potions}\nGold: {self.gold}\nKills: {self.kills}"
        return res

    @property
    def hp(self):
        return self._hp


class Monster:
    def __init__(self, name, hp, reward):
        self.name = name
        self._hp = hp
        self._max_hp = hp
        self.reward = reward

    def take_damage(self, hp):
        self._hp = max(self._hp - hp, 0)

    def attack(self, player):
        attack_name = random.choices(
            list(self.attacks.keys()),
            weights=[attack["weight"] for attack in self.attacks.values()],
        )[0]
        attack = self.attacks[attack_name]
        damage = attack["damage"]

        player.take_damage(damage)

        print(f"\n{self.name} used Attack")
        print(f"{self.name} delt {damage} damage")

        return attack

    @property
    def hp(self):
        return self._hp

    def __str__(self):
        res = f"\nA Wild {self.name} Appeared:\nHP: {self._hp}\nReward: {self.reward} Gold"
        return res


class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 60, 30)

        self.attacks = {
            "Punch": {"damage": 8, "weight": 70},
            "Quick Attack": {"damage": 12, "weight": 30},
        }


class Slime(Monster):
    def __init__(self):
        super().__init__("Slime", 40, 20)

        self.attacks = {
            "Body Slam": {"damage": 5, "weight": 80},
            "Acid Spit": {"damage": 10, "weight": 20},
        }


class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", 120, 80)

        self.attacks = {
            "Axe Swing": {"damage": 15, "weight": 75},
            "Heavy Attack": {"damage": 30, "weight": 25},
        }


class Vampire(Monster):
    def __init__(self):
        super().__init__("Vampire", 90, 100)

        self.attacks = {
            "Bite": {"damage": 12, "weight": 60, "heal": 0},
            "Blood Strike": {"damage": 20, "weight": 30, "heal": 5},
            "Life Drain": {"damage": 15, "weight": 10, "heal": 10},
        }

    def attack(self, player):
        attack = super().attack(player)

        heal = attack["heal"]

        if heal > 0:
            self._hp = min(self.hp + heal, self._max_hp)
            print(f"{self.name} healed for {heal} hp")


class Dragon(Monster):
    def __init__(self):
        super().__init__("Dragon", 200, 300)

        self.attacks = {
            "Claw Attack": {"damage": 25, "weight": 60},
            "Fireball": {"damage": 50, "weight": 25},
            "Dragon Breath": {"damage": 80, "weight": 15},
        }


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
            Goblin(),  # fast/normal
            Slime(),  # small
            Orc(),  # heavy attack
            Vampire(),  # heals itself
            Dragon(),  # powerfull Attack
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
                # self.monster.take_damage(self.player.damage)
                self.player.attack(self.monster)
                print(f"{self.monster.name}'s HP decreased to {self.monster.hp}")
            elif self.player_options[opt] == "Use Potion":
                if not self.player.use_potions():
                    continue
                # print(f"Your HP Increased to {self.player.hp}\n")
            elif self.player_options[opt] == "Run":
                break

            # monster turn
            if self.monster.hp != 0:
                self.monster.attack(self.player)
                # self.player.take_damage(self.monster.damage)
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
