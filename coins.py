import random


class Coin:

    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self, key, value)

        self.is_Rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_Rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin Spent")

    def flip(self):
        heads_choice = [True,False]
        choice = random(heads_choice)
        self.heads = choice


class Pound(Coin):

    def __init__(self):
        data = {
            "original_value": 1,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "edges": 1
        }
        super().__init__(**data)


one_pound_coin = Pound()
print(one_pound_coin.color)
one_pound_coin.rust()
print(one_pound_coin.color)
