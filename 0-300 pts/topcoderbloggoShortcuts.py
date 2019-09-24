# Problem Statement
#
# You are helping to develop a weblog-management system called bloggo. Although bloggo pushes all content to the front end of a website in HTML, not all content authors enjoy using HTML tags in their text. To make their lives easier, bloggo offers a simple syntax called shortcuts to achieve some HTML textual effects. Your job is to take a document written with shortcuts and translate it into proper HTML.
# One shortcut is used to make italicized text. HTML does this with the <i> and </i> tags, but in bloggo, an author can simply enclose a piece of text using two instances of the underscore character, '_'. Thus, where a content author writes
#
#   You _should_ see the baby elephant at the zoo!
# bloggo will publish the following instead.
#
#   You <i>should</i> see the baby elephant at the zoo!
# Another shortcut serves to render text in boldface, which HTML accomplishes with <b> and </b> tags. Bloggo lets content authors do the same with paired instances of the asterisk character, '*'. When a content author writes the text
#
#   Move it from *Receiving* to *Accounts Payable*.
# it will end up on the website as
#
#   Move it from <b>Receiving</b> to <b>Accounts Payable</b>.
# Given a string, text, containing zero or more usages of the italic and boldface shortcuts, translate it into HTML as demonstrated by the examples above. There will be an even number of underscores and of asterisks in text, respectively, and the spans of text enclosed by successive pairs of these characters will not overlap. To render a span of text in italics in HTML, you must start with the <i> tag and end with the </i> tag. For boldface text, start with <b> and end with </b>. After rendering all shortcuts in HTML, return the resulting text as a string.
# Definition
#
# Class:
# bloggoShortcuts
# Method:
# expand
# Parameters:
# string
# Returns:
# string
# Method signature:
# def expand(self, text):


#Gendo90 has submitted the 250-point problem for 144.48 points
#Successful on first try - but difficult to pin down everything!
#can be refactored with a subfunction
class bloggoShortcuts(object):
    def expand(self, text):
        italic_arr = text.split('_')
        if(text[0]!="_"):
            output = italic_arr[0]
            italic_arr = italic_arr[1:]
            opening = True

        else:
            output = ""
            italic_arr = italic_arr[1:]
            opening = True

        for i, segment in enumerate(italic_arr):
            if(opening):
                addition = "<i>"
                opening = False
                output+=addition+segment
            else:
                addition = "</i>"
                opening = True
                output+=addition+segment



        bold_arr = output.split("*")
        if(output[0]!="*"):
            final_output = bold_arr[0]
            bold_arr = bold_arr[1:]
            opening = True
        else:
            final_output = ""
            bold_arr = bold_arr[1:]
            opening = True


        for segment in bold_arr:
            addition = segment
            if(opening):
                addition = "<b>"
                opening = False
                final_output+=addition+segment
            else:
                addition = "</b>"
                opening = True
                final_output+=addition+segment

        return final_output


test = bloggoShortcuts()

print(test.expand("MMMMMWWWW", "MWWWW"))
