import numpy
import math
import matplotlib.pyplot as plt

# import random

print("RRT algorithm!")

#dimesion grid
D=[0,100] 
# iterations
K = 2000
#Starting position
Qstart = [50.0,50.0]
d = 1
vertices = []
edges = []

def draw():
    xAxis=[]
    yAxis=[]
    for vert in vertices:
        xAxis.append(vert[0])
        yAxis.append(vert[1])

    plt.plot(xAxis, yAxis, '.')
    plt.axis([0, 100, 0, 100])

    # for ed in edges:
    #     pt1 = vertices[ed[0]]
    #     pt2 = vertices[ed[1]]
    #     plt.plot([pt1[0],pt2[0]], [pt1[1],pt2[1]], 'ro-')

    # plt.axis([0, 100, 0, 100])
    plt.show()



def getDist(point1,point2):
    return math.sqrt(pow(point1[0]-point2[0],2) + pow(point1[1]-point2[1],2))


def NEAREST_VERTEX(point):
    global vertices
    minDist = 10000.0
    minId = -1 
    for id_temp in range(len(vertices)):
        dist = getDist(vertices[id_temp], point)
        if(minDist>dist):
            minDist = dist
            minId = id_temp
    if(minId==-1):
        print("Error in NEAREST_VERTEX")
    return [minId,minDist]


if __name__ == "__main__":
    numpy.random.seed()
    vertices.append(Qstart)
    # vertices.append([20,50])
    for i in range(K):
        #create random q within D
        Qnew = [numpy.random.rand()*D[1],numpy.random.rand()*D[1]]
        # Qnew = [50,80]

        #find nearest neighbor
        data_dist = NEAREST_VERTEX(Qnew)
        Qnear = vertices[data_dist[0]]

        #add new vertex
        x2=(Qnear[0] - Qnew[0])/data_dist[1]
        y2=(Qnear[1] - Qnew[1])/data_dist[1]
        x = (Qnew[0] - Qnear[0])/data_dist[1]*d
        y = (Qnew[1] - Qnear[1])/data_dist[1]*d
        if x > d: 
            print ("X Error :" + str(x))
        if y > d: 
            print ("y Error :" + str(y))

        Qnext = [x+Qnear[0],y+Qnear[1]]
        vertices.append(Qnext)
        edges.append([data_dist[0],len(vertices)-1])
    draw()


# for vert in vertices:
#     print (vert)
# print ("(******)(******)(******)(******)")
# print(edges)
