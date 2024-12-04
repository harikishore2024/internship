import math

# Sample user-item ratings matrix (rows are users, columns are items)
# 0 represents unrated items
ratings = [
    [5, 4, 0, 2, 1],  # User 1
    [3, 0, 0, 5, 4],  # User 2
    [4, 0, 0, 4, 5],  # User 3
    [3, 3, 0, 3, 3],  # User 4
    [1, 1, 0, 2, 1]   # User 5
]

# Function to compute cosine similarity between two vectors (lists)
def cosine_similarity(v1, v2):
    # Calculate the dot product of two vectors
    dot_product = sum(a * b for a, b in zip(v1, v2))
    
    # Calculate the magnitude (Euclidean norm) of each vector
    magnitude_v1 = math.sqrt(sum(a ** 2 for a in v1))
    magnitude_v2 = math.sqrt(sum(b ** 2 for b in v2))
    
    # Compute cosine similarity
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0
    return dot_product / (magnitude_v1 * magnitude_v2)

# Function to get user-user similarity matrix using cosine similarity
def compute_user_similarity(ratings):
    num_users = len(ratings)
    similarity_matrix = [[0] * num_users for _ in range(num_users)]
    
    # Compute similarity between each pair of users
    for i in range(num_users):
        for j in range(i, num_users):
            sim = cosine_similarity(ratings[i], ratings[j])
            similarity_matrix[i][j] = sim
            similarity_matrix[j][i] = sim  # The matrix is symmetric
            
    return similarity_matrix

# Function to recommend items to a given user based on similar users' ratings
def recommend_items(user_id, ratings, num_recommendations=3):
    # Compute user-user similarity
    user_similarity = compute_user_similarity(ratings)
    
    # Get the similarity scores for the given user
    user_similarity_scores = user_similarity[user_id]
    
    # Get the indices of the most similar users (exclude the user themselves)
    similar_users = sorted(range(len(user_similarity_scores)), key=lambda x: user_similarity_scores[x], reverse=True)
    
    recommended_items = {}
    
    # Loop through the most similar users and recommend items they have rated highly
    for similar_user in similar_users:
        if similar_user == user_id:
            continue  # Skip the user's own ratings
        
        for item_idx, rating in enumerate(ratings[similar_user]):
            if ratings[user_id][item_idx] == 0:  # If the user hasn't rated this item
                if item_idx not in recommended_items:
                    recommended_items[item_idx] = rating
                else:
                    recommended_items[item_idx] += rating
    
    # Sort the recommended items by the rating score (in descending order)
    sorted_recommendations = sorted(recommended_items.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top `num_recommendations` items
    return sorted_recommendations[:num_recommendations]

# Example: Recommend items to user 0 (User 1)
user_id = 0
recommended_items = recommend_items(user_id, ratings)

print(f"Recommended items for User {user_id + 1}:")
for item, score in recommended_items:
    print(f"Item {item + 1} (estimated rating score: {score})")
