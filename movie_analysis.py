import pandas as pd
import matplotlib.pyplot as  plt
df = pd.read_csv("C:\\Users\\uifsa\\Downloads\\movies.csv")
print(df.head())
print("\nAverage Rating:", df['Rating'].mean())


#genere rating
gen_average = df.groupby('Genre')['Rating'].mean()
print("average rating by genere:",gen_average)

#Visualize Average Rating by Genre
gen_average.plot(kind='bar',color='skyblue')
plt.title('average movie rating by genre')
plt.ylabel('Avearge rating of movies')
plt.xlabel('Genre')
plt.show()
