import numpy as np
import data_parser
import matplotlib
import matplotlib.pyplot as plt
import copy
from SingleFit import SingleFit
from SingleFit import timeit
from sklearn.model_selection import KFold
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import mean_squared_error
#from evolutionary_search import EvolutionaryAlgorithmSearchCV
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import r2_score
from multiprocessing import Process,Pool,TimeoutError,Value,Array,Manager
import time
import copy
from DataParser import FeatureNormalization
from DataParser import FeatureIO
__author__ = "Tam Mayeshiba"

class CustomFeatures():
    """Class for creating custom feature columns.
        New methods may be added.

    Args:
        dataframe <data object>

    Returns:
    Raises:
        ValueError if dataframe is None
    """
    def __init__(self, dataframe=None):
        """Custom data handler
            
        Attributes:
            self.original_dataframe <data object>: Dataframe
            self.df <data object>: Dataframe
        """
        if dataframe is None:
            raise ValueError("No dataframe.")
        self.original_dataframe = copy.deepcopy(dataframe)
        self.df = copy.deepcopy(dataframe)
        return

    def calculate_EffectiveFluence(self, pvalue, ref_flux = 3e10, flux_feature="",fluence_feature="", scale_min = 1e17, scale_max = 1e25):
        fluence = self.df[fluence_feature]
        flux = self.df[flux_feature]

        EFl = fluence * (ref_flux / flux) ** pvalue
        EFl = np.log10(EFl)
        fio = FeatureIO(self.df)
        fio.add_features(["EFl"],EFl)
        N_EFl = fio.minmax_scale_single_feature("EFl", 
                                            smin = scale_min,
                                            smax = scale_max)

        return N_EFl

    def testing_subtraction(self, param, col1="",col2=""):
        col1_data = self.df[col1]
        col2_data = self.df[col2]
        new_data = col1_data - col2_data + param
        fio = FeatureIO(self.df)
        fio.add_features(["Subtraction_test"],new_data)
        N_new_data = fio.minmax_scale_single_feature("Subtraction_test")
        return N_new_data

