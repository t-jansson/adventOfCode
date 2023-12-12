#Advent of Code 2023 Day 7 - 2

def cardToValue(card):
    match card:
        case "A": return 14
        case "K": return 13
        case "Q": return 12
        case "J": return 1 #J now the weakest
        case "T": return 10
        case _: return int(card)

def assignValueToHand(hand):
    most_common = max(hand, key=hand.count)
    count = hand.count(most_common)
    if most_common == "J": 
        if count == 5: return 7 #Special case all five are jacks
        tempHand = hand.replace("J","")
        most_common = max(tempHand, key=tempHand.count)
    hand = hand.replace("J", most_common)
    # print(hand)
    most_common = max(hand, key=hand.count) #Get new value
    count = hand.count(most_common)
    match count:
        case 5: return 7 #Five of a kind
        case 4: return 6 #Four of a kind
        case 3: #Full house or Three of a kind
            #Check full house
            hand = hand.replace(most_common,"")
            most_common = max(hand, key=hand.count)
            if hand.count(most_common) == 2: return 5
            else: return 4 #Three of a kind
        case 2: #Pair or two pairs
            #Check two pairs
            hand = hand.replace(most_common,"")
            most_common = max(hand, key=hand.count)
            if hand.count(most_common) == 2: return 3
            else: return 2 #Pair
        case 1: return 1 #All different cards
        case _: return 0 #Should never happen

def compareHands(h1, h2):
    if h1["value"] > h2["value"]: return h1
    if h1["value"] < h2["value"]: return h2
    for i in range(0,len(h1["hand"])):
        if cardToValue(h1["hand"][i]) > cardToValue(h2["hand"][i]): return h1
        if cardToValue(h1["hand"][i]) < cardToValue(h2["hand"][i]): return h2
    print("THE SAME!!!") #Should never happen
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

    with open('day7_input.txt') as input:
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