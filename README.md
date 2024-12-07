# Threadify
Threadify is an innovative twitter/X bot that transforms trending soccer comments from various subreddits into visually appealing quote images, which are then shared on Twitter. This project was driven by a desire to engage soccer fans who may not frequent Reddit, allowing them to enjoy insightful opinions and discussions from the Reddit community.

In 2023, Reddit boasted 70 million daily active users, while twitter/X had an impressive 220 million, highlighting a significant opportunity to bridge these platforms. As a former soccer enthusiast who enjoyed watching English Premier League matches on weekends, I recognized the potential to bring Reddit's vibrant and funny post-match commentary to a broader audience on twitter/X. The primary challenge of this project was to create an automated Twitter bot using entirely free resources, ensuring zero expenses were incurred throughout the development process. The project was successfully deployed with over 2600 automated posts in just a few months. The bot account is here: [https://x.com/Opinions433](https://x.com/Opinions433)

The source code is available for reuse, and while giving credit to this repository is optional, it would be greatly appreciated! Please note that while using the automation, the bot might post more images than the threshold allowed for free twitter/X developer accounts, which may generate errors in the workflow; however, you can ignore these as the images will still be posted. I decided to pause the automation after achieving the project's goals, primarily due to the frequent notifications regarding daily posting limits and changes imposed by twitter/X.

Currently, contributions to this repository are on hold, but the code is designed to be self-explanatory. Should you have any questions or require assistance, please feel free to reach out to me at mailtothedeveloper@gmail.com.

![](https://github.com/pratmo/Threadify/blob/main/Sample.png?raw=true)

## Features
- **Custom Font Selection:** Choose any font from Google Fonts, complete with an added shadow effect for enhanced text visibility.
- **Subreddit-Specific Backgrounds:** Define and create custom background images tailored to your selected subreddit, allowing for a unique visual experience.
- **Personalized Title Colors:** Assign distinct title colors for each subreddit to improve readability and aesthetic appeal.
- **Comment Filtering:** Select and filter the number of comments displayed, ensuring only the most relevant content is included.
- **Content Exclusions:** Automatically exclude GIFs, users such as moderators and bots, as well as emojis and URLs, to maintain a clean and focused output.
- **Credit Attribution:** Include the username in the final image to provide proper credits to the original content creators.
- **Output Management:** Automatically clear the output folder after each run to save storage space and maintain organization.
- **Concise Content Presentation:** Skip lengthy titles and comments to keep the image quotes concise and impactful.
- **Automated Post Looping:** Seamlessly loop through the top posts of the day, ensuring the most current and popular content is featured.

## Main Tech/Packages
- PRAW for reddit API: praw==7.7.1
- PIL (Pillow) for creating and manipulating images: Pillow==9.4.0
- Tweepy for accessing twitter/X API: tweepy==4.14.0

### Parameters
1. In .yml change the UTC time as to when you want this workflow to be deployed automatically.

┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of the week (0 - 7) (Sunday to Saturday, 7 is also Sunday)
│ │ │ │ │
* * * * *

So currently set to 30:18 meaning 6.30 pm.

2. In code, the sleep time between posts is set to 60 which is 1 minute. So after posting 1st image, we will wait for 1 min and then post the next image and so on.

3. In code, post clearing or emptying the output folder and before generating all images, we are waiting for 20 seconds.

4. In code, you may change the subreddits, the color of the title font, no. of comments etc. The code has been commented so no issues.

5. More queries, feel free to reach out to me - mailtothedeveloper@gmail.com / prathikmohan@yandex.com
