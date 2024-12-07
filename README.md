## Threadify
Threadify is an innovative twitter/X bot that transforms trending soccer comments from various subreddits into visually appealing quote images, which are then shared on Twitter. This project was driven by a desire to engage soccer fans who may not frequent Reddit, allowing them to enjoy insightful opinions and discussions from the Reddit community.

In 2023, Reddit boasted 70 million daily active users, while twitter/X had an impressive 220 million, highlighting a significant opportunity to bridge these platforms. As a former soccer enthusiast who enjoyed watching English Premier League matches on weekends, I recognized the potential to bring Reddit's vibrant and funny post-match commentary to a broader audience on twitter/X. The primary challenge of this project was to create an automated Twitter bot using entirely free resources, ensuring zero expenses were incurred throughout the development process. The project was successfully deployed with over 2600 automated posts in just a few months. The bot account is here: [https://x.com/Opinions433](https://x.com/Opinions433)

The source code is available for reuse, and while giving credit to this repository is optional, it would be greatly appreciated! Please note that while using the automation, the bot might post more images than the threshold allowed for free twitter/X developer accounts, which may generate errors in the workflow; however, you can ignore these as the images will still be posted. I decided to pause the automation after achieving the project's goals, primarily due to the frequent notifications regarding daily posting limits and changes imposed by twitter/X.

Currently, contributions to this repository are on hold, but the code is designed to be self-explanatory. Should you have any questions or require assistance, please feel free to reach out to me at mailtothedeveloper@gmail.com.

![](https://github.com/pratmo/Threadify/blob/main/Sample.png?raw=true)

### Features
- **Custom Font Selection:** Choose any font from Google Fonts, complete with an added shadow effect for enhanced text visibility.
- **Subreddit-Specific Backgrounds:** Define and create custom background images tailored to your selected subreddit, allowing for a unique visual experience.
- **Personalized Title Colors:** Assign distinct title colors for each subreddit to improve readability and aesthetic appeal.
- **Comment Filtering:** Select and filter the number of comments displayed, ensuring only the most relevant content is included.
- **Content Exclusions:** Automatically exclude GIFs, users such as moderators and bots, as well as emojis and URLs, to maintain a clean and focused output.
- **Credit Attribution:** Include the username in the final image to provide proper credits to the original content creators.
- **Output Management:** Automatically clear the output folder after each run to save storage space and maintain organization.
- **Concise Content Presentation:** Skip lengthy titles and comments to keep the image quotes concise and impactful.
- **Automated Post Looping:** Seamlessly loop through the top posts of the day, ensuring the most current and popular content is featured.

### Main Tech/Packages
- PRAW for reddit API: praw==7.7.1
- PIL (Pillow) for creating and manipulating images: Pillow==9.4.0
- Tweepy for accessing twitter/X API: tweepy==4.14.0

### Other Notes

- Use Python 3.x

- In .yml cron is setup to run daily at 6:30 PM UTC. It can also be manually triggered.

- In .py modify the wait time post emptying the output folder before generating images, the time gap between consecutive image postings, among other customizable parameters like fonts, number of comments, etc., which is self-explanatory through code comments.

