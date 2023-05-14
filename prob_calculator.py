import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.drawn = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
            setattr(self, key, value)
    def __repr__(self):
        return str(self.contents)
    def draw(self, n):
        self.drawn = []
        for i in range(n):
            if n>len(self.contents):
                self.drawn = self.contents
            else:
                rand = random.randint(0,len(self.contents)-1)
                self.drawn.append(self.contents[rand])
                self.contents.pop(rand)
        return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    s=0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_drawn_list = {}
        switch = True
        for k in expected_balls:
            balls_drawn_list[k] = balls_drawn.count(k)
            if balls_drawn.count(k)<expected_balls[k]:
                switch=False
            #print(balls_drawn.count(k))
            #print(k)
        #print(balls_drawn_list, expected_balls)
        #if balls_drawn_list==expected_balls:
        if switch==True:
            s=s+1
        #print(hat_copy.draw(num_balls_drawn))
    return s/num_experiments