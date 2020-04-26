def sort_string(string):
    return "".join(sorted(string))


rule = {
    sort_string("CP"): "C",
    sort_string("PR"): "P",
    sort_string("RL"): "R",
    sort_string("LS"): "L",
    sort_string("SC"): "S",
    sort_string("CL"): "C",
    sort_string("LP"): "L",
    sort_string("PS"): "P",
    sort_string("SR"): "S",
    sort_string("RC"): "R",
}


def get_winner(player_a, player_b):
    winner = chose_winner(player_a, player_b)
    winner["opp"].append(str(player_a["num"]) if winner["num"] == player_b["num"] else str(player_b["num"]))
    return winner


def chose_winner(player_a, player_b):
    if player_a["sign"] == player_b["sign"]:
        return player_a if player_a["num"] < player_b["num"] else player_b
    winner_sign = rule[sort_string("{}{}".format(player_a["sign"], player_b["sign"]))]
    return player_a if player_a["sign"] == winner_sign else player_b


def play_match(players):
    winners = []
    for i in range(int(len(players) / 2)):
        winners.append(get_winner(
            players[2 * i],
            players[2 * i + 1]
        ))
    return winners


n = int(input())
players = []
for i in range(n):
    numplayer, signplayer = input().split()
    numplayer = int(numplayer)
    players.append({
        "num": numplayer,
        "sign": signplayer,
        "opp": []
    })

while len(players) > 1:
    players = play_match(players)

print(players[0]["num"])
print(" ".join(players[0]["opp"]))
