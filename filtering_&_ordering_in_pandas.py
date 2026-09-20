import pandas as pd

df = pd.read_csv(r"C:/Users/Apala/Documents/Data_analysis/world-population.csv")

'''
op = df[df['Rank'] < 10]
print(op)
'''

'''
specific_countries = ['Bangladesh','Brazil']
op = df[df['Country/Territory'].isin(specific_countries)]
print(op)
'''

'''
op = df[df['Country/Territory'].str.contains('United')]
print(op)
'''

'''
#create a 2nd df using the 1st one by using the index
df2 = df.set_index('Country/Territory')
print(df2)
'''

'''
#1 implies search along the x axes and print the corresponding col
#2 implies search the y axes and print the corresponding row
x_axes = df2.filter(items = ['Continent','CCA3'], axis = 1)
y_axes = df2.filter(items = ['Zimbabwe'], axis = 0)
'''

'''
op = df2.loc['United States']
print(op)
'''

'''
op = df2.iloc[3]
print(op)
'''

'''
op = df[df['Rank'] < 10].sort_values(by=['Continent','Country'],
     ascending=[False,True])
print(op)
'''