import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

class recommender:
    def __init__(self):
        self.movies = None
        self.userrating = None
        self.merged_df = None
        print('hi')
        self.data_matrix = None
        self.user_similarity = None
    def createMoviesDF(self,values):
        self.movies = pd.DataFrame(np.array(values),columns=["Movies","movieid"])
        return self.movies
    def createUserRatingDF(self,values):
        self.userrating = pd.DataFrame(np.array(values),columns=["userid","movieid","rating"])
        return self.userrating
    def mergeDF(self):
        self.merged_df = pd.merge(self.userrating,self.movies)
        return self.merged_df
    def createDataMatrix(self):
        n_movies = len(merged_df['Movies'].unique())
        n_users = len(merged_df['userid'].unique())
        self.data_matrix = np.zeros((n_users, n_movies))
        
        for line in self.merged_df.itertuples():
            print(line[1]-1, line[2], line[3])
            self.data_matrix[line[1]-1, line[2]] = line[3] 
        return self.data_matrix
    def generateUserSimilarityMatrix(self):
        self.user_similarity = pairwise_distances(self.data_matrix, metric='cosine')
        return self.user_similarity
    def getResultFor(self,userid):
        return self.user_similarity[userid]  

