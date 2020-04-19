import pandas as pd 
import datetime
import seaborn as sns

sns.set()
sns.set_palette(sns.cubehelix_palette(8))

DAY = 28 #FIXME hardcoded day

def todate(GE):
    GE = str(GE)
    day   = int(GE[-2:])
    month = int(GE[:-2])
    d = datetime.datetime(2020, month, day).timetuple().tm_yday
    return d

def todate2(GE):
    GE = str(GE)
    day   = int(GE[-2:])
    month = int(GE[:-2])
    if month != 3:
        return -1
    if day > DAY: 
        return -1
    return day

df = pd.read_csv("comune_giorno.csv", encoding = "iso-8859-1") 
df = df.replace(9999, 0)
df['GE'].update( df['GE'].apply(todate2) )
import matplotlib.pyplot as plt

#index = df['NOME_PROVINCIA'] == 'Bergamo'
#index = df['NOME_PROVINCIA'] == 'Piacenza'
#index = df['NOME_PROVINCIA'] == 'Brescia'
index = df['NOME_PROVINCIA'] == 'Milano'

df = df[index]
index = df['GE'] > - 1
df88 = df[index].sort_values(by=['GE'])
df88 = df88.groupby('GE').sum()
#df.loc[df['column_name'] == some_value]
x = ["%d/04" % x for x in range(1, 1+DAY)]

plt.plot(x, list(df88['TOTALE_15'].cumsum()),  label = "2015")
plt.plot(x, list(df88['TOTALE_16'].cumsum()),  label = "2016")
plt.plot(x, list(df88['TOTALE_17'].cumsum()),  label = "2017")
plt.plot(x, list(df88['TOTALE_18'].cumsum()),  label = "2018")
plt.plot(x, list(df88['TOTALE_19'].cumsum()),  label = "2019")
plt.plot(x, list(df88['TOTALE_20'].cumsum()),  label = "2020")
plt.xticks(x, rotation='45')
plt.ylabel('Смерти с нарастающим итогом') 
plt.xlabel('Дата')
plt.title("Регион: " +  "Милан")

plt.subplots_adjust(bottom=0.15)

plt.legend()

plt.show()

