import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for key, val in kwargs.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, count):
        if count <= len(self.contents):
            drawn = []
            while count > 0:
                drew = self.contents.pop(random.randrange(len(self.contents)))
                drawn.append(drew)
                count -= 1
            return drawn
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = list()
    for key, val in expected_balls.items():
        for _ in range(val):
            expected_balls_list.append(key)
    expected_balls_list.sort()
    print(expected_balls_list)
    m = 0
    for _ in range(num_experiments):
        obj = copy.deepcopy(hat)
        expected_balls_list_copy = copy.deepcopy(expected_balls_list)
        balls_drawn = obj.draw(num_balls_drawn)
        for i in balls_drawn:
            for j in expected_balls_list_copy:
                if i == j:
                    expected_balls_list_copy.pop(expected_balls_list_copy.index(j))
        if not expected_balls_list_copy:
            m += 1

    return m/num_experiments
