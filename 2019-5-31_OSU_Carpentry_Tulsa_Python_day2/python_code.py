#!/Users/grachetng/miniconda3/bin/python

import pandas as pd
import sys

#print('hello')

def analyze_my_data(a):
    with open('test_script.txt','w') as output:
        output.write('{}\t{}\t{}\t{}\n'.format('Filename','Minimum','Mean','Maxima'))
        dataframe=pd.read_csv('gapminder_gdp_'+sys.argv[1]+'.csv',index_col='country')
        subset=dataframe.loc[:,"gdpPercap_2007"]
        output.write('{}\t{}\t{}\t{}\n'.format(sys.argv[1],subset.min(),subset.mean(),subset.max()))

analyze_my_data(sys.argv[1])
