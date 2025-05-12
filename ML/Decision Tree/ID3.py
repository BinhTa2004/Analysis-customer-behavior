import pandas as pd
import numpy as np

class DecisionTree:
    def __init__(self, attribute, threshold):
        self.attribute = attribute
        self.threshold = threshold
        self.frame = None
        self.children = []
        self.leaf = False
        self.label = None

    def add_frame(self, frame):
        self.frame = frame
    
    def entropy(self, data: pd.DataFrame, label):
        all = data[label].count()
        negative = data[data[label] == 0][label].count()
        positive = all - negative
        negative = negative + 0.00000001
        positive = positive + 0.00000001
        all = all + 0.00000001
        return -((negative/all * np.log2(negative/all)) + (positive/all * np.log2(positive/all)))
    
    def gain(self, data: pd.DataFrame, label):
        list_features = data.nunique()
        features = list_features.keys()
        ret = {}

        curr_entropy = self.entropy(data, label)

        for i in features:
            if i == label: break
            feature_count = data[i].value_counts()
            feature_count = feature_count / feature_count.values.sum()
            a = [data[data[i] == j] for j in feature_count.keys()]
            temporary_entropy_i = np.array([self.entropy(a_item, label) for a_item in a])
            ret[i] = (curr_entropy - (np.array(feature_count.values) * temporary_entropy_i).sum())

        return ret




