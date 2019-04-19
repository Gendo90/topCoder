# got ~162 out of 250 pts, had to submit twice (used 'screen' instead of 'line')
# in second list comprehension
class ImageDithering(object):
    def count(self, dithered, screen):
        #split dithered into ind. letters
        dith_colors = [x for x in dithered]
        total = 0
        for col in dith_colors:
            for line in screen:
                line_num = len([x for x in line if x==col])
                total += line_num

        return total

test = ImageDithering()

print(test.count("ABCD", ("DCBA")))
