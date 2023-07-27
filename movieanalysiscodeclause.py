import pandas as pd
import matplotlib.pyplot as plt

# Load the movie dataset
movies_data = pd.read_csv('movies_dataset.csv')

# Display the first few rows of the dataset
print("Sample data:")
print(movies_data.head())

# Get the number of movies and number of unique genres
num_movies = len(movies_data)
num_unique_genres = len(movies_data['genres'].unique())

print("\nNumber of movies:", num_movies)
print("Number of unique genres:", num_unique_genres)

# Calculate the highest-rated movie
highest_rated_movie = movies_data.loc[movies_data['rating'].idxmax()]

print("\nHighest-rated movie:")
print(highest_rated_movie['title'], "with a rating of", highest_rated_movie['rating'])

# Calculate the most popular genres
genre_counts = movies_data['genres'].value_counts()
most_popular_genre = genre_counts.idxmax()

print("\nMost popular genre:", most_popular_genre)

# Calculate the average rating per genre
average_rating_per_genre = movies_data.groupby('genres')['rating'].mean()

print("\nAverage rating per genre:")
print(average_rating_per_genre)

# Plot a histogram of movie ratings


plt.hist(movies_data['rating'], bins=10, edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Ratings')
plt.show()
