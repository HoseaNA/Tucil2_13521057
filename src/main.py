import coords
import visualizer
import time
import sys


def checkAllDimension(point1, point2, minDis):
    for i in range(len(point1)):
        if (abs(point1[i] - point2[i]) > minDis):
            return False
    return True


def findClosestPairStrip(points, currMinDis):
    min = currMinDis[0]
    p1 = currMinDis[1]
    p2 = currMinDis[2]
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (checkAllDimension(points[i], points[j], min)):
                distance = coords.EucDis(points[i], points[j])
                if (distance < min):
                    min = distance
                    p1 = points[i]
                    p2 = points[j]

    return (min, p1, p2)


def findClosestPair(points):

    if (len(points) == 2):
        return (coords.EucDis(points[0], points[1]), points[0], points[1])
    elif (len(points) == 3):
        d1 = coords.EucDis(points[0], points[1])
        d2 = coords.EucDis(points[1], points[2])
        d3 = coords.EucDis(points[0], points[2])
        if (d1 >= d2 >= d3):
            return (d3, points[0], points[2])
        elif (d2 >= d1 >= d3):
            return (d3, points[0], points[2])
        elif (d1 >= d3 >= d2):
            return (d2, points[1], points[2])
        elif (d3 >= d1 >= d2):
            return (d2, points[1], points[2])
        elif (d2 >= d3 >= d1):
            return (d1, points[0], points[1])
        elif (d3 >= d2 >= d1):
            return (d1, points[0], points[1])
    else:
        n1 = len(points)//2
        left = points[:n1]
        right = points[n1:]

        d1 = findClosestPair(left)
        d2 = findClosestPair(right)

        if (d1[0] < d2[0]):
            minDistance = d1
        else:
            minDistance = d2

        d3 = findClosestPairStrip(points, minDistance)
        if (d3[0] < minDistance[0]):
            return d3
        else:
            return minDistance


def main():
    sys.setrecursionlimit(10000)
    print("")
    print("=======================================================================================")
    print("Mencari Pasangan Titik Terdekat 3D")
    print("dengan Algoritma Divide and Conquer")
    print("")
    print("By Hosea Nathanael Abetnego - 13521057")
    print("=======================================================================================")
    print("")
    points = coords.getPoints()

    start_time = time.time()
    closestPoints = findClosestPair(coords.quickSort(points))
    end_time = time.time()

    print("")
    print("Results")
    print("Distance                     : ", closestPoints[0])
    print("Point 1                      : ", closestPoints[1])
    print("Point 2                      : ", closestPoints[2])
    print("Banyak perhitungan Euclidean : ", coords.getNumOfEucDis())
    print("Runtime                      : ", end_time - start_time, "detik")
    if (len(points[0]) == 3):
        print("Visualizing")
        visualizer.visualize(points, closestPoints)
    else:
        print("Dimension not supported, no visualization")


main()
