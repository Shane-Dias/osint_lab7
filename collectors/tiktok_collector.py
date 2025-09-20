from TikTokApi import TikTokApi
import asyncio

def fetch_tiktok(hashtag="cybersecurity", count=5):
    """
    Fetch TikTok videos by hashtag
    Note: TikTok scraping is unreliable and may require frequent updates
    """
    results = []
    
    try:
        # Initialize the API
        api = TikTokApi()
        
        # Get videos by hashtag - newer syntax
        videos = api.hashtag(name=hashtag).videos(count=count)
        
        # Convert async generator to list
        video_list = list(videos)
        
        for video in video_list:
            results.append({
                "platform": "tiktok",
                "user": video.author.username if video.author else "unknown",
                "timestamp": str(video.create_time) if hasattr(video, 'create_time') else "unknown",
                "text": video.desc if hasattr(video, 'desc') else "",
                "url": f"https://www.tiktok.com/@{video.author.username}/video/{video.id}" if video.author else f"https://www.tiktok.com/video/{video.id}",
                "likes": video.stats.digg_count if hasattr(video, 'stats') else 0,
                "views": video.stats.play_count if hasattr(video, 'stats') else 0
            })
            
    except Exception as e:
        print(f"TikTok API error: {e}")
        # Fallback to empty results instead of crashing
        return []
    
    return results
