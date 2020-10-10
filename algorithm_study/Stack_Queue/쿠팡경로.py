import heapq

roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]
node = []
for road in roads:
    x, y = road
    node.append(x)
    node.append(y)
node = set(node)
num = len(node)

graph = [[i]*(num+1) for i in range(num+1)]

for road in roads:
    x, y = road
    for i in graph:
        if x == i[0]:
            i.extend([y])

print(graph)
# graph = [[i] for i in node]
# print(graph)
#
# for road in roads:
#     x, y = road
#     for i in graph:
#         if x == i[0]:
#             i.extend([y])
#
#
# print(graph)
# def dij(depart, arrive):
#     q = []
#     dist = [0] * num
#     heapq.heappush(q,(0,depart))
#     dist[depart] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         for nd, ndist in graph[now]:
#             ndist += dist
#             if dist[nd]
#
