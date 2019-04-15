import pandas as pd

"""
Data dictionary:

INFORMATION:

This file lists the films in the MIAS database and provides     
appropriate details as follows:

1st column: MIAS database reference number.

2nd column: Character of background tissue: 
                F - Fatty 
                G - Fatty-glandular
                D - Dense-glandular

3rd column: Class of abnormality present:
                CALC - Calcification
                CIRC - Well-defined/circumscribed masses
                SPIC - Spiculated masses
                MISC - Other, ill-defined masses
                ARCH - Architectural distortion
                ASYM - Asymmetry
                NORM - Normal

4th column: Severity of abnormality;
                B - Benign
                M - Malignant
                
5th,6th columns: x,y image-coordinates of centre of abnormality.

7th column: Approximate radius (in pixels) of a circle enclosing
	    the abnormality.

"""

#reading csv and renaming cols:
results = pd.read_csv('results.csv',sep=';',header=None)
results.columns = ['id','tissue','anomaly','severity','x_abnorm','y_abnorm','abn_radius']


# checking structure
results.head()

# filling with zero
results = results.fillna(0)

"""
renaming tumor category - preparing for prediction:
0: normal
1: benign
2: malignant
"""
ben_malig = {    'B' : 1,
                 'M' : 2
            }
results['severity'].replace(ben_malig, inplace = True)



# checking structure
results.head()
results.severity.unique()

# checking duplicates
results.id.value_counts().sort_values(ascending=False)

duplicates = ['mdb226',
             'mdb249',
             'mdb239',
             'mdb132',
             'mdb144',
             'mdb223',
             'mdb005',]

results.loc[results['id'].isin(duplicates),:]

# removing duplicates

results = results.drop(index=[5,132,145,225,229,230,244,255])

# saving to a new csv file
results.to_csv('results_clean.csv',index=False)
