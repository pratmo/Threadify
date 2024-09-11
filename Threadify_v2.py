import praw
import textwrap
import os
import re
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import tweepy

# Define font path and base font size
font_path = "fonts/Poppins-BoldItalic.ttf"  # Relative path
base_font_size = 80  # Adjust based on image size

# Define text and shadow colors
text_color = (255, 255, 255)  # White
shadow_color = (0, 0, 0)  # Black
shadow_offset = 2

# Define output directory
output_dir = "Output_Images"

# Define background images for each subreddit
subreddit_images = {
    'reddevils': 'Pillow/Reddevils_Background.jpg',
    'Gunners': 'Pillow/Gunners_Background.jpg',
    'PremierLeague': 'Pillow/PremierLeague_Background.jpg',
    'chelseafc': 'Pillow/Chelsea_Background.jpg',
    'LiverpoolFC': 'Pillow/Liverpool_Background.jpg',
    'MCFC': 'Pillow/MCFC_Background.jpg'
}

# Define unique title colors for each subreddit
subreddit_colors = {
    'reddevils': (255, 255, 0),      # Yellow
    'Gunners': (255, 255, 255),      # White for Gunners
    'PremierLeague': (255, 255, 255),# White for Premier League
    'chelseafc': (0, 255, 255),      # Chelsea Blue
    'LiverpoolFC': (255, 255, 255),  # Liverpool Red
    'MCFC': (237, 204, 154),         # Man City Blue
}

# Regular expression pattern for detecting URLs
url_pattern = re.compile(r'http[s]?://|www\.')

# List of common GIF formats to detect GIFs
gif_keywords = ['.gif', '[gif]']

# List of users to exclude from comments
excluded_users = ['gunnersmoderator', 'AutoModerator', 'mcfcbot', 'DragonSlayer271', 'rLiverpoolFC_Mods']

# Emoji removal using regular expressions
def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        u"\U0001F700-\U0001F77F"  # Alchemical Symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251"  # Enclosed Characters
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Configure PRAW (Reddit API) with environment variables
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD'),
    check_for_async=False,
)

# Dynamic variables for number of comments and subreddits
num_comments = 8  # Number of top comments to filter from the top 20
subreddits = ['reddevils', 'Gunners', 'PremierLeague', 'chelseafc', 'LiverpoolFC', 'MCFC']

