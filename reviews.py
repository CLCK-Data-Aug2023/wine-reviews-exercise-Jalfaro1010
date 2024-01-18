# add your code here

# Importing pandas and reading the zip file
import pandas as pd

df = pd.read_csv("data\\winemag-data-130k-v2.csv.zip")

# Summary of Name, Number of Reviews, Average Points, and Unique Country
new_df = df[["country", "points"]]

count_df = new_df.groupby("country").apply("count")
count_df = count_df.rename(columns={"points":"counts"})

# Finding The Average or "mean"
mean_df = new_df.groupby("country").apply("mean")

# Merging dataframes with inner join
final = pd.merge(count_df, mean_df, how="inner", on="country")

# Reverse ascending order so it goes Highest to Lowest
final.sort_values("counts", ascending=False)

# Saving Dataframe to CSV File
df.to_csv("reviews-per-country.csv")

print(df.columns)