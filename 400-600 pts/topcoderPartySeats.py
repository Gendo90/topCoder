# Problem Statement
#
# It is time to arrange the seating around a circular table for a party. We want to alternate boys and girls around the table. We have a list of all the attendees and their genders. Each attendee is specified by a string that consists of the name, followed by one space, followed by either "boy" or "girl".
# In addition to the attendees, we need to seat the HOST (a boy) and the HOSTESS (a girl) with the HOSTESS directly across from the HOST. That means that half the attendees should be on the HOST's left, and half on his right.
# Create a class PartySeats that contains a method seating that is given a tuple (string) attendees that lists all the attendees and their genders. The method returns a tuple (string) that gives the seating plan, starting with "HOST" and proceeding clockwise around the table, including all the attendees and the HOSTESS.
# If there is more than one possible seating plan, return the one that comes first lexicographically. "First lexicographically" means that each successive element in the return should be chosen to be the earliest alphabetically that is consistent with a legal seating plan. If there is no legal seating plan, the return should contain 0 elements.
# Definition
#
# Class:
# PartySeats
# Method:
# seating
# Parameters:
# tuple (string)
# Returns:
# tuple (string)
# Method signature:
# def seating(self, attendees):

# Gendo90 has submitted the 550-point problem for 300.51 points
# Successful on second try - tried something too fancy for the not possible
# condition check, should have just looked for leftovers first!
class PartySeats(object):
    def seating(self, attendees):
        all_boys = [a.split(" ")[0] for a in attendees if("boy"==a[-3:])]
        all_boys.sort()
        all_girls = [a.split(" ")[0] for a in attendees if("girl"==a[-4:])]
        all_girls.sort()
        output_order = ["HOST"]

        if(len(all_boys)!=len(all_girls)):
            return tuple()

        num_attendees = len(attendees)

        last_boy = True
        while(all_girls):
            if(num_attendees/2!=len(output_order)-1):
                if(last_boy):
                    output_order.append(all_girls.pop(0))
                    last_boy = False
                else:
                    output_order.append(all_boys.pop(0))
                    last_boy = True
            else:
                output_order.append("HOSTESS")
                last_boy = False
        if(all_boys or all_girls):
            return tuple()

        return tuple(output_order)


test = PartySeats()

print(test.seating(("JOHN boy","CARLA girl")))
