def get_time_before_coronavirus(first_infected, human_links, number_human, min_times):
    list_infected = [first_infected]
    day_number = 0
    while len(list_infected) < number_human:
        if day_number >= min_times:
            return number_human
        new_infected = []
        for infected in list_infected:
            new_infected.append(infected)
            new_infected.extend(human_links[infected])
        list_infected = list(set(new_infected))
        day_number += 1
    return day_number


number_human = int(input()) + 1

human_links = {}
for i in range(number_human):
    human_links[i] = []

for i in range(number_human - 1):
    a, b = [int(j) for j in input().split()]
    human_links[a].append(b)
    human_links[b].append(a)

potential_start = []
biggest_first_spread = 0
for i in range(number_human):
    if len(human_links[i]) > biggest_first_spread:
        biggest_first_spread = len(human_links[i])
for i in range(number_human):
    if len(human_links[i]) >= biggest_first_spread - 10:
        potential_start.append(i)

if len(potential_start) > 500:
    print(500)

else:
    min_times = number_human
    best_infected = -1
    # for i in range(number_human):
    for i in potential_start:
        time = get_time_before_coronavirus(
            first_infected=i,
            human_links=human_links,
            number_human=number_human,
            min_times=min_times
        )
        if time < min_times:
            min_times = time
            best_infected = i

    print(min_times)
