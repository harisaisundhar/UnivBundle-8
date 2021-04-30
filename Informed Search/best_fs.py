# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from graphviz import Graph


def bfsCalculate(edgeList, straightLine, initialNode, goalNode):
    Open = []
    Closed = []
    traversed = []
    OpenPrint = []
    Cost = 0
    ClosedPrint = [initialNode]
    dot = Graph(comment='Best First Search')
    str1 = ""
    str2 = ""
    currentNode = initialNode
    Open.append(initialNode)
    while(Open):
        for i in Open:
            str1 += i
        OpenPrint.append(str1)
        str1 = ""
        if(currentNode == goalNode):
            break

        # print(Open)
        Closed.append(currentNode)
        for i in Closed:
            str2 += i
        ClosedPrint.append(str2)
        str2 = ""

        # print(Open)

        uniqueFrom = []
        childFrom = edgeList[(edgeList["from"] == currentNode)]
        for i in childFrom['to']:
            if i not in Closed:
                uniqueFrom.append(i)

        uniqueTo = []
        childTo = edgeList[(edgeList['to'] == currentNode)]
        for i in childTo['from']:
            if i not in Closed:
                uniqueTo.append(i)

        childNodes = {}

        for i in uniqueFrom:
            if i not in Open:
                Open.append(i)
                childNodes[i] = list(
                    straightLine[(straightLine['node'] == i)]['cost'])

        for i in uniqueTo:
            if i not in Open:
                Open.append(i)
                childNodes[i] = list(
                    straightLine[(straightLine['node'] == i)]['cost'])

        print(childNodes)
        # print(Open)
        for i in childNodes:
            traversed.append(currentNode+i)
        temp = min(childNodes.values())
        # print(temp)
        res = [key for key in childNodes if childNodes[key] == temp]

        Cost += list(edgeList[(edgeList['from'] == currentNode)
                              & (edgeList['to'] == res[0])]['cost'])[0]

        Open.remove(currentNode)
        dot.node(currentNode, color="red")
        currentNode = res[0]
        # print(Open)
    dot.node(goalNode, color="green")
    # print(traversed)
    dot.edges(traversed)
    dot.attr(label=r"\n\nBest First Search Graph")
    dot.render('output/best_fisrt_search.gv', view=True)
    'output/best_fisrt_search.gv.pdf'
    print("============COST============\n")
    print(Cost)
    print("\n============PATH============\n")

    for i in Closed:
        print(i, '--> ', end="")
    print(goalNode)
    return Closed


edgeList = pd.read_csv('edge_list.csv')
straigtLine = pd.read_csv('straight_line_distance.csv')
# print(straigtLine['node'])

bfsPath = bfsCalculate(edgeList, straigtLine, "A", "R")


# %%
