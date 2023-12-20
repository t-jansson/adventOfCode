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

    print(workflows)
    print("")
    print(ratings)

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
            if work[0][1] == "<":
                if int(rating[work[0][0]]) < int(work[0][2:work[0].index(":")]):
                    if work[work[0].index(":"):] == "A":
                        approved.append(rating)
                    elif work[work[0].index(":"):] == "R":
                        rejected.append(rating)
                    workflow.append([flows[work[work[0].index(":"):]]])
            elif work[0][1] == ">":
                if int(rating[work[0][0]]) > int(work[0][2:work[0].index(":")]):
                    if work[work[0].index(":"):] == "A":
                        approved.append(rating)
                    elif work[work[0].index(":"):] == "R":
                        rejected.append(rating)
                    workflow.append([flows[work[0].index(":"):]])
            else:
                
            pass
