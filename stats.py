class Stats():      #просматривается статистика
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('record.txt', 'r') as file:
            self.record = int(file.readline())

    def reset_stats(self):      #вся статистика, которая будет меняться во время игры
        self.guns_left = 2
        self.score = 0
