# Gendo90 has submitted the 200-point problem for 185.66 points
# Successful on first go! Took ~8 minutes
class Time(object):
    def whatTime(self, seconds):
        hours = seconds//(60*60)
        time_left = seconds - hours*(60*60)
        minutes = time_left//(60)
        time_left -= minutes*60
        seconds = time_left
        return str(hours)+":"+str(minutes)+":"+str(seconds)


test = Time()

print(test.whatTime(86399))
