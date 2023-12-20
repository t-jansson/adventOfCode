#Advent of Code 2023 Day 19 - 1

if __name__ == "__main__":

    with open('day19_input.txt') as input:
        input = input.readlines()
    input = [i.strip() for i in input]
    workflows = []
    ratings = []
    for i, workflow in enumerate(input):
        if workflow == "": break
        workflows.append(workflow)
    for i in range(i+1, len(input)):
        ratings.append(input[i])

    flows = {}
    for workflow in workflows:
        workflow = workflow.split("{")
        flows[workflow[0]] = workflow[1].split(",")
        flows[workflow[0]][-1] = flows[workflow[0]][-1].strip("}")

    approved = []
    rejected = []
    for rating in ratings:
        rating = rating[1:-1] #remove {}
        rating = rating.split(",")
        rating = [r.split("=") for r in rating]
        rating = dict(rating)
        workflow = [flows["in"]]
        for work in workflow:
            for w in work:
                if w == "A":
                    approved.append(rating)
                elif w == "R":
                    rejected.append(rating)
                elif w[1] == "<":
                    if int(rating[w[0]]) < int(w[2:w.index(":")]):
                        if w[w.index(":")+1:] == "A":
                            approved.append(rating)
                        elif w[w.index(":")+1:] == "R":
                            rejected.append(rating)
                        else:
                            workflow.append(flows[w[w.index(":")+1:]])
                        break
                elif w[1] == ">":
                    if int(rating[w[0]]) > int(w[2:w.index(":")]):
                        if w[w.index(":")+1:] == "A":
                            approved.append(rating)
                        elif w[w.index(":")+1:] == "R":
                            rejected.append(rating)
                        else:
                            workflow.append(flows[w[w.index(":")+1:]])
                        break
                else:
                    workflow.append(flows[w])

    x = 0
    m = 0
    a = 0
    s = 0
    for items in approved:
        x += int(items["x"])
        m += int(items["m"])
        a += int(items["a"])
        s += int(items["s"])
    
    result = x+m+a+s
    print(result)