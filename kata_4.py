import re
def parse_weather():
    source = open('./weather.dat', 'r')
    days = []
    for line in source:
        splitted = line.strip().split()
        days.append(splitted)
        # days.append(re.findall('\d+', line))
    source.close()
    # print(days)
    days.pop()
    days.pop(0)
    days.pop(0)
    return days

def minimum_delta_t():
    weather_data = parse_weather()
    spreads = []
    for day in weather_data:
        date = int(day[0])
        number= '\d*'
        high = re.findall(number, day[1])[0]
        low = re.findall(number, day[2])[0]
        spread = int(high) - int(low)
        spreads.append([date,spread])
    ranked_spreads = sorted(spreads, key=lambda day: day[1])
    return ranked_spreads[0][0]

def parse_sports():
    source = open('./football.dat')
    teams = []
    for line in source:
        # teams.append(re.findall('\d+\.? ?\w*',line))
        teams.append(re.findall('\d+\. \w*|\d+',line))
    source.close()
    teams.pop(0)
    teams.pop(-4)
    return teams

def minimum_delta_score():
    team_data = parse_sports()
    spreads = []
    for team in team_data:
        spreads.append([team[0], abs(int(team[5])-int(team[6]))])
    return sorted(spreads, key=lambda team: team[1])[0][0]

def generic_parse(file_address):
    source = open(file_address, 'r')
    data = []
    for line in source:
        if len(line.strip()) ==0:
            continue
        if not re.match('\d', line.strip()[0]):
            continue
        data.append(re.findall('\d+\. \w*|\d+',line))
        if len(data[-1])<3:
            data.pop()
    source.close()
    return data

def generic_comparisons(data, id_index, a_index, b_index):
    comparisons = []
    for entry in data:
        comparisons.append(
            [
                entry[id_index],
                abs(int(entry[a_index])-int(entry[b_index]))
            ]
            )
    return comparisons

def min_element_id(list_of_pairs):
    #pairs are structured with id, value
    return sorted(list_of_pairs, key=lambda pair: pair[1])[0][0]


def min_delta_tem_2():
    dates = generic_parse('./weather.dat')
    temp_spreads = generic_comparisons(dates, id_index=0, a_index=1, b_index=2)
    return min_element_id(temp_spreads)

def min_score_spread_2():
    teams = generic_parse('./football.dat')
    score_spreads = generic_comparisons(teams, id_index=0, a_index=5, b_index=6)
    return min_element_id(score_spreads)

print(minimum_delta_t())
print(minimum_delta_score())

print(min_delta_tem_2())
print(min_score_spread_2())

'''
reflections
To what extent did the design decisions you made when writing the original programs make it easier or harder to factor out common code?
Refactoring was conceptually easy, the harder details was making a parser that would work equally well on both data sets.


Was the way you wrote the second program influenced by writing the first?
My use of regex I think made the following one easier.

Is factoring out as much common code as possible always a good thing? Did the readability of the programs suffer because of this requirement? How about the maintainability?
I think the readability improved because I made a stronger effort to make functions that handled discrete tasks.

'''
