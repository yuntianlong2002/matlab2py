from constants import *
from utils import *
import numpy as np
import pandas as pd


#TODO: What is N, N of what? Give comment
def mtg_prepay_instrument_generator_fast(file_path, file_name, extract_date, N, amrt_bucket_size, trm_bucket_size, ttm_bucket_size):
    date_array = generate_next_x_months(MONTHS_NEEDED, extract_date)
    SMM_partial=1-np.math.pow(1-PARTIAL_PREPAY_RATE,(1/12))
    SMM_core=[0]*len(CPR_BY_TERM)
    #TODO: Add test for this
    for i in range(0,len(CPR_BY_TERM)):
        SMM_core[i]=1-np.math.pow((1-CPR_BY_TERM[i]),(1/12))

    # numpy.loadtxt(open(file_path+file_name,"rb"),delimiter=",",skiprows=1)
    data = np.matrix(np.loadtxt(file_path+file_name, delimiter=",", skiprows=1))

    # Column map used to access the colume with field data
    # print(data[:, colmap['term']])
    colmap = dict(zip(FIELD_NAMES, range(len(FIELD_NAMES))))

    #TODO: Do we really need to do the conversion at column 3?
    # data.mat_date_num=datenum(A{3});