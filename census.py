import pandas as pd
import censusdata
mydata = censusdata.download('acs5', 2017,
                            censusdata.censusgeo([('state','34'), ('county', '*'), ('county subdivision',
                                                '*')]), ['B19013_001E', 'B01003_001E'])
mydata['city'] = mydata.index
mydata = mydata.reset_index()

cities = []
length = len(mydata['city'])
for i in range (0,length):
    cities.append(str(mydata['city'].to_list()[i]).split(',')[0])
 
df = pd.DataFrame({"City": [],"Income":[],"Population":[]})
df['City'] = cities
df['Income'] = mydata["B19013_001E"]
df['Population'] = mydata['B01003_001E']

df
                                                
