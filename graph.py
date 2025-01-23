import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bench/out.csv", header=None).T
new_header = df.iloc[0]
df = df[1:].astype('float64')
df.columns = new_header
df.drop(df.tail(1).index,inplace=True)


bp = df.boxplot(whis=(0, 100))
bp.set_title('Whiskers show full range, not IQR')

# bp.set_yscale('log') # remove comment if timings are too dissimilar

plt.show()