from datetime import datetime


def stopwatch(function):
    def inner(request=None):
        start = datetime.now()
        function()
        stop = datetime.now()
        timedown = (stop - start)
        if request == 0:
            return start
        elif request == 1:
            return stop
        elif request == 100:
            return [start, stop, timedown.seconds]
        else:
            return timedown.microseconds
    return inner
