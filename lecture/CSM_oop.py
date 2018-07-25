class Baller:
    all_players = []
    def __init__(self, name, has_ball = False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)

    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False

class BallHog(Baller):
    def pass_ball(self, other_player):
        return False

"""
>>> ajay = Baller('Ajay', True)
>>> surya = BallHog('Surya')
>>> len(Baller.all_players)
2
>>> len(surya.all_players)
2
>>> ajay.pass_ball(surya)
True
>>> ajay.pass_ball(surya)
False
>>> BallHog.pass_ball(surya, ajay)
False
>>> surya.pass_ball(ajay)
False
"""

class TeamBaller(Baller):
    """
    >>> ajay = Baller('Ajay', True)
    >>> surya = BallHog('Surya')
    >>> len(Baller.all_players)
    2
    >>> len(surya.all_players)
    2
    >>> ajay.pass_ball(surya)
    True
    >>> ajay.pass_ball(surya)
    False
    >>> BallHog.pass_ball(surya, ajay)
    False
    >>> surya.pass_ball(ajay)
    False
    >>> cheerballer = TeamBaller('Thomas', has_ball=True)
    >>> cheerballer.pass_ball(surya)
    Yay!
    True
    >>> cheerballer.pass_ball(surya)
    I don't have the ball
    False
    """
    def pass_ball(self, other):
        if self.has_ball:
            self.has_ball = False
            other.has_ball = True
            print('Yay!')
            print(True)
        else:
            print("I don't have the ball")
            print(False)

"""
>>> tracker1 = PingPongTracker()
>>> tracker2 = PingPongTracker()
>>> tracker1.next()
1
>>> tracker1.next()
2
>>> tracker2.next()
1
"""
class PingPongTracker:
    def __init__(self):
        self.current = 0
        self.index = 1
        self.add = True
    def next(self):
        if self.add:
            self.current += 1
        else:
            self.current -= 1

        if has_seven(index):
            self.add = False


class Bird:
    def __init__(self, call):
        self.call = call
        self.can_fly = True
    def fly(self):
        if self.can_fly:
            return "Don't stop me now!"
        else:
            return "Ground control to Major Tom..."
    def speak(self):
        print(self.call)

class Chicken(Bird):
    def speak(self, other):
        Bird.speak(self)
        other.speak()

class Penguin(Bird):
    can_fly = False
    def speak(self):
        call = "Ice to meet you"
        print(call)

andre = Chicken("cluck")
gunter = Penguin("noot")
def g():
    """
    >>> andre.speak(Bird("coo"))
    cluck
    coo
    >>> gunter.fly()
    "Don't stop me now!"
    >>> andre.speak(gunter)
    cluck
    Ice to meet you
    >>> Bird.speak(gunter)
    noot
    """

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'

class Proletariat(Worker):
    greeting = 'Comrade'
    def work(self, other):
        other.greeting = self.greeting + ' ' + other.greeting
        other.work() # for revolution
        return other

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

def f():
    """
    >>> Worker().work()
    'Sir, I work'
    >>> jack
    Peon
    >>> jack.work()
    'Maam, I work'
    >>> john.work()[10:]
    Peon, I work
    'to gather wealth'
    >>> Proletariat().work(john)
    Comrade Peon, I work
    Peon
    >>> john.elf.work(john)
    'Comrade Peon, I work'
    """

class Dress:
    """What color is the dress?
    >>> blue = Dress('blue')
    >>> blue.look()
    'blue'
    >>> gold = Dress('gold')
    >>> gold.look()
    'gold'
    >>> blue.look()  # 2 does not evenly divide 3; changes to gold
    >>> Dress('black').look()
    'black'
    >>> gold.look()  # 2 does not evenly divide 5; changes to black
    >>> gold.look()  # 3 evenly divides 6
    'black'
    >>> Dress('white').look()
    'white'
    >>> gold.look()  # 4 evenly divides 8
    'black'
    >>> blue.look()  # 3 evenly divides 9
    'gold'
    """
    seen = 0
    color = None
    def __init__(self, color):
        self.color = color
        self.seen = 0
    def look(self):
        self.seen += 1
        Dress.seen += 1
        if Dress.seen % self.seen == 0:
            Dress.color = self.color
            return self.color
        else:
            self.color = Dress.color

def play_round(starter, cards):
    """Play a round and return all winners so far. Cards is a list of pairs.
    Each (who, card) pair in cards indicates who plays and what card they play.
    >>> play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    [1]
    >>> play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It's not your turn, player 3
    It's not your turn, player 0
    The round is over, player 1
    [1, 3]
    >>> play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed
    It's not your turn, player 2
    [1, 3]
    """
    r = Round(starter)
    for who, card in cards:
        try:
            r.play(who, card)
        except AssertionError as e:
            print(e)
    return Round.winners

class Round:
    players, winners = 4, []

    def __init__(self, starter):
        self.starter, self.player, self.highest = starter, starter, -1

    def play(self, who, card):
        assert not self.complete(), 'The round is over, player '+str(who)
        assert self.player == who, "It's not your turn, player "+str(who)
        self.player = (self.player + 1) % 4
        if card >= self.highest:
            self.control, self.highest = who, card
        if self.complete():
            self.winners.append(self.control)
    def complete(self):
        return self.player == self.starter and self.highest != -1
