import pandas
import csv
import os

def prizepicks_6_legs_flex(wager, odds):
    #calculate EV
    value_win_6 = wager * 24
    odds_win_6 = 1
    for i in range(len(odds)):
        odds_win_6 *= odds[i]
    value_win_6 *= odds_win_6
    
    value_win_5 = wager
    odds_win_5 = 0
    for i in range(len(odds)):
        temp = 1 - odds[i]
        for n in range(len(odds)):
            if n == i:
                continue
            temp *= odds[n]
        odds_win_5 += temp
    value_win_5 *= odds_win_5
    
    value_win_4 = 0.6 * wager * -1
    odds_win_4 = 0
    for i in range(len(odds)):
        temp_1 = 1 - odds[i]
        for n in range(len(odds)):
            if n <= i:
                continue
            temp_2 = (1 - odds[n]) * temp_1
            for j in range(len(odds)):
                if j == i or j == n:
                    continue
                temp_2 *= odds[j]
            odds_win_4 += temp_2
    value_win_4 *= odds_win_4
    
    value_win_3 = wager * -1
    odds_win_3 = 0
    for i in range(len(odds)):
        temp_1 = 1 - odds[i]
        for n in range(len(odds)):
            if n <= i:
                continue
            temp_2 = (1 - odds[n]) * temp_1
            for j in range(len(odds)):
                if j <= n:
                    continue
                temp_3 = (1 - odds[j]) * temp_2
                for k in range(len(odds)):
                    if k == i or k == n or k == j:
                        continue
                    temp_3 *= odds[k]
                odds_win_3 += temp_3
    value_win_3 *= odds_win_3
    
    odds_inverse = []
    for i in range(len(odds)):
        odds_inverse.append(1 - odds[i])
    
    value_win_2 = wager * -1
    odds_win_2 = 0
    for i in range(len(odds_inverse)):
        temp_1 = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n <= i:
                continue
            temp_2 = (1 - odds_inverse[n]) * temp_1
            for j in range(len(odds_inverse)):
                if j == i or j == n:
                    continue
                temp_2 *= odds_inverse[j]
            odds_win_2 += temp_2
    value_win_2 *= odds_win_2
    
    value_win_1 = wager * -1
    odds_win_1 = 0
    for i in range(len(odds_inverse)):
        temp = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n == i:
                continue
            temp *= odds_inverse[n]
        odds_win_1 += temp
    value_win_1 *= odds_win_1
    
    value_win_0 = wager * -1
    odds_win_0 = 1
    for i in range(len(odds_inverse)):
        odds_win_0 *= odds_inverse[i]
    value_win_0 *= odds_win_0
    
    ev = value_win_0 + value_win_1 + value_win_2 + value_win_3 + value_win_4 + value_win_5 + value_win_6
    print("$" + str(wager) + " 6-legs flex play with implied odds: " + str(odds))
    print("Chance to win 6/6 (PnL $" + str(wager * 24) + "): " + str(odds_win_6))
    print("Chance to win 5/6 (PnL $" + str(wager) + "): " + str(odds_win_5))
    print("Chance to win 4/6 (PnL $" + str(wager * -0.6) + "): " + str(odds_win_4))
    print("Chance to lose (PnL $" + str(wager * -1) + "): " + str(odds_win_3 + odds_win_2 + odds_win_1 + odds_win_0))
    print("Expected PnL: $" + str(ev))
    print()
    return ev, "6-legs flex"

