import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-movie ratings dataset
data = {
    "User": ["A", "A", "A", "B", "B", "C", "C"],
    "Movie": ["Inception", "Interstellar", "Memento", "Inception", "Memento", "Interstellar", "Tenet"],
    "Rating": [5, 4, 5, 4, 3, 5, 4]
}

df = pd.DataFrame(data)

# Create User-Item Matrix
user_item_matrix = df.pivot_table(index="User", columns="Movie", values="Rating").fillna(0)

# Collaborative Filtering: Find similarity between users
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to recommend movies for a given user
def recommend_movies(user):
    similar_users = user_similarity_df[user].sort_values(ascending=False)
    best_match = similar_users.index[1]  # most similar other user
    recommendations = df[df["User"] == best_match]["Movie"].tolist()
    return recommendations

# Example
print("Recommendations for User A:", recommend_movies("A"))
