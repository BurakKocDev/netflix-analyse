import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

netflix = pd.read_csv("netflix_titles.csv")

print(netflix.head())
print(netflix.shape)
print(netflix.columns)
print(netflix.isnull().sum())
print(netflix.nunique())

data = netflix.copy()

print(data.shape)

data = data.dropna()

print(data.shape)


sns.countplot(netflix["type"])
fig = plt.gcf()
fig.set_size_inches(5,5)
plt.title("tür")



sns.countplot(netflix["rating"])
sns.countplot(netflix["rating"]).set_xticklabels(sns.countplot(netflix["rating"]).get_xticklabels(),rotation = 90,ha = "right")
fig = plt.gcf()
fig.set_size_inches(13,13)
plt.title("rating")



plt.figure(figsize=(10,8))
sns.countplot(x = "rating",hue = "type",data = netflix)
plt.title("tür ve rating oran")
plt.show()




labels = ["Movie","Tv show"]
size = netflix["type"].value_counts()
colors = plt.cm.Wistia(np.linspace(0,1,2))
explode=[0,0.1]
plt.rcParams["figure.figsize"] = (9,9)
plt.pie(size,labels = labels,colors = colors,explode = explode,shadow = True,startangle = 90)
plt.title("tür görünümü",fontsize = 25)
plt.show()


netflix["rating"].value_counts().plot.pie(autopct="%1.1f%%",shadow = True,figsize = (10,8))
plt.show()


from wordcloud import WordCloud


plt.subplots(figsize = (25,15))
wordcloud = WordCloud(
background_color="white",
    width=1920,
    height=1080
).generate(" ".join(data.country))
plt.imshow(wordcloud)
plt.axis("off")
plt.davefig("country.png")
plt.show()




plt.subplots(figsize = (25,15))
wordcloud = WordCloud(
background_color="white",
    width=1920,
    height=1080
).generate(" ".join(data.cast))
plt.imshow(wordcloud)
plt.axis("off")
plt.davefig("cast.png")
plt.show()



plt.subplots(figsize = (25,15))
wordcloud = WordCloud(
background_color="white",
    width=1920,
    height=1080
).generate(" ".join(data.director))
plt.imshow(wordcloud)
plt.axis("off")
plt.davefig("director.png")
plt.show()