def prizepicks_5_legs_flex(wager, odds):
    #calculate EV
    value_win_5 = wager * 9
    odds_win_5 = 1
    for i in range(len(odds)):
        odds_win_5 *= odds[i]
    value_win_5 *= odds_win_5
    
    value_win_4 = wager
    odds_win_4 = 0
    for i in range(len(odds)):
        temp = 1 - odds[i]
        for n in range(len(odds)):
            if n == i:
                continue
            temp *= odds[n]
        odds_win_4 += temp
    value_win_4 *= odds_win_4
    
    value_win_3 = 0.6 * wager * -1
    odds_win_3 = 0
    for i in range(len(odds)):
        temp_1 = 1 - odds[i]
        for n in range(len(odds)):
            if n <= i:
                continue
            temp_2 = (1 - odds[n]) * temp_1
            for j in range(len(odds)):
                if j == i or j == n:
                    continue
                temp_2 *= odds[j]
            odds_win_3 += temp_2
    value_win_3 *= odds_win_3
    
    odds_inverse = []
    for i in range(len(odds)):
        odds_inverse.append(1 - odds[i])
    
    value_win_2 = wager * -1
    odds_win_2 = 0
    for i in range(len(odds_inverse)):
        temp_1 = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n <= i:
                continue
            temp_2 = (1 - odds_inverse[n]) * temp_1
            for j in range(len(odds_inverse)):
                if j == i or j == n:
                    continue
                temp_2 *= odds_inverse[j]
            odds_win_2 += temp_2
    value_win_2 *= odds_win_2
    
    value_win_1 = wager * -1
    odds_win_1 = 0
    for i in range(len(odds_inverse)):
        temp = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n == i:
                continue
            temp *= odds_inverse[n]
        odds_win_1 += temp
    value_win_1 *= odds_win_1
    
    value_win_0 = wager * -1
    odds_win_0 = 1
    for i in range(len(odds_inverse)):
        odds_win_0 *= odds_inverse[i]
    value_win_0 *= odds_win_0
    
    ev = value_win_0 + value_win_1 + value_win_2 + value_win_3 + value_win_4 + value_win_5
    print("$" + str(wager) + " 5-legs flex play with implied odds: " + str(odds))
    print("Chance to win 5/5 (PnL $" + str(wager * 9) + "): " + str(odds_win_5))
    print("Chance to win 4/5 (PnL $" + str(wager) + "): " + str(odds_win_4))
    print("Chance to win 3/5 (PnL $" + str(wager * -0.6) + "): " + str(odds_win_3))
    print("Chance to lose (PnL $" + str(wager * -1) + "): " + str(odds_win_2 + odds_win_1 + odds_win_0))
    print("Expected PnL: $" + str(ev))
    print()
    return ev, "5-legs flex"

def prizepicks_4_legs_flex(wager, odds):
    #calculate EV
    value_win_4 = wager * 4
    odds_win_4 = 1
    for i in range(len(odds)):
        odds_win_4 *= odds[i]
    value_win_4 *= odds_win_4
    
    value_win_3 = wager * 0.5
    odds_win_3 = 0
    for i in range(len(odds)):
        temp = 1 - odds[i]
        for n in range(len(odds)):
            if n == i:
                continue
            temp *= odds[n]
        odds_win_3 += temp
    value_win_3 *= odds_win_3
    
    value_win_2 = wager * -1
    odds_win_2 = 0
    for i in range(len(odds)):
        temp_1 = 1 - odds[i]
        for n in range(len(odds)):
            if n <= i:
                continue
            temp_2 = (1 - odds[n]) * temp_1
            for j in range(len(odds)):
                if j == i or j == n:
                    continue
                temp_2 *= odds[j]
            odds_win_2 += temp_2
    value_win_2 *= odds_win_2
    
    odds_inverse = []
    for i in range(len(odds)):
        odds_inverse.append(1 - odds[i])
    
    value_win_1 = wager * -1
    odds_win_1 = 0
    for i in range(len(odds_inverse)):
        temp = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n == i:
                continue
            temp *= odds_inverse[n]
        odds_win_1 += temp
    value_win_1 *= odds_win_1
    
    value_win_0 = wager * -1
    odds_win_0 = 1
    for i in range(len(odds_inverse)):
        odds_win_0 *= odds_inverse[i]
    value_win_0 *= odds_win_0
    
    ev = value_win_0 + value_win_1 + value_win_2 + value_win_3 + value_win_4
    print("$" + str(wager) + " 4-legs flex play with implied odds: " + str(odds))
    print("Chance to win 4/4 (PnL $" + str(wager * 4) + "): " + str(odds_win_4))
    print("Chance to win 3/4 (PnL $" + str(wager * 0.5) + "): " + str(odds_win_3))
    print("Chance to lose (PnL $" + str(wager * -1) + "): " + str(odds_win_2 + odds_win_1 + odds_win_0))
    print("Expected PnL: $" + str(ev))
    print()
    return ev, "4-legs flex"

