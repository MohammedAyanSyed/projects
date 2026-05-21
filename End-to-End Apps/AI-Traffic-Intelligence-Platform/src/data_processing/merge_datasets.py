import numpy as np
import pandas as pd
import glob

address = glob.glob('C:\\Users\\Mohammed Ayan Syed\\Downloads\\datasets\\*.csv')

df = [pd.read_csv(x) for x in address]

combined_df = pd.concat(df,ignore_index=True)
counts = combined_df['Region label'].value_counts()
k = np.unique([x for x in combined_df['Region label']])

aus = ['Council of the City of Sydney', 'Inner West Council', 'Woollahra Municipal Council', 'Randwick City Council',
       'Waverley Council', 'Bayside Council', 'Burwood Council', 'City of Canada Bay Council','North Sydney Council',
       'Strathfield Municipal Council','Mosman Municipal Council','Lane Cove Municipal Council','Willoughby City Council',
       'Canterbury-Bankstown Council']
ber = ['Berlin']
cago = ['Cook County']
dub = ['County Dublin']
frn = ['Paris']
tky = ['Setagaya', 'Suginami', 'Nakano', 'Shinjuku', 'Chiyoda', 'Minato', 'Shibuya','Meguro', 'Shinagawa', 'Chuo',
             'Koto', 'Bunkyo', 'Ota', 'Toshima', 'Sumida','Taito']
la = ['Los Angeles County']
lon = ['Westminster', 'Camden', 'Islington', 'Hackney', 'Tower Hamlets','City of London', 'Southwark', 'Lewisham',
       'Greenwich', 'Newham', 'Lambeth', 'Wandsworth', 'Kensington and Chelsea', 'Hammersmith and Fulham']
nyc = ['Bronx County', 'Staten Island', 'New York County', 'Kings County', 'Queens County']

conditions = [
    combined_df['Region label'].str.contains('|'.join(aus)),
    combined_df['Region label'].str.contains('|'.join(ber)),
    combined_df['Region label'].str.contains('|'.join(cago)),
    combined_df['Region label'].str.contains('|'.join(dub)),
    combined_df['Region label'].str.contains('|'.join(frn)),
    combined_df['Region label'].str.contains('|'.join(tky)),
    combined_df['Region label'].str.contains('|'.join(la)),
    combined_df['Region label'].str.contains('|'.join(lon)),
    combined_df['Region label'].str.contains('|'.join(nyc)),
]

choice = ['Sydney','Berlin','Chicago','Dublin','Paris','Tokyo','Los Angeles','London','Ney York City']
city = np.select(condlist=conditions,choicelist=choice,default='Other')
combined_df.insert(loc=1,column='City',value=city)

# Saving CSV File
combined_df.to_csv('combined_df.csv',index=False)