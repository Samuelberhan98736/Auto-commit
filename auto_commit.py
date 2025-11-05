import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Configuration from .env
REPO_PATH = os.getenv('REPO_PATH')
GITHUB_USERNAME = "Samuelberhan98736"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = "Auto-commit"

def auto_commit():
    # Check if environment variables are loaded
    if not GITHUB_TOKEN:
        print(" Error: GITHUB_TOKEN not found in .env file!")
        return
    
    if not REPO_PATH:
        print(" Error: REPO_PATH not found in .env file!")
        return
    
    try:
        # Change to repository directory
        os.chdir(REPO_PATH)
        print(f"Working in: {os.getcwd()}")
        
        # Make change
        with open("commit_log.txt", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Commit at: {timestamp}\n")
        print(" Updated commit_log.txt")
        
        # Git operations
        subprocess.run(["git", "add", "."], check=True)
        print("Files added to git")
        
        commit_message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Commit created")
        
        # Push to GitHub
        push_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
        subprocess.run(["git", "push", push_url, "main"], check=True)
        print("Pushed to GitHub")
        
        print(f" Successfully committed at {datetime.now()}")
        
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    auto_commit()