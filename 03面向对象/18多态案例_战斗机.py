class HeroFighter():
    def power(self):
        return 60

class AdvHeroFighter():
    def power(self):
        return 80

class EnemyFighter():
    def power(self):
        return 70

def fight(fighter1, fighter2):
    if fighter1.power() > fighter2.power():
        print('英雄飞机赢了')
    else:
        print('敌人飞机赢了')

if __name__ == '__main__':
    h1 = HeroFighter()
    e1 = EnemyFighter()
    fight(h1, e1)
    ah1 = AdvHeroFighter()
    e1 = EnemyFighter()
    fight(ah1, e1)




