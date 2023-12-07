import sys
import math
from operator import attrgetter, itemgetter
# start by reading in all the clusters, i will make a point class that will hold x and y coordinates. 
# then calculate the distances between all the points, these will not change (until we make clustes) as the points don't move

# to form a new cluster, find the two points that are closest to each other by distance. Put them together.

# we "recalculate" distance when we form a new cluster, but only from the new cluster to all the other points and clusters.
# The one's that haven't formed new clusters don't need to update with each other
#  lets say we have a newly formed cluster c1 (holding p1 and p2) and a point n1 that is not in the cluster
#    the new distance is calculated by taking the distance of lesser value of those between p1 & n1  and  p2 & n1.

# (this is "points" in main )thinking i should have a list that has all the points that are not in a cluster, and remove points as i go

class Point:
   def __init__(self, x_coord , y_coord ):
      self.x = x_coord
      self.y = y_coord
      self.coords = "(" + str(x_coord) + ", " + str(y_coord) + ")"
      self.list = []
   def __str__(self):
      return self.coords
   __repr__ = __str__
   def __lt__(self, obj):
      if self.x < obj.x:
         return 

def sortX(p1):
   return p1.x

def sortY(p1):
   return p1.y

def sortListX(list):
   return list[0].x

def calculateAll(one_point, points, distances):
   for point in points:
      dist = calc_distance(one_point, point)
      if(dist != 0):
         distances.append([one_point, point, dist])

def calc_distance(p1, p2):
   return math.sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2))

def makeCluster(clusters, p1, p2):
   indice1 = searchCluster(clusters, p1)
   indice2 = searchCluster(clusters, p2)
   # len(clusters[indice1])
   if indice1 == indice2:
      # case where both points are in the same cluster already
      pass

   # need to delete old clusters from Clusters[]
   elif len(clusters[indice1]) == 1 and len(clusters[indice2]) == 1:
      # case where both clusters hold one point, thus a new larger one
      # newCluster(clusters, p1, p2)
      joinClusters(clusters, indice1, indice2)
   
   elif len(clusters[indice1]) > 1 and len(clusters[indice2]) > 1:
      # case where both clusters hold multiple points, and we join them
      joinClusters(clusters, indice1, indice2)
   
   elif len(clusters[indice1]) > 1 and len(clusters[indice2]) == 1:
      joinClusters(clusters, indice1, indice2)

   elif len(clusters[indice1]) == 1 and len(clusters[indice2]) > 1:
      joinClusters(clusters, indice1, indice2)

def joinClusters(clusters, indice1, indice2):
   list1 = clusters[indice1]
   list2 = clusters[indice2]
   list1.extend(list2)
   if(indice1 > indice2):
      del clusters[indice1]
      del clusters[indice2]
   if(indice1 < indice2):
      del clusters[indice2]
      del clusters[indice1]
   clusters.append(list1)

def newCluster(clusters, p1, p2):
   clusters.append([p1, p2])

# use this function to get indice of the cluster that contains the point
def searchCluster(clusters, pointSearch):
   i = 0 
   for cluster in clusters:
      for point in cluster:
         if(pointSearch == point):
            return i
      i += 1


# distances[[]] = calculate all distances and put them in here. sort them ascending by distance.
def main():
   # points only holds Point objects
   points = read_file(sys.argv[1])
   # print(points)
   clusters = []
   distances = [] 
   for one_point in points:
      clusters.append([one_point])
      calculateAll(one_point, points, distances)
   printer(clusters)
   distances = sorted(distances, key=itemgetter(2))

   i = 0
   num_clusters = len(clusters)
   inky = num_clusters - 1
   for entry in distances:
      makeCluster(clusters, entry[0], entry[1])
      num_clusters = len(clusters)
      if (inky == num_clusters):
         printer(clusters)
         inky -= 1
      i += 1

def printer(clusters):
   numClusters = len(clusters)
   sorted_clusters = []
   for cluster in clusters:
      # sort each cluster in itself
      sorted_clusters.append(sorted([(point.x, point.y) for point in cluster]))
   print(str(numClusters) + "-clustering:")

   sorted_clusters = sorted(sorted_clusters)
   for cluster in sorted_clusters:
      if(numClusters == 1):
         finalpoint = len(cluster)
         i = 1
         for point in cluster:
            if (finalpoint == i):
               print(str(point), end='')
            else:
               print(str(point) + ", ", end='')
            i += 1
      else:
         print(*cluster, sep = ", ")
         
   

def read_file(file_name):
   f = open(file_name, 'r')
   points_list = []
   line_list = f.readlines()
   line = line_list[0]
   line = line.replace("(", '')
   line = line.replace(")", '')
   line = line.replace(" ", '')
   splitted = line.split(",")
   i = 0

   while i < len(splitted):
      points_list.append(Point(int(splitted[i]), int(splitted[i+1])))
      i += 2

   return points_list

main()