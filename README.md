# TOEFTEL_Instagram_Bot

This comprehensive Instagram bot offers an automated solution for maximizing your Instagram engagement and presence efficiently. With features like account data retrieval, automated Instagram login, and hashtag navigation, it streamlines your social media interactions. The bot not only interacts with posts by commenting and liking but also manages follow and unfollow actions based on specific criteria. It includes advanced functionalities like direct messaging automation and a web-based UI using Flask, enhancing user experience and control. Whether for personal use or to boost a business profile, this bot serves as a versatile tool for effective Instagram management.

This Instagram bot serves as a demonstration of automation possibilities on social media platforms and is intended for personal experimentation and learning; users should employ it responsibly, ensuring compliance with platform guidelines and regulations.

### Youtube Video

- Link to Video Part 1 (public): https://youtu.be/BR4TxhSrBTc
- Link to Video Part 2 (public): https://youtu.be/T0OMQ9MRGLY
- Link to Video Part 3 (public): https://youtu.be/HwksRdA_814
- Link to Video Part 4 (public): https://youtu.be/xlQmGy6A7Hg?si=3vnvbLxk5XAblz_1

### Features
- Account Data Retrieval:
  - Extracts account details directly from a JSON file. (✅ Done)
- Instagram Login:
  - Automates login process using the account data. (✅ Done)
- Hashtag Navigation:
  - Can navigate to specified hashtags with ease. (✅ Done)
- Post Interaction:
  - Comment on the first post of a hashtag. (✅ Done)
  - Extract up to 10 posts from a specific hashtag. (✅ Done)
  - Reads the post text. (⏳ In Progress)
  - Fetches AI-generated responses for comments. (❌ Not Done)
  - Uses a predefined list of comments for engagement. (✅ Done)
  - Likes posts. (✅ Done)
  - Extends predefined post list by adding multiple hashtags. (✅ Done)
- Follow Management:
  - Enables following users. (✅ Done, "Folgen hinzufügen")
  - Generates files with timestamps & names of followed accounts. (✅ Done, "Datei erstellen")
  - If the timestamp exceeds 3 days, the bot can unfollow the user and delete the respective record file. (✅ Done)
  - User Management for multiple accounts (✅ Done)
- Direct Messaging Automation on Instagram (✅ Done)
  - This code automates the process of sending direct messages to a list of Instagram users. Here's a breakdown of its functionalities:
    - Navigation to Direct Inbox:
    - Checks for any notification prompts and dismisses them if present.
    - Direct Message Iteration:
      - Iterates through a list of usernames provided as cls.names.
      - For each username, the following sequence of events occurs:
        - Initiate New Message: Clicks the 'New Message' button to initiate the process.
        - Recipient Selection:
          - Types in the username in the recipient input field.
          - Waits for the username to be recognized by Instagram's search.
          - If the user is found, selects the user. Otherwise, skips to the next username.
        - Message Composition and Dispatch:
          - After selecting the user, moves to the message input field.
          - Fetches a message from CommentGenerator class (this suggests that the class generates or provides messages).
          - Types the message into the input field and sends it.
  - Unfollowing all followed Account (✅ Done)
  - Web-based UI with flask (✅ Done)
    - On Screen Update Panel via JSON tunnel (✅ Done)
    - Headless Browser Setup for Server (✅ Done)
  - Follow Followers
    - Enter name of instagram user and follow 50 accounts which have followed the account (✅ Done)

### Upcoming Features
- AI-Driven Commenting:
  - Based on the post's content, generate relevant and engaging comments. (❌ Not Done due to unsatisfactory outcomes)

### Setup & Usage
- Import yml file into an anaconda environment.
- Open command line in environment, go to app.py file location.
- Enter python app.py.
- Open browser and open: http://127.0.0.1:5000/

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

