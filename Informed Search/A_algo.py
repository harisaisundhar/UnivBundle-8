# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from graphviz import Graph


def A_Algo(edgeList, straightLine, initialNode, goalNode):
    Closed = []
    Open1 = []
    Open1.append(initialNode)
    dot = Graph(comment='A* Algo')
    pathCost = []
    edgeCost = 0
    Path = ''
    Cost = 0
    traversed = []
    Open = {}
    Open[list(straightLine[(straightLine['node'] == initialNode)]['node'])[0]] = list(
        straightLine[(straightLine['node'] == initialNode)]['cost'])[0]
    # print(pathCost)
    count = 0
    currentNode = initialNode
    currentPathCost = initialNode
    while(Open1 or currentNode == ''):
        del Open[currentNode]
        Open1.pop(0)

        Closed.append(currentNode)
        # print(Closed)
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

        childNodePath = []
        #childNodeCost = []
        # print(currentNode)
        for i in uniqueFrom:
            traversed.append(currentNode+i)
            Open1.append(i)
            Open[i] = list(edgeList[(edgeList['from'] == currentNode) & (edgeList['to'] == i)]['cost'])[
                0]+list(straightLine[(straightLine['node'] == i)]['cost'])[0]+edgeCost
            childNodePath = [currentPathCost+i, list(edgeList[(edgeList['from'] == currentNode) & (edgeList['to'] == i)]['cost'])[0]+edgeCost, list(
                edgeList[(edgeList['from'] == currentNode) & (edgeList['to'] == i)]['cost'])[0]+list(straightLine[(straightLine['node'] == i)]['cost'])[0]+edgeCost]
            pathCost.append(childNodePath)
            childNodePath = []

        for i in uniqueTo:
            traversed.append(currentNode+i)
            Open1.append(i)
            Open[i] = list(edgeList[(edgeList['to'] == currentNode) & (edgeList['from'] == i)]['cost'])[
                0]+list(straightLine[(straightLine['node'] == i)]['cost'])[0]+edgeCost
            childNodePath = [currentPathCost+i, list(edgeList[(edgeList['to'] == currentNode) & (edgeList['from'] == i)]['cost'])[0]+edgeCost, list(
                edgeList[(edgeList['to'] == currentNode) & (edgeList['from'] == i)]['cost'])[0]+list(straightLine[(straightLine['node'] == i)]['cost'])[0]+edgeCost]
            pathCost.append(childNodePath)
            childNodePath = []

        # print(pathCost)
        # print(Open)
        pathCost.sort(key=lambda x: x[2])
        Open = dict(sorted(Open.items(), key=lambda item: item[1]))
        #print("After Sort")
        # print(pathCost)
        # print(Open)
        # print(Open1)
        currentNode = list(Open.keys())[0]
        # print(currentNode)
        currentPathCost = pathCost[0][0]
        Cost = pathCost[0][2]
        edgeCost = pathCost[0][1]
        if(currentNode == goalNode):
            break
        Path = currentPathCost
        # print(edgeCost)
        pathCost.pop(0)
        # print("=================================")
    # print(Closed)
    for i in Path:
        dot.node(i, color="red")
    dot.node(goalNode, color="green")
    dot.edges(traversed)
    dot.attr(label=r"\n\n A* Algorithm Graph")
    dot.render('output/A*_Algo.gv', view=True)
    'output/A*_Algo.gv.pdf'
    print("============COST============")
    print(Cost)
    return Path


edgeList = pd.read_csv('edge_list.csv')
straigtLine = pd.read_csv('straight_line_distance.csv')
# print(straigtLine['node'])

A_Algo_Path = A_Algo(edgeList, straigtLine, "A", "R")
goalNode = 'R'
print("============PATH============")
# print(A_Algo_Path)
for i in range(0, len(A_Algo_Path)):
    print(A_Algo_Path[i], '--> ', end="")
print(goalNode)


# %%
