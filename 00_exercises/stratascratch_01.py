# Find all posts which were reacted to with a heart

# https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
facebook_reactions.head()
result = (
    facebook_reactions[facebook_reactions['reaction'] == 'heart']
    .merge(facebook_posts, on='post_id', how='inner')
    [['post_id', 'post_text', 'post_keywords', 'post_date']]
)
print(result.columns.tolist())

result = result.drop_duplicates(subset=['post_id'])

print(result)
