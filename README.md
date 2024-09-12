# Threadify
An auto twitter bot for transforming reddit threads into eye catching images.

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
