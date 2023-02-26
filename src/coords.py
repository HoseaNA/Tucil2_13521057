import random

# Banyaknya penghitungan Euclidean dengan Divide and Conquer dan Brute Force
numOfEucDis = 0
bruteNumEucDis = 0

# Fungsi untuk mengembalikan banyaknya penghitungan Euclidean dengan Divide and Conquer
def getNumOfEucDis():
    return numOfEucDis

# Fungsi untuk mengembalikan banyaknya penghitungan Euclidean dengan Brute Force
def getbruteNumEucDis():
    return bruteNumEucDis

# Fungsi mencari Euclidean Distance untuk Divide and Conquer
def EucDis(p1, p2):
    global numOfEucDis

    distance = 0
    for i in range(len(p1)):
        distance += (p2[i] - p1[i])**2

    numOfEucDis += 1
    return distance**(1/2)

# Fungsi mencari Euclidean Distance untuk Brute Force
def bruteEucDis(p1, p2):
    global bruteNumEucDis

    distance = 0
    for i in range(len(p1)):
        distance += (p2[i] - p1[i])**2

    bruteNumEucDis += 1
    return distance**(1/2)

# Fungsi mempartisi pada algoritma quicksort
def partition(points):
    pivot = points[-1]
    i = 0
    j = len(points) - 1
    while (i < j):
        if (points[i][0] < pivot[0]):
            i += 1
        else:
            j -= 1
            points[i], points[j] = points[j], points[i]
    points[i], points[-1] = points[-1], points[i]
    return points[:i], points[i:]

# Fungsi memulai algoritma quicksort
def quickSort(points):
    if (len(points) <= 1):
        return points
    else:
        leftPart, rightPart = partition(points)
        return quickSort(leftPart) + quickSort(rightPart)

# Fungsi untuk memperoleh posisi semua titik
def getPoints():

    n = int(input("Masukkan jumlah titik (n)    : "))
    dimension = int(input("Masukkan dimensi titik       : "))

    points = [[0 for i in range(dimension)] for j in range(n)]
    for i in range(n):
        for j in range(dimension):
            points[i][j] = random.uniform(-1000, 1000)

    return quickSort(points)
