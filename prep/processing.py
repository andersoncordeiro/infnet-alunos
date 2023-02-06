import pandas as pd
import numpy as np
import json


def returnDict(str):
    try:
        return json.loads(str)
    except:
        return np.NaN
    
    
df = pd.read_csv('../data/raw/imoveis.csv')
limite = 40
cols_remove = df.columns[df.isnull().sum() > limite]

cols_remove = ['Unnamed: 0',
              'displayId', 
               'cityId', 
               'photos', 
               'photosCategorizedByRooms', 
               'relevantRegions', 
               'photospheres',
               'status',
               'showUrlHasBeenCopiedSnackbar',
               'isGalleryModalOpen',
               'error',
               'loaded',
               'loading',
               'loadingCategorizedRooms',
               'selectedMedia',
               'promotions',
               'closingStatus',
               'lastPublishedDate',
               'listingPublication',
               'forSale', 
               'forRent', 
               'salePrice', 
               'isPrimaryMarket', 
               'extraInfo', 
               'houseVisitStatus',
               'visitsUnavailable',
               'isReserved',
               'allowDirectOffer',
               'rentOnTermination',]

df.drop(columns=cols_remove, inplace=True)
df_macro = df['macroRegion'].str.replace('\'','"').apply(returnDict).apply(pd.Series)
df = pd.concat([df, df_macro.add_prefix('macroRegion_')], axis=1)
cols_remove = ['macroRegion_id', 'macroRegion', 'macroRegion_0']
df.drop(columns=cols_remove, inplace=True)
df = df[~(df['id'].isnull())]
df.to_csv('../data/cleaned/imoveis_cleaned.csv')