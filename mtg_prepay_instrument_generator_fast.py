from constants import *
from utils import *
from datetime import datetime
import numpy as np
import pandas as pd
import math as math


#TODO: What is N, N of what? Give comment
def mtg_prepay_instrument_generator_fast(file_path, file_name, extract_date, N, amrt_bucket_size, trm_bucket_size, ttm_bucket_size):
    date_array = generate_next_x_months(MONTHS_NEEDED, extract_date)
    SMM_partial = 1-np.math.pow(1-PARTIAL_PREPAY_RATE,(1/12))
    current_date_number = datetime.toordinal(datetime.strptime(extract_date, "%Y/%m/%d"))

    SMM_core=[0]*len(CPR_BY_TERM)
    #TODO: Add test for this
    for i in range(0,len(CPR_BY_TERM)):
        SMM_core[i]=1-np.math.pow((1-CPR_BY_TERM[i]),(1/12))

    data = pd.read_csv(file_path+file_name)
    data.columns = FIELD_NAMES;
    ## print data.mat_date_num.head() # Regular format
    data['mat_date_Y'] = data.mat_date_num.apply(lambda e: datetime.strptime(e, "%Y-%m-%d %H:%M:%S").date().year)
    data['mat_date_M'] = data.mat_date_num.apply(lambda e: datetime.strptime(e, "%Y-%m-%d %H:%M:%S").date().month)
    data['mat_date_D'] = data.mat_date_num.apply(lambda e: datetime.strptime(e, "%Y-%m-%d %H:%M:%S").date().day)
    data.mat_date_num = data.mat_date_num.apply(lambda e: datetime.toordinal(datetime.strptime(e, "%Y-%m-%d %H:%M:%S"))) # 2016-11-19 00:00:00
    ## print data.mat_date_num.head() # date number format
    # Show year, month, day individually
    ## print data.mat_date_Y.head()
    ## print data.mat_date_M.head()
    ## print data.mat_date_D.head()
    data['TTM'] = data.mat_date_num.apply(lambda e: (e-current_date_number)/30.0)
    ## print data.TTM.head()
    data.ix[data.term < data.TTM, 'term'] = data.ix[data.term < data.TTM, 'TTM']
    ## print data.term.head()
    data.ix[data.amort < data.TTM, 'amort'] = data.ix[data.amort < data.TTM, 'TTM']
    ## print data.amort.head()
    '''
    Create Buckets
    '''
    data['amort_bucket'] = data.amort.apply(lambda e: math.ceil(e/amrt_bucket_size)*amrt_bucket_size)
    ## print data.amort_bucket.head()
    data['term'] = data.term.apply(lambda e: e if e<120 else 120)
    ## print data.term.head()
    data['term_bucket'] = data.term.apply(lambda e: math.ceil(e/trm_bucket_size)*trm_bucket_size)
    ## print data.term_bucket.head()
    data['TTM_bucket'] = data.TTM.apply(lambda e: math.ceil(e/ttm_bucket_size)*ttm_bucket_size)
    ## print data.TTM_bucket.head()

    search_groups = data[['term_bucket', 'TTM_bucket', 'amort_bucket']]
    search_groups["term_bucket"] = search_groups["term_bucket"].astype(int)
    search_groups["TTM_bucket"] = search_groups["TTM_bucket"].astype(int)
    search_groups["amort_bucket"] = search_groups["amort_bucket"].astype(int)
    ## print search_groups
    ## print search_groups.duplicated()
    search_groups = search_groups.drop_duplicates()
    print search_groups


