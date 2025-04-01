import pandas
from matplotlib import pyplot

fifa_df = pandas.read_csv('PlayerData.csv')
print("Nr. rows", len(fifa_df))

fifa_df1 = fifa_df[['short_name','age','nationality','club_name','league_name','value_eur','wage_eur']]
df = fifa_df1.groupby('age')['wage_eur'].mean()
print(df)

pyplot.plot(df, marker = 'o', linestyle = 'dotted')
pyplot.xlabel("Age")
pyplot.ylabel("Wage")
pyplot.show()