# Function to empty the output folder
def empty_output_folder(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

    # Add wait time after emptying the folder
    print("Waiting for 20 seconds after emptying the folder...")
    time.sleep(20)
    print("20 seconds wait over, proceeding with the next steps.")

# Image generation function
def add_text_to_image(image_path, text, author, title, output_path, title_color):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Prepare and draw the post title first
    title_font = ImageFont.truetype(font_path, base_font_size // 2)
    wrapped_title = textwrap.fill(f"On {title}", width=50)
    title_bbox = draw.textbbox((0, 0), wrapped_title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]

    # Prepare and draw the comment text
    quoted_text = f'"{text}"'
    wrapped_text = textwrap.fill(quoted_text, width=30)
    font_size = max(60, base_font_size - len(quoted_text) // 10)
    font = ImageFont.truetype(font_path, font_size)

    text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Prepare and draw the username text
    author_text = f'- u/{author}'
    wrapped_author = textwrap.fill(author_text, width=30)
    author_bbox = draw.textbbox((0, 0), wrapped_author, font=font)
    author_width = author_bbox[2] - author_bbox[0]
    author_height = author_bbox[3] - author_bbox[1]

    # Calculate the total height for all text elements
    total_text_height = title_height + text_height + author_height + 120

    # Calculate the starting Y position
    image_width, image_height = image.size
    y_start = (image_height - total_text_height) / 2

    # Draw the title
    x_title = (image_width - title_width) / 2
    draw.text((x_title + shadow_offset, y_start + shadow_offset), wrapped_title, font=title_font, fill=shadow_color)
    draw.text((x_title, y_start), wrapped_title, font=title_font, fill=title_color)

    # Draw the comment
    x_text = (image_width - text_width) / 2
    y_text = y_start + title_height + 40
    draw.text((x_text + shadow_offset, y_text + shadow_offset), wrapped_text, font=font, fill=shadow_color)
    draw.text((x_text, y_text), wrapped_text, font=font, fill=text_color)

    # Draw the username
    x_author = (image_width - author_width) / 2
    y_author = y_text + text_height + 40
    draw.text((x_author + shadow_offset, y_author + shadow_offset), wrapped_author, font=font, fill=shadow_color)
    draw.text((x_author, y_author), wrapped_author, font=font, fill=text_color)

    # Save the image
    image.save(output_path)

# Function to check if a text contains a URL or GIF keyword
def contains_url_or_gif(text):
    if url_pattern.search(text) or any(gif_keyword in text.lower() for gif_keyword in gif_keywords):
        return True
    return False

# Function to scan a subreddit, get the top post and comments, and generate images
def scan_subreddit(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    # Loop through the top posts of the day
    for top_post in subreddit.top(time_filter='day', limit=10):  # limit set to 10 for demonstration, adjust as needed

        post_title = remove_emojis(top_post.title)

        # Skip posts with URLs, GIFs, or where the title exceeds 120 characters
        if len(post_title) > 120 or contains_url_or_gif(post_title):
            print(f"Skipping post in {subreddit_name} due to invalid title (either too long or contains a URL/GIF).")
            continue  # Move to the next post

        top_post.comment_sort = 'top'
        top_post.comment_limit = 20
        top_post.comments.replace_more(limit=0)

        # Filter comments based on length constraints, excluding specific users, URLs, and GIFs
        comments = [
            (remove_emojis(comment.body.strip()), comment.author.name)
            for comment in top_post.comments[:num_comments]
            if comment.author
            and comment.author.name not in excluded_users  # Exclude comments from specified users
            and len(comment.body.strip()) <= 500
            and not contains_url_or_gif(comment.body.strip())  # Exclude comments with URLs or GIFs
        ]

        if comments:
            # Use subreddit-specific background image and title color
            image_path = subreddit_images[subreddit_name]
            title_color = subreddit_colors[subreddit_name]

            for i, (comment, author) in enumerate(comments):
                output_image_path = os.path.join(output_dir, f"{subreddit_name}_quote_{i+1}.jpg")
                add_text_to_image(image_path, comment, author, post_title, output_image_path, title_color)
            break  # Exit after processing the first valid post

# Twitter posting function using v1.1 for media upload and v2 for posting
def post_images_to_twitter(image_files):
    # Twitter API Authentication using environment variables
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # V1.1 Twitter API Authentication (for media upload)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # V2 Twitter API Authentication (for creating the tweet with media)
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True,
    )

    for image_file in image_files:
        try:
            # Step 1: Upload image using v1.1 API
            media_id = api.media_upload(filename=image_file).media_id_string
            print(f"Uploaded media: {media_id}")

            # Step 2: Create a tweet using v2 API (no text, just media)
            client.create_tweet(media_ids=[media_id])
            print(f"Tweeted image: {image_file}")

        except Exception as e:
            print(f"Failed to tweet {image_file}: {e}")

        # Wait 20 seconds before posting the next image
        time.sleep(20)

# Function to scan all subreddits
def scan_all_subreddits():
    print(f"Running scan at {datetime.now()}")

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Empty the output folder
    print(f"Emptying output folder: {output_dir}")
    empty_output_folder(output_dir)

    image_files = []
    for subreddit in subreddits:
        scan_subreddit(subreddit)
        for i in range(num_comments):
            output_image_path = os.path.join(output_dir, f"{subreddit}_quote_{i+1}.jpg")
            if os.path.exists(output_image_path):
                image_files.append(output_image_path)

    print(f"Generated {len(image_files)} images.")
    if image_files:
        post_images_to_twitter(image_files)  # Post images after generation
    else:
        print("No images to post.")

if __name__ == "__main__":
    scan_all_subreddits()
