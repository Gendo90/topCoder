# Problem Statement
#
# You are the coach of a high school cross country team. You are hosting a cross country meet at your school this weekend, and you need to be ready to score the meet. Since it is a bit of a pain to do by hand, especially for large meets, you are going to write a program to do it for you. Given the number of teams and the order in which the runners finish, determine the order in which each team places.  Capital letters will represent the teams in finishOrder and in the return value. The first team is 'A', the second team is 'B', and so on. The place in which the five fastest runners on a team finish is added together (first place=1, second place=2, etc...), and that is the team's score (a team must have at least five runners finish to place). Lower scores beat higher scores, and in the event of a tie the sixth fastest runners of each team are compared, and the team whose sixth fastest runner finished earlier wins the tie. If two teams tie and only one has a sixth runner, that team wins the tie. If two teams tie and neither has a sixth runner, the team who's letter comes first alphabetically wins the tie.  You will be given an integer, numTeams, which is the number of teams competing, and a string, finishOrder, which is the order in which the runners finish. You are to return a string that lists the teams in the order they placed in the meet. If a team has fewer than 5 runners finish, do not include it in the return value.  For example, if finishOrder="AABBABBABBA", then team A's runners finish 1st, 2nd, 5th, 8th, and 11th, for a team score of 27 points. Team B's runners finish 3rd, 4th, 6th, 7th, 9th, and 10th, for a team score of 29 points (notice that only team B's first 5 runners are scored). In this case the return value would be "AB".
# Definition
#
# Class:
# CrossCountry
# Method:
# scoreMeet
# Parameters:
# integer, string
# Returns:
# string
# Method signature:
# def scoreMeet(self, numTeams, finishOrder):



# Gendo90 has submitted the 600-point problem for 289.64 points
# Successful on first try!

import string

class CrossCountry(object):
    def scoreMeet(self, numTeams, finishOrder):
        teams = {}
        for i, runner in enumerate(finishOrder):
            if(not teams.get(runner)):
                teams[runner] = [i+1]
            else:
                teams[runner].append(i+1)

        scores = {}
        team_from_score = {}
        tiebreaker = {}
        for team in teams.keys():
            if(len(teams[team])<5):
                continue
            else:
                scores[team] = sum(teams[team][0:5])
                if(not team_from_score.get(scores[team])):
                    team_from_score[scores[team]] = team
                #check scores to see if they are equal
                else:
                    former_team = team_from_score[scores[team]]
                    if(len(teams[former_team])>5 and len(teams[team])>5):
                        former_team_tiebreaker = sum(teams[former_team][0:6])
                        this_team_tiebreaker = sum(teams[team][0:6])
                        if(former_team_tiebreaker<this_team_tiebreaker):
                            team_from_score[scores[team]] = former_team+team
                        else:
                            team_from_score[scores[team]] = team+former_team
                    elif(len(teams[former_team])>5 and not len(teams[team])>5):
                        team_from_score[scores[team]] = former_team+team
                    elif(not len(teams[former_team])>5 and len(teams[team])>5):
                        team_from_score[scores[team]] = team+former_team
                    else:
                        if(string.ascii_uppercase.find(team)<string.ascii_uppercase.find(former_team)):
                            team_from_score[scores[team]] = team+former_team
                        else:
                            team_from_score[scores[team]] = former_team+team

        score_totals = set(score for score in scores.values())
        score_totals = list(score_totals)
        score_totals.sort()
        # print(score_totals)
        output = "".join([team_from_score[score] for score in score_totals])

        return output



test = CrossCountry()

print(test.scoreMeet(3, "BABCAABABAB"))
