# Problem Statement
#
# Forgetting a close friend's birthday is quite embarrassing, but forgetting it two years in a row is a catastrophe. So what can a coder do to prevent this from happening again? Well, the thing he possibly can do best: code...  Given a string date (the current date) and a tuple (string) birthdays, a list of people's birthdays and names, return a string, the date of the next occurring birthday, starting from the current date.  date is in the format "MM/DD" (quotes for clarity), where MM represents the two-digit month and DD represents the two-digit day (leading zero if necessary). Each element of birthdays is in the format "MM/DD <Name>" (quotes for clarity), where MM/DD is the date of <Name>'s birthday. <Name> is a sequence of characters from 'A'-'Z' and 'a'-'z'. There is exactly one space character between the date and <Name>. The date returned also has to be in the format "MM/DD" (quotes for clarity).
# Definition
#
# Class:
# Birthday
# Method:
# getNext
# Parameters:
# string, tuple (string)
# Returns:
# string
# Method signature:
# def getNext(self, date, birthdays):

# Gendo90 has submitted the 500-point problem for 150.00 points
# Successful on ~6th try...
# There is surely an easier way, probably using a special date object or
# something
class Birthday(object):
    def sortByMonth(self, datestring):
        return int(datestring[0:2])

    def sortByDate(self, datestring):
        return int(datestring[3:5])

    def getNext(self, date, birthdays):
        if(not isinstance(birthdays, tuple)):
            return birthdays[0:5]
        date_list = [l[0:5] for l in birthdays if (int(l[0:2])>=int(date[0:2]))]
        date_list = [l[0:5] for l in date_list if not (int(l[3:5])<int(date[3:5]) and int(l[0:2])==int(date[0:2]))]
        this_date = date.split("/")
        if(not date_list):
            next_bday_month = min(int(l[0:2]) for l in birthdays)
            possible_bdays = [a for a in birthdays if (next_bday_month==int(a[0:2]))]
            if(len(possible_bdays)>1):
                possible_bdays.sort(key=self.sortByDate)
                if(next_bday_month==date[3:5]):
                    possible_bdays = [a for a in possible_bdays if(int(a[3:5])>=int(this_date[1]))]
            return possible_bdays[0][0:5]
        else:
            date_list.sort(key=self.sortByMonth)
            next_bday_month = int(date_list[0][0:2])
            possible_bdays = [a for a in date_list if (next_bday_month==int(a[0:2]))]
            if(len(possible_bdays)>1):
                possible_bdays.sort(key=self.sortByDate)
                if(next_bday_month==date[3:5]):
                    possible_bdays = [a[0:5] for a in possible_bdays if(int(a[3:5])>=int(this_date[1]))]
            return possible_bdays[0]


test = Birthday()

print(test.getNext("11/22", ("11/05 Lelah", "07/18 Stillman", "05/09 Brooks", "05/23 Nolan", "06/04 Cyrillus", "07/02 Neville", "07/28 Goldie", "04/06 Rouvin", "01/03 Eal", "01/05 Christopher", "08/08 Hubey")))
