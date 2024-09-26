import pandas as pd
import math

class Proteomagic:

    '''
    A class representing the Proteomagic package. This class is used to perform basic proteomic analysis in Python.

    Attributes:
    data (pd.DataFrame): A pandas DataFrame containing the proteomic data.

    Methods:
    fromcsv(cls, filename): A class method to create a Proteomagic object from a CSV file.
    fromdict(cls, data): A class method to create a Proteomagic object from a dictionary.
    '''

    def __init__(self, data):
        self.data = data

    @classmethod
    def fromcsv(cls, filename):
        '''
        A class method to create a Proteomagic object from a CSV file.

        Args:
        filename (str): The filename of the CSV file to be read. 
                        The first column of the CSV file should contain the protein names.
        '''
        data = pd.read_csv(filename, index_col=0)
        return cls(data)
    
    @classmethod
    def fromdict(cls, data):
        '''
        A class method to create a Proteomagic object from a dictionary.

        Args:
        data (dict): A dictionary containing the proteomic data. 
                     The keys of the dictionary should be the sample names of the proteomic data.
                     The first key:[value] should be a list of string representing the protein names.
        '''
        data = pd.DataFrame(data, index=data[list(data.keys())[0]]).drop(list(data.keys())[0], axis=1)
        return cls(data)
    
    def transform(self, method='log2'):

        '''
        A method to transform the proteomic data.

        Args:
        method (str): The transformation method to be used. 
                      The available methods are 'log2', .
                      The default method is 'log2'. 

        *** If 'NaN' is present in the data, it will be ignored and returned as 'NaN'.
        '''


        if method == 'log2':
            self.data = self.data.applymap(lambda x: math.log2(x) if x > 0 else None)


    def normalize(self, method='quantile'):

        '''
        A method to normalize the proteomic data.

        Args:
        method (str): The normalization method to be used. 
                      The available methods are 'zscore', .
                      The default method is 'zscore'.
        '''
        if method == 'quantile':

            sample_rankings = self.data.rank(axis=0, na_option='top')
            ranked_sample = pd.DataFrame()
            for col in self.data.columns:
                ranked_sample[col] = self.data[col].sort_values(na_position='first', ignore_index=True)

            ranked_sample_mean = ranked_sample.kmean(axis=0, skipna=True)

            return sample_rankings
                                                         
    def remove_missing(self):
        '''
        A method to remove missing values from the proteomic data.
        '''
        self.data = self.data.dropna()
    
    
dict = {
    'proteins': ['NUDT48', 'IGKV3-7', 'IGLV4-69'],
    'Sample1': [12.5, 13.2, 43.2],
    'Sample2': [19.3, None, 23.4],
    'Sample3': [15, 23.5, 32.4]
}

pm = Proteomagic.fromdict(dict)
pm.transform()
print(pm.normalize())
#print(pm.data)