def prizepicks_4_legs_power(wager, odds):
    #calculate EV
    value_win_4 = wager * 9
    odds_win_4 = 1
    for i in range(len(odds)):
        odds_win_4 *= odds[i]
    value_win_4 *= odds_win_4
    
    value_win_3 = wager * -1
    odds_win_3 = 0
    for i in range(len(odds)):
        temp = 1 - odds[i]
        for n in range(len(odds)):
            if n == i:
                continue
            temp *= odds[n]
        odds_win_3 += temp
    value_win_3 *= odds_win_3
    
    value_win_2 = wager * -1
    odds_win_2 = 0
    for i in range(len(odds)):
        temp_1 = 1 - odds[i]
        for n in range(len(odds)):
            if n <= i:
                continue
            temp_2 = (1 - odds[n]) * temp_1
            for j in range(len(odds)):
                if j == i or j == n:
                    continue
                temp_2 *= odds[j]
            odds_win_2 += temp_2
    value_win_2 *= odds_win_2
    
    odds_inverse = []
    for i in range(len(odds)):
        odds_inverse.append(1 - odds[i])
    
    value_win_1 = wager * -1
    odds_win_1 = 0
    for i in range(len(odds_inverse)):
        temp = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n == i:
                continue
            temp *= odds_inverse[n]
        odds_win_1 += temp
    value_win_1 *= odds_win_1
    
    value_win_0 = wager * -1
    odds_win_0 = 1
    for i in range(len(odds_inverse)):
        odds_win_0 *= odds_inverse[i]
    value_win_0 *= odds_win_0
    
    ev = value_win_0 + value_win_1 + value_win_2 + value_win_3 + value_win_4
    print("$" + str(wager) + " 4-legs power play with implied odds: " + str(odds))
    print("Chance to win 4/4 (PnL $" + str(wager * 9) + "): " + str(odds_win_4))
    print("Chance to lose (PnL $" + str(wager * -1) + "): " + str(odds_win_3 + odds_win_2 + odds_win_1 + odds_win_0))
    print("Expected PnL: $" + str(ev))
    print()
    return ev, "4-legs power"

def prizepicks_3_legs_flex(wager, odds):
    #calculate EV
    value_win_3 = wager * 1.25
    odds_win_3 = 1
    for i in range(len(odds)):
        odds_win_3 *= odds[i]
    value_win_3 *= odds_win_3
    
    value_win_2 = wager * 0.25
    odds_win_2 = 0
    for i in range(len(odds)):
        temp = 1 - odds[i]
        for n in range(len(odds)):
            if n == i:
                continue
            temp *= odds[n]
        odds_win_2 += temp
    value_win_2 *= odds_win_2
    
    odds_inverse = []
    for i in range(len(odds)):
        odds_inverse.append(1 - odds[i])
    
    value_win_1 = wager * -1
    odds_win_1 = 0
    for i in range(len(odds_inverse)):
        temp = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n == i:
                continue
            temp *= odds_inverse[n]
        odds_win_1 += temp
    value_win_1 *= odds_win_1
    
    value_win_0 = wager * -1
    odds_win_0 = 1
    for i in range(len(odds_inverse)):
        odds_win_0 *= odds_inverse[i]
    value_win_0 *= odds_win_0
    
    ev = value_win_0 + value_win_1 + value_win_2 + value_win_3
    print("$" + str(wager) + " 3-legs flex play with implied odds: " + str(odds))
    print("Chance to win 3/3 (PnL $" + str(wager * 1.25) + "): " + str(odds_win_3))
    print("Chance to win 2/3 (PnL $" + str(wager * 0.25) + "): " + str(odds_win_2))
    print("Chance to lose (PnL $" + str(wager * -1) + "): " + str(odds_win_1 + odds_win_0))
    print("Expected PnL: $" + str(ev))
    print()
    return ev, "3-legs flex"

