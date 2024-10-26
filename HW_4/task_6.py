class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        if 0 <= hours < 24:
            self.hours = hours
        else:
            print('Неверно указаны часы.')
        if 0 <= minutes < 59:
            self.minutes = minutes
        else:
            print('Неверно указаны минуты.')

        if 0 <= seconds < 59:
            self.seconds = seconds
        else:
            print('Неверно указаны секунды.')

    def add_seconds(self, second):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + second
        self.hours = total_seconds / 3600 % 24
        self.minutes = total_seconds / 60 % 60
        self.seconds = total_seconds % 60

    def add_minutes(self, minute):
        h = minute / 60
        if self.minutes + minute >= 60 and self.hours + h >= 24:
            self.minutes = (self.minutes + minute) % 60
            self.hours = (self.hours + h) % 24
        elif self.minutes + minute >= 60 and self.hours + h < 24:
            self.minutes = (self.minutes + minute) % 60
            self.hours = self.hours + h
        else:
            self.minutes = self.minutes + minute

    def add_hours(self, hour):
        if self.hours + hour >= 24:
            self.hours = (self.hours + hour) % 24
        else:
            self.hours = self.hours + hour

    def __add__(self, other):
        total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        total_seconds = total_seconds_self + total_seconds_other
        self.hours = total_seconds / 3600 % 24
        self.minutes = total_seconds / 60 % 60
        self.seconds = total_seconds % 60

