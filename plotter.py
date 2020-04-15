import pandas as pd 
import datetime

#>>> d = datetime.datetime(2020, 3, 28)
#>>> d.timetuple().tm_yday
#88

def todate(GE):
    GE = str(GE)
    day   = int(GE[-2:])
    month = int(GE[:-2])
    d = datetime.datetime(2020, month, day).timetuple().tm_yday
    return d

df = pd.read_csv("comune_giorno.csv", encoding = "iso-8859-1") 
df = df.replace(9999, 0)
df['GE'].update( df['GE'].apply(todate) )

import matplotlib.pyplot as plt

index = df['GE'] < 88
df88 = df[index].sort_values(by=['GE'])
df88 = df88.groupby('GE').sum()
plt.plot(list(df88['TOTALE_15'].cumsum()), label = "2015")
plt.plot(list(df88['TOTALE_16'].cumsum()), label = "2016")
plt.plot(list(df88['TOTALE_17'].cumsum()), label = "2017")
plt.plot(list(df88['TOTALE_18'].cumsum()), label = "2018")
plt.plot(list(df88['TOTALE_19'].cumsum()), label = "2019")
plt.plot(list(df88['TOTALE_20'].cumsum()), label = "2020")
plt.ylabel('Death')
plt.legend()
plt.show()

