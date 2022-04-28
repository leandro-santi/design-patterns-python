#!/bin/python3


class Action:
    def execute(self, player):
        pass


class Idle(Action):
    def execute(self, player):
        print(f"{player} ...")


class Walk(Action):
    def execute(self, player):
        print(f"{player} walked")


class Jump(Action):
    def execute(self, player):
        print(f"{player} jumped")


class DoubleJump(Jump):
    def execute(self, player):
        super().execute(player)
        print(f"{player} jumped in the air")


class Player:
    def __init__(self, name):
        self._name = name
        self._action = Idle()

    def set_action(self, action):
        self._action = action
    
    def execute_action(self):
        self._action.execute(self)

    def __str__(self):
        return self._name


if __name__ == "__main__":
    mario = Player("Mario")
    mario.execute_action()

    mario.set_action(Walk())
    mario.execute_action()

    mario.set_action(Jump())
    mario.execute_action()

    mario.set_action(Walk())
    mario.execute_action()

    mario.set_action(DoubleJump())
    mario.execute_action()

