

class FootballMatch:
    def __init__(self, firstname, lastname,team, post, kitnumber, minute, howmanygoals):
        self.firstname = firstname
        self.lastname = lastname
        self.team = team
        self.post = post
        self.kitnumber = kitnumber
        self.minute = minute
        self.howmanygoals = howmanygoals
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    def details(self):
            return 'He plays in {} and he is a(n) {}. His kitnumber is {}.'.format(self.team, self.post, self.kitnumber)
    def goal(self):
        return 'The goal was scored in the {} minute and it was his {} goal.'.format(self.minute, self.howmanygoals)


player1 = FootballMatch('Ádám', 'Szalai', 'Basel', 'Striker', '9', '46.', '2.')

player1.fullname()
player1.details()
player1.goal()
print('Who scored?')
print(FootballMatch.fullname(player1))
print('Who is he?')
print(FootballMatch.details(player1))
print('When was the goal?')
print(FootballMatch.goal(player1))



