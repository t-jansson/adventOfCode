#Advent of Code 2023 Day 7 - 1

def cardToValue(card):
    match card:
        case "A": return 14
        case "K": return 13
        case "Q": return 12
        case "J": return 11
        case "T": return 10
        case _: return int(card)

def assignValueToHand(hand):
    most_common = max(hand, key=hand.count)
    count = hand.count(most_common)
    match count:
        case 5: return 7
        case 4: return 6
        case 3: 
            #Check full house
            hand = hand.replace(most_common,"")
            most_common = max(hand, key=hand.count)
            if hand.count(most_common) == 2: return 5
            else: return 4
        case 2:
            #Check two pair
            hand = hand.replace(most_common,"")
            most_common = max(hand, key=hand.count)
            if hand.count(most_common) == 2: return 3
            else: return 2
        case 1: return 1
        case _: return 0

def compareHands(h1, h2):
    if h1["value"] > h2["value"]: return h1
    if h1["value"] < h2["value"]: return h2
    for i in range(0,len(h1["hand"])):
        if cardToValue(h1["hand"][i]) > cardToValue(h2["hand"][i]): return h1
        if cardToValue(h1["hand"][i]) < cardToValue(h2["hand"][i]): return h2
    print("THE SAME!!!")
    return h1

def sortHands(hands):
    for i in range(0,len(hands)):
        for j in range(i+1,len(hands)):
            if hands[i]["hand"] != compareHands(hands[i], hands[j])["hand"]: swapPositions(hands, i, j)

def swapPositions(list, p1, p2):
    ls = list[p1], list[p2]
    list[p2], list[p1] = ls
    return list

def getValueFromHand(hand):
    return hand["value"]

if __name__ == "__main__":

    with open('input.txt') as input:
        input = input.readlines()
        input = [x.split() for x in input]

    hands = []
    for cards, rank in input:
        hand = {}
        hand["hand"] = cards
        hand["rank"] = int(rank)
        hand["value"] = assignValueToHand(cards)
        hands.append(hand)

    hands.sort(key=getValueFromHand, reverse=True)
    sortHands(hands)
    hands.reverse()

    result = 0
    for i in range(0, len(hands)):
        # print(i+1, hands[i], hands[i]["rank"] * (i+1))
        result += hands[i]["rank"] * (i+1)

    print(result)