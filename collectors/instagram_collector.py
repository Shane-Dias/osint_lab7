import instaloader, os
import time
import random
from dotenv import load_dotenv
load_dotenv()

def fetch_instagram(username="nasa", limit=5):
    L = instaloader.Instaloader()
    results = []
    
    # Set up Instaloader to be less aggressive
    L.request_timeout = 300
    L.sleep = True
    L.sleep_between_requests = 5  # 5 seconds between requests
    
    try:
        # Try anonymous session first
        profile = instaloader.Profile.from_username(L.context, username)
        
        post_count = 0
        for post in profile.get_posts():
            if post_count >= limit:
                break
                
            # Add random delay to avoid detection
            time.sleep(random.uniform(2, 6))
            
            results.append({
                "platform": "instagram",
                "user": username,
                "timestamp": post.date,
                "text": post.caption if post.caption else "",
                "url": f"https://www.instagram.com/p/{post.shortcode}/",
                "likes": post.likes,
                "comments": post.comments
            })
            post_count += 1
            
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Instagram profile '{username}' does not exist")
    except instaloader.exceptions.ConnectionException:
        print("Error: Connection failed. Instagram may be blocking requests.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Instagram error: {e}")
        # Retry with login if available
        return fetch_instagram_with_login(username, limit)
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return results

def fetch_instagram_with_login(username="nasa", limit=5):
    """Alternative method with login credentials"""
    L = instaloader.Instaloader()
    results = []
    
    try:
        USERNAME = os.getenv("INSTA_USERNAME")  
        PASSWORD = os.getenv("INSTA_PASSWORD")  
        
        L.login(USERNAME, PASSWORD)
        print("Logged in to Instagram successfully")
        
        profile = instaloader.Profile.from_username(L.context, username)
        
        post_count = 0
        for post in profile.get_posts():
            if post_count >= limit:
                break
                
            time.sleep(random.uniform(3, 8))  # Longer delays when logged in
            
            results.append({
                "platform": "instagram",
                "user": username,
                "timestamp": post.date,
                "text": post.caption if post.caption else "",
                "url": f"https://www.instagram.com/p/{post.shortcode}/"
            })
            post_count += 1
            
    except Exception as e:
        print(f"Instagram login error: {e}")
    
    return results