def prizepicks_3_legs_power(wager, odds):
    #calculate EV
    value_win_3 = wager * 4
    odds_win_3 = 1
    for i in range(len(odds)):
        odds_win_3 *= odds[i]
    value_win_3 *= odds_win_3
    
    value_win_2 = wager * -1
    odds_win_2 = 0
    for i in range(len(odds)):
        temp = 1 - odds[i]
        for n in range(len(odds)):
            if n == i:
                continue
            temp *= odds[n]
        odds_win_2 += temp
    value_win_2 *= odds_win_2
    
    odds_inverse = []
    for i in range(len(odds)):
        odds_inverse.append(1 - odds[i])
    
    value_win_1 = wager * -1
    odds_win_1 = 0
    for i in range(len(odds_inverse)):
        temp = 1 - odds_inverse[i]
        for n in range(len(odds_inverse)):
            if n == i:
                continue
            temp *= odds_inverse[n]
        odds_win_1 += temp
    value_win_1 *= odds_win_1
    
    value_win_0 = wager * -1
    odds_win_0 = 1
    for i in range(len(odds_inverse)):
        odds_win_0 *= odds_inverse[i]
    value_win_0 *= odds_win_0
    
    ev = value_win_0 + value_win_1 + value_win_2 + value_win_3
    print("$" + str(wager) + " 3-legs power play with implied odds: " + str(odds))
    print("Chance to win 3/3 (PnL $" + str(wager * 4) + "): " + str(odds_win_3))
    print("Chance to lose (PnL $" + str(wager * -1) + "): " + str(odds_win_2 + odds_win_1 + odds_win_0))
    print("Expected PnL: $" + str(ev))
    print()
    return ev, "3-legs power"

def prizepicks_2_legs_power(wager, odds):
    #calculate EV
    value_win_2 = wager * 2
    odds_win_2 = 1
    for i in range(len(odds)):
        odds_win_2 *= odds[i]
    value_win_2 *= odds_win_2
    
    value_win_1 = wager * -1
    odds_win_1 = 0
    for i in range(len(odds)):
        temp = 1 - odds[i]
        for n in range(len(odds)):
            if n == i:
                continue
            temp *= odds[n]
        odds_win_1 += temp
    value_win_1 *= odds_win_1
    
    odds_inverse = []
    for i in range(len(odds)):
        odds_inverse.append(1 - odds[i])
    
    value_win_0 = wager * -1
    odds_win_0 = 1
    for i in range(len(odds_inverse)):
        odds_win_0 *= odds_inverse[i]
    value_win_0 *= odds_win_0
    
    ev = value_win_0 + value_win_1 + value_win_2
    print("$" + str(wager) + " 2-legs power play with implied odds: " + str(odds))
    print("Chance to win 2/2 (PnL $" + str(wager * 2) + "): " + str(odds_win_2))
    print("Chance to lose (PnL $" + str(wager * -1) + "): " + str(odds_win_1 + odds_win_0))
    print("Expected PnL: $" + str(ev))
    print()
    return ev, "2-legs power"

def sort_plays(plays):
    plays.sort(key = lambda x: x[0], reverse=True)
    return plays

