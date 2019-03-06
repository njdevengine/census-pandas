import pandas as pd
import censusdata
mydata = censusdata.download('acs5', 2017,
                            censusdata.censusgeo([('state','34'), ('county', '*'),
                            ('county subdivision','*')]),
                            ['B19013_001E', 'B01003_001E', 'B01001_002E',
                             'B01001A_001E', 'B01001B_001E', 'B01001D_001E', 'B01001I_001E',
                             'B23025_004E', 'B08136_001E'])
mydata['city'] = mydata.index
mydata = mydata.reset_index()

cities = []
clean = []
length = len(mydata['city'])
for i in range (0,length):
    cities.append(str(mydata['city'].to_list()[i]).split(',')[0])
for i in cities:
    end = (len(i.split(' ')))
    i = (i.split(' ')[:end-1])
    clean.append(" ".join(i))
    
df = pd.DataFrame({"City": [],"Income":[],"Population":[], "Male Pop (%)":[],
                   "White (%)":[],"Black (%)":[],"Asian (%)":[],"Hispanic (%)":[],
                   "Employed (%)":[], "Travel Time to Work (mins)":[]})
df['City'] = clean
df['Income'] = mydata["B19013_001E"]
df['Population'] = mydata['B01003_001E']
df['Male Pop (%)'] = ((mydata['B01001_002E'])/(mydata['B01003_001E'])*100).round(2)
df["White (%)"] = ((mydata['B01001A_001E'])/(mydata['B01003_001E'])*100).round(2)
df["Black (%)"] = ((mydata['B01001B_001E'])/(mydata['B01003_001E'])*100).round(2)
df["Asian (%)"] = ((mydata['B01001D_001E'])/(mydata['B01003_001E'])*100).round(2)
df["Hispanic (%)"] = ((mydata['B01001I_001E'])/(mydata['B01003_001E'])*100).round(2)
df["Employed (%)"] = ((mydata['B23025_004E'])/(mydata['B01003_001E'])*100).round(2)
df["Travel Time to Work (mins)"] = ((mydata['B08136_001E'])/(mydata['B23025_004E'])).round(0)
