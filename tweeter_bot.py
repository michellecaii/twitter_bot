# import tweepy

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("HVERKzLCqDBPJQd7xwYmZvpGY", "rz2gX7VM1kUNYyH6doXpj3qZdHwVWsT21MmmKkQC78UUi6Thsd")
# auth.set_access_token("1756881055410270208-PtsXcZhqrMwbCkdMK6DpMKpb87LubU"
# , "xJEdoT9M55Fnnk8JvS4z5sbOQYq4utCKHM03ubvEyJuIn")

# # Create API object
# api = tweepy.API(auth)

# # Create a tweet
# api.update_status("Hello, world! This is my first tweet from my Twitter bot.")

import tweepy
import base64

# Credentials for Twitter API
consumer_key = "HVERKzLCqDBPJQd7xwYmZvpGY"
consumer_secret = "rz2gX7VM1kUNYyH6doXpj3qZdHwVWsT21MmmKkQC78UUi6Thsd"
access_token = "1756881055410270208-PtsXcZhqrMwbCkdMK6DpMKpb87LubU"
access_token_secret = "xJEdoT9M55Fnnk8JvS4z5sbOQYq4utCKHM03ubvEyJuIn"

# Authenticate with Twitter API V1.1
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api_v1 = tweepy.API(auth)

# Authenticate with Twitter API V2
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)

# Path to the image file
image_path = '/Users/michellecai/Downloads/cutecat.jpeg'

# Read and encode the image
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
image_base64 = base64.b64encode(image_data)

# Upload the image to Twitter (using API V1.1)
media = api_v1.media_upload(filename=image_path)

# Extract media ID from the response
media_id = media.media_id_string

# Post a tweet with the image using API V2
response = client.create_tweet(text="testing with tweepy", media_ids=[media_id])

# Print the response from Twitter
print(response.data)
