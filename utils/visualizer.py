import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud  # Now this will import the library, not your file
import os

def generate_wordcloud(db_path="data/osint.db"):
    """Generate a word cloud from the database text content"""
    try:
        # Get absolute path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if db_path.startswith("data/"):
            db_path = os.path.join(os.path.dirname(current_dir), db_path)
        
        print(f"📂 Generating word cloud from: {db_path}")
        
        if not os.path.exists(db_path):
            print("❌ Database file not found!")
            return
        
        conn = sqlite3.connect(db_path)
        df = pd.read_sql("SELECT text FROM osint_data WHERE text IS NOT NULL AND text != ''", conn)
        conn.close()
        
        if len(df) == 0:
            print("❌ No text data available for word cloud")
            return
        
        # Combine all text
        text = " ".join(df['text'].dropna())
        
        if not text.strip():
            print("❌ No valid text content for word cloud")
            return
        
        # Generate word cloud
        wordcloud = WordCloud(
            width=1200, 
            height=600, 
            background_color='white',
            max_words=100,
            colormap='viridis',
            stopwords=None  
        ).generate(text)
        
        # Create plot
        plt.figure(figsize=(15, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Collected OSINT Data', fontsize=16, fontweight='bold')
        
        # Save and show
        screenshots_dir = os.path.join(os.path.dirname(current_dir), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        wordcloud_path = os.path.join(screenshots_dir, "wordcloud.png")
        plt.savefig(wordcloud_path, dpi=300, bbox_inches='tight')
        print(f"✅ Word cloud saved to: {wordcloud_path}")
        plt.show()
        
    except Exception as e:
        print(f"❌ Error generating word cloud: {e}")

# Add to your existing visualizer.py functions
def plot_sentiment(db_path="data/osint.db"):
    # Your existing sentiment function here
    pass

if __name__ == "__main__":
    generate_wordcloud()
    # plot_sentiment()  # Uncomment if you want to run sentiment analysis instead