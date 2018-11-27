## 2. Frequency Distribution ##


freq_counts = norm_reviews['Fandango_Ratingvalue'].value_counts()
fandango_distribution = freq_counts.sort_index()

fIMDB_norm_counts = norm_reviews['IMDB_norm'].value_counts()
imdb_distribution = fIMDB_norm_counts.sort_index()

print(fandango_distribution)
print(imdb_distribution)

## 4. Histogram In Matplotlib ##

fig,ax= plt.subplots()
ax.hist(norm_reviews["Fandango_Ratingvalue"],range=(0,5))
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews["Fandango_Ratingvalue"],range=(0,50), bins=20)
ax1.set_title("Distribution of Fandango Ratings")
ax1.set_ylim(0,50)

ax2.hist(norm_reviews["RT_user_norm"],range=(0,50), bins=20)
ax2.set_title("Distribution of Rotten Tomatoes Rating")
ax2.set_ylim(0,50)

ax3.hist(norm_reviews["Metacritic_user_nom"],range=(0,50), bins=20)
ax3.set_title("Distribution of Metacritic Ratings")
ax3.set_ylim(0,50)
ax4.hist(norm_reviews["IMDB_norm"],range=(0,50), bins=20)
ax4.set_title("Distribution of IMDB Ratings")
ax4.set_ylim(0,50)

plt.show()

## 7. Box Plot ##

fig,ax= plt.subplots()

ax.boxplot(norm_reviews["RT_user_norm"])

ax.set_xticklabels(["Rotten Tomatoes"])
ax.set_ylim(0,5)
plt.show()

## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig,ax= plt.subplots()

ax.boxplot(norm_reviews[num_cols].values)

ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)
plt.show()