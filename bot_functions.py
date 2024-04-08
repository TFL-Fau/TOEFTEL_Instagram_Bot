#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
import json
import argparse

import random
from datetime import datetime, timedelta
import os

import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

class CommentGenerator:
    def __init__(self):
        self.comments = [
            "This is absolute perfection! 🌟",
            "You have such a unique perspective.",
            "Gorgeous! I'm in awe.",
            "This is simply breathtaking.",
            "Your creativity knows no bounds.",
            "The details here are exquisite.",
            "Such a beautiful moment captured.",
            "This has made my day!",
            "Every element in this is just right.",
            "Your talent truly shines in this.",
            "Pure magic in every pixel!",
            "I can't take my eyes off this!",
            "The vibe in this is just incredible.",
            "Stunning beyond words.",
            "This is why I love your feed!",
            "Your posts always inspire me.",
            "Masterfully captured.",
            "Art in its truest form.",
            "The colors and composition are just right.",
            "This radiates so much positivity!",
            "I'm feeling all the emotions looking at this.",
            "This speaks volumes.",
            "You've outdone yourself with this one.",
            "An absolute visual treat!",
            "Your content is always top-notch.",
            "I'm lost in the beauty of this.",
            "How do you always get it just right?",
            "This resonates with me deeply.",
            "Pure, unfiltered excellence!",
            "I'm genuinely mesmerized by this.",
            "Another brilliant piece from you!",
            "You have the midas touch with images.",
            "Beauty in every corner of this shot.",
            "Your aesthetic is always on point.",
            "Can't help but double tap on this!",
            "Feels like a scene from a dream.",
            "You've captured the essence perfectly.",
            "In love with every detail here.",
            "This is going straight to my saved collection!",
            "A perfect balance of mood and tone.",
            "Every time I see your posts, I'm amazed.",
            "This is pure artistry.",
            "Feels like a story waiting to be told.",
            "Your feed is an inspiration.",
            "A symphony of colors and emotions.",
            "You've got a keen eye for beauty.",
            "Taking a moment to appreciate this masterpiece.",
            "You never cease to impress.",
            "A visual journey I'm glad to be a part of.",
            "There's so much depth in this.",
            "Your style is unparalleled.",
            "I can look at this all day.",
            "There's a soul in this picture.",
            "This is poetry in image form.",
            "You have a gift, and I'm here for it.",
            "A snapshot of perfection.",
            "This is giving me all the feels!",
            "Every layer of this speaks to me.",
            "This has a timeless beauty.",
            "Your vision always astounds me.",
            "An artful blend of light and emotion.",
            "Another reason why I adore your content.",
            "You've painted a thousand words with this shot.",
            "Keep blessing us with your talent!",
            "In awe of the story this tells.",
            "This is iconic in every sense.",
            "Your captures always stand out.",
            "I'm inspired just looking at this.",
            "You're a true artist with a camera.",
            "Brilliance in every frame.",
            "There's a magic in your content.",
            "This brings so much joy!",
            "Your approach to images is transformative.",
            "This is a treasure in digital form.",
            "The mood in this is just right.",
            "You have an innate sense of beauty.",
            "Loving the narrative in this.",
            "This is transcendent in every way.",
            "Another gem from your collection.",
            "The nuances in this are just beautiful.",
            "You have an art of making images speak.",
            "So much to love in this capture.",
            "Your posts are a ray of sunshine.",
            "The harmony in this is palpable.",
            "Taking in all the beauty of this.",
            "There's a serene elegance to this.",
            "This is more than a picture, it's a feeling.",
            "Lingering over the beauty of this.",
            "This capture is a journey in itself.",
            "Your creativity sets you apart.",
            "The essence of this is simply captivating.",
            "Lost in the charm of this.",
            "Every pixel here tells a tale.",
            "Purely and utterly enchanting.",
            "This deserves all the accolades!",
            "Captivating every essence of beauty.",
            "A tapestry of colors and emotions.",
            "This leaves a lasting impression.",
            "An embodiment of grace and charm.",
            "Elevating digital content with every post!",
            "Your perspective is a breath of fresh air."
        ]
        self.index_comments = 0
        self.iterations_comments = 0
        
        self.message = [
            "Hey there, love your content! Would love if you could check out my page too. Maybe we could share some ideas.",
            "Just stumbled upon your profile and I'm really impressed. Have you had a chance to see my work?",
            "Your content is truly inspiring! Would appreciate your thoughts on my page.",
            "I admire the work you put into your posts. I think we have a similar vibe on my page. Mind taking a look?",
            "I'm genuinely amazed by your content. Let's connect and share ideas.",
            "Love the creativity in your posts! I'd be honored if you checked out mine and shared some feedback.",
            "Your page is a breath of fresh air! Have you had a moment to check out mine?",
            "Hey! Your content is top-notch. Would love to discuss some ideas if you're up for it.",
            "I find your posts really captivating. I think you'd find my content interesting too.",
            "It's rare to come across content as genuine as yours. Hope you can take a moment to view my page.",
            "Truly admire your work. Would love for you to see mine and perhaps share some insights.",
            "Your content stands out! I've got some similar posts on my page. Care to check them out?",
            "I'm always looking for innovative creators like you. Let's connect and share thoughts.",
            "Your posts resonate with me. I believe you'd appreciate my content too.",
            "Kudos on your amazing content! If you have a moment, please check out my page.",
            "Your innovative approach to content is refreshing. Let's collaborate. Have you seen my page?",
            "Your content has a unique flair that I appreciate. I'd love for you to see what I've been up to on my page.",
            "I must say, I'm a fan of your work. Let's connect more and maybe you can check out my content?",
            "I often find inspiration in your posts. Would love to hear your thoughts on my content.",
            "You've got a knack for this! I'd appreciate if you could give my page a look.",
            "Your creativity is through the roof! Have a moment to see my content?",
            "I've been following your content for a while and it's inspiring. I'd love if you could check out my work too.",
            "The dedication in your posts shows. It'd be great to connect and maybe you can view my content?",
            "You bring a unique touch to your content. I believe you'd like my page as well.",
            "I get a lot of motivation from your posts. Hope you can take a moment to view my content.",
            "Your work speaks volumes! I'd be thrilled if you checked out my page.",
            "There's a lot one can learn from your content. I'd love to share some of my work with you too.",
            "I appreciate the effort you put into your content. Let's connect! Maybe you can check out my page?",
            "Your content has a distinctive charm. I invite you to see what I've been creating on my page.",
            "Every post of yours is a masterpiece. Let's share ideas. Have you seen my content?",
            "I've been admiring your content from afar. I think we have a similar taste. Care to see my page?",
            "Your authenticity shines in every post. I'd love for you to experience my content as well.",
            "You're doing an amazing job with your content. It would mean a lot if you checked out my page.",
            "Every post of yours tells a story. I try to do the same on my page. Mind giving it a look?",
            "You have a unique voice in your content. I'd love to share my perspective with you. Have you checked out my page?",
            "Your content is a daily dose of inspiration for many. I'd be grateful if you took a moment to see my work.",
            "The passion you have for your content is evident. I invite you to see my page and maybe we can share some insights.",
            "You're setting the bar high with your content! I'd love to get your opinion on my work.",
            "The creativity in your posts is contagious. I strive for the same energy in my content. Care to give it a look?",
            "I've always been impressed by your content. Would love to hear your thoughts on my page.",
            "Your work is a testament to your dedication. I'd be honored if you took a moment to check out my content.",
            "I'm always on the lookout for authentic content like yours. I believe you'd enjoy my page too.",
            "Your content is both entertaining and informative. I aim for the same balance on my page. Mind checking it out?",
            "Every time I see your posts, I'm inspired to create better content. Would love for you to see my work.",
            "The way you engage with your audience is commendable. I'd be thrilled if you checked out my content and shared your insights.",
            "You have a knack for creating memorable content. I'd love to hear your thoughts on my work.",
            "Your content is a blend of originality and creativity. I believe you'd appreciate my work too. Care to see?",
            "I've been an admirer of your work for quite some time. It'd be great to connect and maybe you can view my content?",
            "Your posts are always a delight to see. I think we share a similar vibe. Mind giving my page a look?",
            "It's evident that you put a lot of thought into your content. I'd be honored if you viewed mine.",
            "You've created a wonderful space here with your content. I invite you to see the world through my posts on my page.",
            "Your content always leaves an impression. Would be great if you could check out my work and share your thoughts.",
            "Every piece of content you create adds value. I strive for the same on my page. Would you mind taking a look?",
            "You have a wonderful way of connecting with your audience. Would love for you to experience my content.",
            "Your posts have a magnetic pull. I believe you'd find my content intriguing as well. Care to check?",
            "I've been looking for content as genuine as yours. It'd be great if you could also give my page a glance.",
            "Your content is like a breath of fresh air. I'd be thrilled if you took a moment to see my work.",
            "You've curated your content beautifully. I invite you to see the stories I've shared on my page.",
            "Every post you share sparks curiosity. Would love to hear your thoughts on my content.",
            "I'm in awe of the creativity in your content. It'd be great to connect and maybe you can check out my page?",
            "Your content is a beautiful blend of heart and art. I believe you'd appreciate my work too.",
            "The stories you share through your content are captivating. I'd love for you to experience mine. Have you checked out my page?",
            "Your content is truly one-of-a-kind. I strive for a similar touch in my work. Mind giving it a look?",
            "The authenticity in your posts is heartwarming. Would love to share my content journey with you.",
            "I've always admired the depth in your content. It'd mean a lot if you checked out my work.",
            "You have a beautiful narrative style in your content. I try to weave similar stories on my page. Care to see?",
            "The vibrancy in your content is unmatched. I'd be honored if you took a moment to view my work.",
            "You have a unique way of presenting content. I'd love to get your perspective on my posts. Have you seen them?",
            "Your content speaks to the heart. I invite you to see the tales I've shared on my page.",
            "Your posts are a reflection of your passion. I'd be thrilled if you could check out my content.",
            "Every piece of content you share resonates deeply. Would love to hear your thoughts on my work.",
            "The artistry in your content is evident. I aim for a similar touch in my posts. Mind checking them out?",
            "Your content is both thought-provoking and delightful. I believe you'd enjoy my page too.",
            "You have an innate ability to create memorable content. I'd be grateful if you took a moment to see my work.",
            "The diversity in your content is inspiring. I'd love for you to experience the range on my page.",
            "You're truly a trendsetter with your content. Would be great if you could give my page a look.",
            "I've been inspired by your content for a while. I think you might appreciate my work too. Care to check?",
            "Your content always brings a smile to my face. Would love to share my stories with you. Have you seen my page?",
            "Your dedication to content creation is commendable. I'd be honored if you checked out my work.",
            "Every post you share is a journey. I invite you to embark on the journeys I've shared on my page.",
            "The richness in your content is unparalleled. It'd be great to connect and maybe you can view my work?",
            "I've been following your content journey and it's truly inspiring. Would love for you to see mine.",
            "Your content is a perfect blend of emotion and creativity. I think you'd appreciate my work too. Care to take a look?",
            "The magic in your content is palpable. I invite you to experience the magic on my page.",
            "Every post of yours has a unique essence. I'd love to hear your thoughts on my content.",
            "Your content is a wonderful escape. I'd be thrilled if you took a moment to explore mine.",
            "I often find solace in your content. Would love to share my world with you. Have you checked out my page?",
            "Your posts are truly a visual treat. I aim for a similar aesthetic in my content. Mind giving it a look?",
            "I'm inspired by the consistency in your content. I'd be honored if you viewed my work.",
            "You've got a special touch when it comes to content. Would love to hear your thoughts on my page.",
            "The stories you weave through your content are mesmerizing. I invite you to see the tales on my page.",
            "Your content always feels fresh and invigorating. It'd be great if you could check out my work."
        ]
        
        self.index_message = 0
        self.iterations_message = 0

        self.comment_post = [
            "I completely agree!",
            "Exactly what I wanted to say.",
            "You've taken the words right out of my mouth.",
            "I see it the same way.",
            "That's what I thought!",
            "Absolutely right.",
            "I agree with you 100%.",
            "You've hit the nail on the head.",
            "That was also my first thought.",
            "Totally agree with you!",
            "You're not alone in your opinion.",
            "I couldn't have put it better myself.",
            "I fully agree.",
            "That was also my impression.",
            "Exactly my thoughts on this.",
            "You are absolutely correct.",
            "Yes, exactly that!",
            "I see it the same way.",
            "You've hit the nail on the head.",
            "I'm glad someone finally said it.",
            "I feel exactly the same.",
            "That's how I see it too.",
            "I couldn't agree more.",
            "Thank you for bringing this up. I feel the same way.",
            "Exactly my words.",
            "That's how I perceived it too.",
            "We agree on this.",
            "You're speaking from my heart.",
            "I think so too.",
            "You've found exactly the words I was missing.",
            "Absolutely correct.",
            "Yes, that's also my view.",
            "I see it just like you do.",
            "You've summarized it perfectly.",
            "We're on the same wavelength.",
            "Exactly right.",
            "I'm with you on this.",
            "That's it!",
            "Exactly so.",
            "I can only agree.",
            "That was also my feeling on it.",
            "Yes, I see it that way too.",
            "I agree with you on every point.",
            "That's exactly it.",
            "I concur.",
            "I can only concur.",
            "That represents my viewpoint as well.",
            "That's also my conviction.",
            "I share your opinion.",
            "That also reflects my thoughts.",
            "That's exactly what I was getting at.",
            "That's exactly my view.",
            "It seems we agree.",
            "You've captured it exactly.",
            "That's also my opinion.",
            "I couldn't put it better myself.",
            "Yes, that's exactly it!",
            "That's how I would have said it.",
            "I find that too.",
            "I can only join in.",
            "You're exactly right.",
            "That's also my perception.",
            "I think the same.",
            "I completely agree with you.",
            "Yes, I see it the same way.",
            "Nothing to add there.",
            "That represents my opinion exactly.",
            "That's how I saw it too.",
            "That's also my conviction.",
            "Yes, exactly that's what I think too.",
            "I wholeheartedly agree.",
            "I see it that way too.",
            "I find that too.",
            "I agree with you.",
            "Yes, that's my position too.",
            "You've expressed exactly what I was thinking.",
            "I agree with you there.",
            "That's also my assessment.",
            "I see it just like you do.",
            "I can only agree.",
            "That's also my perspective.",
            "Yes, I see it that way too.",
            "That's exactly my opinion.",
            "Exactly what I think too.",
            "I see it that way too.",
            "That represents exactly my thoughts on it.",
            "I completely agree with you."
        ]
        
        self.index_comment_post = 0
        self.iterations_comment_post = 0
        
    def get_comment(self):
        if self.iterations_comments >= 2:
            raise Exception("All comments have been used twice!")
        
        comment = self.comments[self.index_comments]
        
        # Move to the next index
        self.index_comments += 1

        # If we've reached the end of the list, reset the index and increment iterations
        if self.index_comments == len(self.comments):
            self.index_comments = 0
            self.iterations_comments += 1
        
        return comment
    
    def get_message(self):
        if self.iterations_message >= 2:
            raise Exception("All comments have been used twice!")
        
        message = self.message[self.index_message]
        
        # Move to the next index
        self.index_message += 1

        # If we've reached the end of the list, reset the index and increment iterations
        if self.index_message == len(self.message):
            self.index_message = 0
            self.iterations_message += 1
        
        return message
    
    def get_comment_response(self):
        if self.iterations_comment_post >= 2:
            raise Exception("All comments have been used twice!")
        
        comment_post = self.comment_post[self.index_comment_post]
        
        # Move to the next index
        self.index_comment_post += 1

        # If we've reached the end of the list, reset the index and increment iterations
        if self.index_comment_post == len(self.comment_post):
            self.index_comment_post = 0
            self.iterations_comment_post += 1
        
        return comment_post

