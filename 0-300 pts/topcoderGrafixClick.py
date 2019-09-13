# Problem Statement
#
# Note: This problem statement includes an image that may not appear if you are using a plugin. For best results, use the Arena editor.
# You have been hired to work on a graphics application called grafix. The interface includes several buttons that the user can click on during a session. One of these is the Save button, which appears in the application window as a rectangle composed of pixels. The location of each pixel is given by a pair of integers that specify the pixel's row number and column number, in that order. Such an integer pair is called the window coordinates of a pixel. Rows are numbered from top to bottom, and columns are numbered from left to right.
# The top left corner of the Save button has window coordinates (20, 50), meaning that it is a pixel occupying the 20th row from the top and the 50th column from the left. The bottom right corner of the Save button has window coordinates (39, 99). If the user clicks her mouse on any pixel within or on the border of the rectangle defined by these points, she is considered to have activated the Save button. Below is a magnified image of the Save button, showing the numbers of its rows and columns.
#
#
# Given a sequence of mouse clicks, your job is to determine which ones have activated the Save button. For each mouse click, the tuple (integer) mouseRows contains the row number of its window coordinates, while the tuple (integer) mouseCols contains its column number. The values in each tuple (integer) are in corresponding order, so the nth element of mouseRows and the nth element of mouseCols make up the window coordinates of the nth mouse click. You are to return a tuple (integer) containing, in ascending order, the zero-based index of each mouse click that activates the Save button.
# Definition
#
# Class:
# grafixClick
# Method:
# checkSaveButton
# Parameters:
# tuple (integer), tuple (integer)
# Returns:
# tuple (integer)
# Method signature:
# def checkSaveButton(self, mouseRows, mouseCols):


#Gendo90 has submitted the 300-point problem for 277.73 points
#Successful on first try!
class grafixClick(object):
    def checkSaveButton(self, mouseRows, mouseCols):
        output = []
        inputCoords = zip(mouseRows, mouseCols)
        for i, coord in enumerate(inputCoords):
            if(20<=coord[0]<=39):
                if(50<=coord[1]<=99):
                    output.append(i)

        return tuple(output)


test = grafixClick()

print(test.checkSaveButton((20, 39, 100), (99, 50, 200)))
