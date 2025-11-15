class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Punkt(1, 2 )
    print(p.x, p.y)

    q = Punkt(3, 4)

    p.x = 5
    p.y = 10
    print(p.x, p.y)
    print(q.x, q.y)