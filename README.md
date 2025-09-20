# OSINT Data Collection Pipeline 🔍

## 📋 Project Description
An automated **Open Source Intelligence (OSINT)** aggregation system that collects, processes, and analyzes public data from social media platforms.  

Designed for:
- Cybersecurity research  
- Threat intelligence  
- Digital forensics applications  

The pipeline features **multi-platform data collection, sentiment analysis, and structured database storage**.

**Integrated Platforms:**  
- Twitter  
- Reddit  
- Quora  
- GitHub  

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.9+
- API keys for **Twitter** and **Reddit**

### Step-by-Step Installation

#### 1. Clone and Navigate
```bash
git clone https://github.com/Shane-Dias/osint_lab7.git
cd osint_lab7

2. Create Virtual Environment
# Windows
python -m venv osint_env
osint_env\Scripts\activate

# Linux/Mac
python -m venv osint_env
source osint_env/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure API Keys
# Copy environment file
cp .env.example .env


Edit .env with your actual keys:

REDDIT_ID=
REDDIT_SECRET=
GITHUB_TOKEN=
TWITTER_BEARER_TOKEN=

# Run complete pipeline (collection + processing + storage)
python main.py
# View database contents
python main.py --view-db

# Generate visualizations
python visualization_controller.py --sentiment
python visualization_controller.py --wordcloud
python visualization_controller.py --all
