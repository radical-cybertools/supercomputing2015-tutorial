#!/opt/anaconda/envs/python2/bin/python
import os, sys
import pickle
import pandas as pd
import sklearn.metrics
import numpy as np

def mapper(data, centroids):
    # compute distances between all points and centroids
    distance = sklearn.metrics.pairwise.euclidean_distances(data, clusters)
    # compute cluster with min distance
    cluster_id = np.argmin(distance, axis=1)
    # reshape to row vector
    cluster_id = cluster_id[:, np.newaxis]
    # join data and cluster ids
    data=np.column_stack((data, cluster_id))
    return data


if __name__ == "__main__":  
    
    if len(sys.argv)!=3:
        print("Usage: " + sys.argv[0] + " <point-file> <cluster-file>")
        sys.exit(1)
    
    points_file = sys.argv[1]
    cluster_file = sys.argv[2]    
    
    points = pd.read_csv(points_file)
    clusters = pd.read_csv(cluster_file)
    
    clusters = clusters.loc[:,'SepalLength':'PetalWidth']
    points = points.loc[:,'SepalLength':'PetalWidth']

    data = mapper(points, clusters)
    #print np.array_str(data)
    print np.array2string(data, separator=",")
    
    
    #print np.array_repr(data)
    #print(str(data))