class Time(object):
    #constructor function
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    # overload reverse addition so I can add ints to the Time class. Also allows me to use built in sum() method
    def __radd__(self, other):
        seconds = self.time_to_seconds() + other
        return self.seconds_to_time(seconds)

    # overload the addition operator
    def __add__(self, other):
            if isinstance(other, Time):
                seconds = self.time_to_seconds() + other.time_to_seconds()
                return self.seconds_to_time(seconds)
            else:
                return self.__radd__(other)

    #convert all base 60 numbers to base 10
    def time_to_seconds(self):
        seconds = self.minute * 60 + (self.hour * 60 * 60) + self.second
        return seconds

    #covert from base 10 to base 60 into proper time notation
    def seconds_to_time(self, seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time



blank = Time(2, 43)
t = Time(1,2)

print(blank + 2)