def main():
    input_fname = "All-Sports_PrizePicks Optimizer.csv"
    output_fname = "dgf.csv"

    with open(input_fname, newline='') as inFile, open(output_fname, 'w', newline='') as outFile:
        r = csv.reader(inFile)
        w = csv.writer(outFile)

        next(r, None)
        w.writerow(['First Name', 'Last Name', 'Sport', 'Team', 'Over/Under', 'Prop', 'PrizePicks Line',
        'Sportsbook Line', 'DGF', 'Pinnacle', 'Fanduel', 'DraftKings', 'Barstool', 'MGM', 'Caesars',
        'BetOnline', 'Bovada', 'Bet365', 'FoxBet', 'Odds to hit'])

        for row in r:
            w.writerow(row)

    data = pandas.read_csv('dgf.csv')
    top_lines = data.iloc [[0,1,2,3,4,5]]
    print(top_lines)
    odds = top_lines['Odds to hit'].tolist()

    plays_6 = top_lines.iloc [[0,1,2,3,4,5], [0,1,4,5,6]]
    plays_5 = top_lines.iloc [[0,1,2,3,4], [0,1,4,5,6]]
    plays_4 = top_lines.iloc [[0,1,2,3], [0,1,4,5,6]]
    plays_3 = top_lines.iloc [[0,1,2], [0,1,4,5,6]]
    plays_2 = top_lines.iloc [[0,1], [0,1,4,5,6]]

    for i in range(len(odds)):
        odds[i] = odds[i]/100

    wager = 100
    plays = []
    pp_6_legs_flex = prizepicks_6_legs_flex(wager, odds)
    pp_6_legs_flex_ev = pp_6_legs_flex[0]
    plays.append(pp_6_legs_flex)

    pp_5_legs_flex = prizepicks_5_legs_flex(wager, odds[:5])
    pp_5_legs_flex_ev = pp_5_legs_flex[0]
    plays.append(pp_5_legs_flex)

    pp_4_legs_flex = prizepicks_4_legs_flex(wager, odds[:4])
    pp_4_legs_flex_ev = pp_4_legs_flex[0]
    plays.append(pp_4_legs_flex)

    pp_4_legs_power = prizepicks_4_legs_power(wager, odds[:4])
    pp_4_legs_power_ev = pp_4_legs_power[0]
    plays.append(pp_4_legs_power)

    pp_3_legs_flex = prizepicks_3_legs_flex(wager, odds[:3])
    pp_3_legs_flex_ev = pp_3_legs_flex[0]
    plays.append(pp_3_legs_flex)

    pp_3_legs_power = prizepicks_3_legs_power(wager, odds[:3])
    pp_3_legs_power_ev = pp_3_legs_power[0]
    plays.append(pp_3_legs_power)

    pp_2_legs_power = prizepicks_2_legs_power(wager, odds[:2])
    pp_2_legs_power_ev = pp_2_legs_power[0]
    plays.append(pp_2_legs_power)
    
    outputs = []

    output_6_flex = ""
    output_6_flex += "$" + str(wager) + " 6-legs flex play expected PnL: $" + str(float("{:.2f}".format(pp_6_legs_flex_ev))) + "\n"
    output_6_flex += str(plays_6)
    output_6_flex += "\n"
    tup_6_flex = (pp_6_legs_flex_ev, output_6_flex)
    outputs.append(tup_6_flex)

    output_5_flex = ""
    output_5_flex += "$" + str(wager) + " 5-legs flex play expected PnL: $" + str(float("{:.2f}".format(pp_5_legs_flex_ev))) + "\n"
    output_5_flex += str(plays_5)
    output_5_flex += "\n"
    tup_5_flex = (pp_5_legs_flex_ev, output_5_flex)
    outputs.append(tup_5_flex)

    output_4_flex = ""
    output_4_flex += "$" + str(wager) + " 4-legs flex play expected PnL: $" + str(float("{:.2f}".format(pp_4_legs_flex_ev))) + "\n"
    output_4_flex += str(plays_4)
    output_4_flex += "\n"
    tup_4_flex = (pp_4_legs_flex_ev, output_4_flex)
    outputs.append(tup_4_flex)

    output_4_power = ""
    output_4_power += "$" + str(wager) + " 4-legs power play expected PnL: $" + str(float("{:.2f}".format(pp_4_legs_power_ev))) + "\n"
    output_4_power += str(plays_4)
    output_4_power += "\n"
    tup_4_power = (pp_4_legs_power_ev, output_4_power)
    outputs.append(tup_4_power)

    output_3_flex = ""
    output_3_flex += "$" + str(wager) + " 3-legs flex play expected PnL: $" + str(float("{:.2f}".format(pp_3_legs_flex_ev))) + "\n"
    output_3_flex += str(plays_3)
    output_3_flex += "\n"
    tup_3_flex = (pp_3_legs_flex_ev, output_3_flex)
    outputs.append(tup_3_flex)

    output_3_power = ""
    output_3_power += "$" + str(wager) + " 3-legs power play expected PnL: $" + str(float("{:.2f}".format(pp_3_legs_power_ev))) + "\n"
    output_3_power += str(plays_3)
    output_3_power += "\n"
    tup_3_power = (pp_3_legs_power_ev, output_3_power)
    outputs.append(tup_3_power)

    output_2_power = ""
    output_2_power += "$" + str(wager) + " 2-legs power play expected PnL: $" + str(float("{:.2f}".format(pp_2_legs_power_ev))) + "\n"
    output_2_power += str(plays_2)
    output_2_power += "\n"
    tup_2_power = (pp_2_legs_power_ev, output_2_power)
    outputs.append(tup_2_power)

    sort_plays(outputs)
    for i in range(len(outputs)):
        print(outputs[i][1])

if __name__ == "__main__":
    main()