messages = []
    
def add_message(msg):
    messages.append(msg)
    
def get_messages():
    return messages

class InstagramBot:
    
    links = []
    names = []
    
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=930,820")
        #chrome_options.add_argument("--headless")	

        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        self.messages = []
        
    def login(self, email, password):
        # Open Instagram
        self.driver.get("https://www.instagram.com/")
        # Wait for the login elements to become available
        wait = WebDriverWait(self.driver, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        add_message("Found Username and Password field!")
        # Find button for cookies and decline
        try:        
            cookies = self.driver.find_element(By.XPATH, "//button[text()='Optionale Cookies ablehnen']")
            cookies.click()
        except NoSuchElementException:
            add_message("No Cookie button!")
                
        # Find the login elements and enter email and password
        email_field.send_keys(email)
        password_field.send_keys(password)
        add_message("Entered Username and Password!")
        # Submit the login form
        password_field.send_keys(Keys.RETURN)
        
        add_message("Logged in!")
        
        # Wait for the login process to complete (you may need to adjust the delay based on your internet speed)
        time.sleep(10)  # Wait for 5 seconds (adjust as needed)
        
    def get_post_links(self, cls, hashtag):
        
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        time.sleep(8)
        # Find all elements with role="link"
        elements = self.driver.find_elements(By.XPATH, "//a[@role='link']")

        # Extract href values
        hrefs = [element.get_attribute("href") for element in elements if element.get_attribute("href").startswith("https://www.instagram.com/p")]
        
        # Add them to cls
        for href in hrefs:
            cls.links.append(href)
            
        add_message(f"Total number of posts found: {len(hrefs)}")

    def like_posts(self, cls):
        liked_count = 0
        for link in cls.links:
            # Open each post link
            self.driver.get(link)
            time.sleep(2)

            try:               
                if random.random() > 0.25:
                    element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/section[1]/div[1]/span[1]/div/div")
                    ActionChains(self.driver).move_to_element(element).click(element).perform()
                    liked_count += 1
                    add_message(f"Liked Post. Total liked: {liked_count}")

            except Exception as e:
                add_message(f"Post: {link}. Can not be liked, so it got skipped!")
                continue
            
            sleep_duration = random.randint(5, 15)
            time.sleep(sleep_duration)
    
    def comment_on_posts_and_like(self, cls):
        likes = 0
        comment_gen = CommentGenerator()
        for link in cls.links:
            # Open each post link
            self.driver.get(link)
            time.sleep(2)

            try:
                # Find the comment input field
                comment_input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Kommentieren …"]')
                comment_input.click()
                time.sleep(1)

                if random.random() > 0.5:
                    comment_input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Kommentieren …"]')
                    comment_input.click()
                    time.sleep(1)

                    actions = ActionChains(self.driver)
                    actions.send_keys(comment_gen.get_comment())
                    actions.send_keys(Keys.RETURN)
                    actions.perform()
                
                if random.random() > 0.25:
                    element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/section[1]/div[1]/span[1]/div/div")
                    ActionChains(self.driver).move_to_element(element).click(element).perform()

            except Exception as e:
                add_message(f"No comment option for post {link}. So it got skipped!")
                continue
            
            sleep_duration = random.randint(5, 15)
            time.sleep(sleep_duration)
    
    def follow_and_save(self, cls):
        
        names = []
        
        for link in cls.links:
            self.driver.get(link)
            sleep_duration = random.randint(5, 15)
            time.sleep(sleep_duration)
                        
            try:
                follow_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Folgen']")))
                follow_button.click()
                time.sleep(2)
                element = self.driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/span/span/div/a/div/div/span')

                # Check if the name is not already in the list
                if element.text not in names:
                    # Extract the text and save it to a variable
                    names.append(element.text)
                    print(names)  # This should print the latest name appended to the list
                else:
                    add_message(f"{element.text} is already in the list.")
            
            except Exception as e:
                add_message("More posters so it got skipped!")
                
                continue
        
        # Save followed names and timestamp in file
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Create the path for the file based on the timestamp
        file_path = os.path.join('followed_accounts', f"{timestamp}.txt")

        # Write to the file
        with open(file_path, 'w') as file:
            for name in names:
                file.write(f"{name}\n")

        add_message(f"Names saved to file: {file_path}.")
    
    def follow_save_like_comment(self, cls, account_name):
        
        names = []
        comment_gen = CommentGenerator()
        for link in cls.links:
            # Open each post link
            self.driver.get(link)
            time.sleep(2)
            try:
                element = self.driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/span/span/div/a/div/div/span')
                
                if element.text not in cls.names:
                    cls.names.append(element.text)
                    add_message(cls.names)
                    
                    follow_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Folgen']")))
                    follow_button.click()
                    time.sleep(2)
                    
                    if random.random() > 0.35:
                        comment_input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Kommentieren …"]')
                        comment_input.click()
                        time.sleep(1)

                        actions = ActionChains(self.driver)
                        actions.send_keys(comment_gen.get_comment())
                        actions.send_keys(Keys.RETURN)
                        actions.perform()
                
                if random.random() > 0.25:
                    element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/section[1]/div[1]/span[1]/div/div")
                    ActionChains(self.driver).move_to_element(element).click(element).perform()
                    
                else:
                    add_message(f"{element.text} is already in the list.")
                
            except Exception as e:
                add_message("Skipping...")
            sleep_duration = random.randint(5, 15)
            time.sleep(sleep_duration)
            
        # Save followed names and timestamp in file
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        
        # Create folder for account
        
        folder_path = os.getcwd() + "\\followed_accounts\\" + account_name.lower()
        
        if not os.path.exists(folder_path):
            # Ordner erstellen, falls er nicht existiert
            os.makedirs(folder_path)
            add_message(f"Folder {folder_path} got created.")
        else:
            add_message(f"Folder {folder_path} already exists.")
        
        # Create the path for the file based on the timestamp
        file_path = os.path.join('followed_accounts\\'+account_name.lower(), f"{timestamp}.txt")
        
        # Write to the file
        with open(file_path, 'w') as file:
            for name in cls.names:
                file.write(f"{name}\n")

        add_message(f"Names saved to file: {file_path} in folder {account_name.lower()}.")
    
    def process_files_in_directory(self, name):
        # Get the current date and time
        time.sleep(10)
        current_datetime = datetime.now()
        
        self.driver.get("https://www.instagram.com/" + name.lower()+ "/following/")
        
        followed_elements = self.driver.find_elements(By.XPATH, "//*[text()='Gefolgt']")
        
        # Check if the text is '0'
        if len(followed_elements) == 0:
            add_message("Account got no followers, so checking files in folder!")
            # Define folder path
            folder_path = "followed_accounts\\"+name

            # Check if folder exists
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                # List all files in folder
                files = os.listdir(folder_path)

                # Check if list is empty
                if not files:
                    add_message(f"There are no files in folder {folder_path}.")
                else:
                    # Go through all files in folder
                    for filename in files:
                        # Check if file is a txt file
                        if filename.endswith(".txt"):
                            file_path = os.path.join(folder_path, filename)

                            # Check if its a file and delete it
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)
                                print(f"File {file_path} got deleted.")
                                add_message(f"File {file_path} got deleted.")

                    add_message(f"All files in folder {folder_path} got deleted.")
            else:
                add_message("Folder does not exist!")
        else:
            add_message("Checking files in folder for account!")
            # Iterate over each file in the directory
            for file_name in os.listdir("followed_accounts"):
                # Check if the file is a .txt file
                if file_name.endswith('.txt'):
                    # Extract the timestamp from the file name
                    try:
                        file_datetime = datetime.strptime(file_name, "%Y-%m-%d_%H-%M-%S.txt")
                    except ValueError:
                        # If the filename doesn't match the expected format, skip it
                        continue

                    # If the file is older than 3 days
                    if (current_datetime - file_datetime) > timedelta(days=3):
                        # Open the file and do something
                        with open(os.path.join("followed_accounts", file_name), 'r') as f:
                            names = f.readlines()

                        # Process each name
                        for name in names:
                            try:
                                self.driver.get("https://www.instagram.com/" + name)
                                time.sleep(2)
                                unfollow_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Gefolgt']")))
                                unfollow_button.click()
                                time.sleep(1)
                                confirm_unfollow = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Nicht mehr folgen']")))
                                confirm_unfollow.click()

                            except TimeoutException:
                                continue
                        # Delete the file after processing it
                        os.remove(os.path.join("followed_accounts", file_name))

                        add_message(f"Unfollowed all accounts from {file_name}. And deleted file!")
                    else:
                        add_message(f"Skipping file: {file_name} as it's not older than 3 days.")
     
    def send_dm(self, cls):
        # Go to the Instagram Direct Inbox
        add_message("Going to inbox to send dms!")
        self.driver.get("https://www.instagram.com/direct/inbox/")
        comment_gen = CommentGenerator()
        time.sleep(10)
        
        notifications =  self.driver.find_element(By.CLASS_NAME, "_a9_1")
        notifications.click()
       
        for username in cls.names:
            self.driver.get("https://www.instagram.com/direct/inbox/")
            time.sleep(10)
             # Click the 'New Message' button
            new_message_button = self.driver.find_element(By.XPATH, '//*[@aria-label="Neue Nachricht"]')
            new_message_button.click()
            time.sleep(2)

            # Wait for the recipient input field to become available
            wait = WebDriverWait(self.driver, 10)
            recipient_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')))

            # Type each username and press Enter to add as a recipient
            recipient_input.send_keys(username)
            time.sleep(5)
            
            try:
                select_user = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[3]/div/label/div/input')
                add_message("Sended message to user!")
                time.sleep(10)
            except Exception as e:
                print("Did not find name!")
                add_message("Did not find name!")
                continue
            
            select_user.click()
            
            select_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')))
            select_button.click()
            time.sleep(2)

            comment_input = self.driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div')
            comment_input.click()
            time.sleep(1)

            actions = ActionChains(self.driver)
            actions.send_keys(comment_gen.get_message())
            actions.send_keys(Keys.RETURN)
            actions.perform()
    
            sleep_duration = random.randint(5, 15)
            time.sleep(sleep_duration)

    def unfollow_all(self, name):
        
        self.driver.get("https://www.instagram.com/" + name.lower() + "/following/")
        time.sleep(10)
        add_message("Starting to unfollow accounts!")
        
        while True:
            try:

                # Find all items with the text “Followed”
                followed_elements = self.driver.find_elements(By.XPATH, "//*[text()='Gefolgt']")

                # If no more elements are found, end the loop
                if not followed_elements[1:]:
                    break

                # Go through the list of items found and click on each one
                for index, element in enumerate(followed_elements):
                    # If this is the first item, skip
                    if index == 0:
                        continue
                
                    try:
                        element.click()
                        add_message("Unfollowed account!")
                    except ElementClickInterceptedException:
                        add_message("Refreshing page!")
                        self.driver.refresh()
                
                    time.sleep(1)
                    # Wait until the item is visible and click on it
                    nicht_mehr_folgen_button = self.driver.find_element(By.XPATH, "//button[text()='Nicht mehr folgen']")
                    nicht_mehr_folgen_button.click()
                    time.sleep(2)  # Wait a few seconds between clicks


                # Reload website
                self.driver.refresh()
                time.sleep(5)  # Wait a few seconds for the page to fully reload
            
            except NoSuchElementException:
                # Reload website
                self.driver.refresh()
                time.sleep(5)  # Wait a few seconds for the page to fully reload
        add_message("Finished unfollowing accounts on page!") 
        # Define folder path
        folder_path = "followed_accounts\\"+name.lower()

        # Check if folder exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # List all files in folder
            files = os.listdir(folder_path)

            # Check if list is empty
            if not files:
                add_message(f"There are no file in folder {folder_path}.")
            else:
                # Go through all files in folder
                for filename in files:
                    # Check if file is a txt file
                    if filename.endswith(".txt"):
                        file_path = os.path.join(folder_path, filename)

                        # Check if its a file and delete it
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                            add_message(f"File {file_path} got deleted.")

                print(f"All files in folder {folder_path} got deleted.")
                add_message(f"All files in folder {folder_path} got deleted.")
        else:
            print("Folder does not exist!")
            add_message("Folder does not exist!")
            
    def answer_comments(self, name):
        self.driver.get("https://www.instagram.com/" + name.lower() + "/")
        time.sleep(5)
        # Select all <a> elements with the given class name
        links_elements = self.driver.find_elements(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w')

        # Save the href attributes of the selected elements in a list
        hrefs = [link.get_attribute('href') for link in links_elements]

        # Filter the list to only keep URLs that start with 'https://www.instagram.com/p/'
        filtered_urls = [url for url in hrefs if url.startswith('https://www.instagram.com/p/')]

        answer_gen = CommentGenerator()
        
        for url in filtered_urls:
            self.driver.get(url)
            antworten_elements = self.driver.find_elements(By.XPATH,"//*[contains(text(), 'Antworten')]")
            for antwort in antworten_elements:
                antwort.click()
                time.sleep(2)
                try:
                    element = self.driver.find_element(By.XPATH,'//textarea[@placeholder="Kommentieren …"]')
                    actions = ActionChains(self.driver)
                    actions.send_keys(answer_gen.get_comment_response())
                    actions.send_keys(Keys.RETURN)
                    actions.perform()
                    sleep_duration = random.randint(2, 5)
                    time.sleep(sleep_duration)			
                except NoSuchElementException:
                    add_message("This Post can't be commented!")
                    
    def follow_followers(self,name):
        self.driver.get("https://www.instagram.com/" + name.lower() + "/followers/")
        time.sleep(5)
        followed_counter = 0
        
        # Find all items with the text “Followed”
        try:
            followed_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[.//div[contains(text(), 'Folgen')]]"))
            )
            # Now you can work with followed_elements
        except TimeoutException:
            add_message("Timed out waiting for elements to appear")
        
        # Go through the list of items found and click on each one
        for index, element in enumerate(followed_elements):
            # If this is the first item, skip
            if index == 0:
                continue
            if followed_elements!=50:
                try:
                    element.click()
                    followed_counter+=1
                    add_message("Followed " + str(followed_counter) + " accounts following " + str(name) + ".")
                    sleep_duration = random.randint(1, 5)
                    time.sleep(sleep_duration)
                except ElementClickInterceptedException:
                    add_message("Could not find element. Finished Task!")
                    break
            else:
                break
        add_message("Finished following Followers!")

    def like_stories(self, cls):

        time.sleep(2)
        
        # Click Start page
        element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/span/div/a/div/div[2]/div/div/span/span")
        ActionChains(self.driver).move_to_element(element).click(element).perform()

        time.sleep(2)

        # Deactivate Notifications
        element = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        ActionChains(self.driver).move_to_element(element).click(element).perform()
        
        # Click first story
        element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/div/div[2]/div/div/div/div/div/div/ul/li[3]/div/button")
        ActionChains(self.driver).move_to_element(element).click(element).perform()

        time.sleep(5)
        
        counter = 0
        last_href = None 

        while counter <= 30:
            time.sleep(2)
            try:
                element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/header/div[2]/div[1]/div/div[2]/div/div[1]/a")
                current_href = element.get_attribute("href")
                print(current_href)
            except Exception as e:
                # Click next
                try:
                    next_element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div")
                    ActionChains(self.driver).move_to_element(next_element).click(next_element).perform()
                except Exception as e:
                    print("Finished liking all new stories! Start again for liking existing ones!")
                    break

            if current_href != last_href:

                last_href = current_href
                
                # Click like
                try:
                    like_element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[3]/div/div/div[2]/div[1]/span/div/div")
                    ActionChains(self.driver).move_to_element(like_element).click(like_element).perform()
                except Exception as e:
                    print("Could not like the post, probably an advertisement")
                    # Click next
                    try:
                        next_element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div")
                        ActionChains(self.driver).move_to_element(next_element).click(next_element).perform()
                    except Exception as e:
                        print("Finished liking all new stories! Start again for liking existing ones!")
                        break
                    
                counter += 1
                print(counter)
            else:
                # Click next
                try:
                    next_element = self.driver.find_element(By.XPATH, "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div")
                    ActionChains(self.driver).move_to_element(next_element).click(next_element).perform()
                except Exception as e:
                    print("Could not click next.")

# In[4]:

def start_bot(hashtags_user, name, passwort, methods, accountname):
    hashtags = hashtags_user
    
    bot = InstagramBot()
    bot.login(email=name, password=passwort)
    
    if len(hashtags[0]) - 1 < 3:
        add_message("No Hashtags were given, continuing code!")
    else:
        for hashtag in hashtags:
            print(f"Starting getting links for hashtag: {hashtag}")
            add_message(f"Starting getting links for hashtag: {hashtag}")

            bot.get_post_links(bot, hashtag=hashtag)

            add_message(f"Finished getting links for hashtag: {hashtag}")
        
    # Now you can call methods on each based on the selected methods
    for method in methods:
        if method == "comment_on_posts_and_like":
            bot.comment_on_posts_and_like(bot)
        elif method == "follow_and_save":
            bot.follow_and_save(bot)
        elif method == "follow_save_like_comment":
            bot.follow_save_like_comment(bot, name)
        elif method == "send_dm":
            bot.send_dm(bot)
        elif method == "unfollow_all":
            bot.unfollow_all(name)
        elif method == "follow_followers":
            bot.follow_followers(accountname)
        elif method == "answer_comments":
            bot.answer_comments(accountname)
        elif method == "like_posts":
            bot.like_posts(bot)
        elif method == "like_stories":
            bot.like_stories(bot)
    bot.process_files_in_directory(name)
    print("Finished all Tasks. Have a nice day!")
    add_message("Finished all Tasks. Have a nice day!")
    bot.driver.quit()