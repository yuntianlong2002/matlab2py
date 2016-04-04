import numpy

MONTHS_NEEDED = 120;
CPR_BY_TERM = numpy.array([.07, .07, .07, .07, .07, 0, .07,  0, 0, .07])
PARTIAL_PREPAY_RATE = .01;

RUN_OFF_RATE = numpy.zeros((7,10))
RUN_OFF_RATE[:,0] = numpy.array([.1918, .1338, .1112,.0853, .0862, .1094, .2824])#1yr
RUN_OFF_RATE[:,1] = numpy.array([.1918, .1338, .1112,.0853, .0862, .1094, .2824])#2yr
RUN_OFF_RATE[:,2] = numpy.array([.1918, .1338, .1112,.0853, .0862, .1094, .2824])#3yr
RUN_OFF_RATE[:,3] = numpy.array([.1918, .1338, .1112,.0853, .0862, .1094, .2824])#4yr
RUN_OFF_RATE[:,4] = numpy.array([.1918, .1338, .1112,.0853, .0862, .1094, .2824])#5yr
RUN_OFF_RATE[:,6] = numpy.array([.1918, .1338, .1112,.0853, .0862, .1094, .2824])#7yr
RUN_OFF_RATE[:,9] = numpy.array([.1918, .1338, .1112,.0853, .0862, .1094, .2824])#10yr

FIELD_NAMES = ['num', 'auth_date_num', 'mat_date_num', 'term', 'amort', 'curr_bal', 'rate', 'float_ind']
			   #,'mat_date_Y', 'mat_date_M', 'mat_date_D', 'TTM', 'amort_bucket', 'term_bucket', 'TTM_bucket']