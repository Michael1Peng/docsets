import os
import requests
from urllib.parse import urljoin
import base64
import json
import concurrent.futures
from typing import List, Dict, Union
from dataclasses import dataclass

@dataclass
class DownloadConfig:
    github_url: str
    local_path: str

# Configuration list - add your download tasks here
DOWNLOAD_CONFIGS = [
    DownloadConfig(
        github_url="https://github.com/frdel/agent-zero/tree/main/docs",
        local_path="/home/michael/ubuntu-repos/docsets/agent-zero"
    ),
]

class GitHubDownloader:
    def __init__(self, config: DownloadConfig, token=None):
        self.github_url = config.github_url
        self.local_path = config.local_path
        self.api_base = "https://api.github.com/"
        self.headers = {
            'User-Agent': 'GitHub-Folder-Downloader/1.0',
            'Accept': 'application/vnd.github.v3+json'
        }
        if token:
            self.headers['Authorization'] = f'token {token}'
        
    def parse_github_url(self):
        # Remove 'https://github.com/' from the URL
        path = self.github_url.replace("https://github.com/", "")
        parts = path.split("/")
        
        # Extract owner, repo, branch and path
        owner = parts[0]
        repo = parts[1]
        branch = "main"  # Default to main
        folder_path = ""
        
        if "tree" in parts:
            branch_index = parts.index("tree") + 1
            branch = parts[branch_index]
            folder_path = "/".join(parts[branch_index + 1:])
        
        return owner, repo, branch, folder_path
    
    def download_file(self, file_url, local_file_path):
        """Download a single file"""
        print(f"Downloading: {os.path.basename(local_file_path)}")
        file_response = requests.get(file_url, headers=self.headers)
        
        if file_response.status_code == 200:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            with open(local_file_path, 'wb') as f:
                f.write(file_response.content)
            return True
        else:
            print(f"Failed to download {os.path.basename(local_file_path)}")
            return False

    def process_contents(self, contents, current_path=""):
        """Recursively process contents of a directory"""
        for item in contents:
            if item['type'] == 'file':
                # Only download markdown files
                if item['name'].lower().endswith('.md'):
                    file_url = item['download_url']
                    relative_path = os.path.join(current_path, item['name'])
                    local_file_path = os.path.join(self.local_path, relative_path)
                    self.download_file(file_url, local_file_path)
            
            elif item['type'] == 'dir':
                # Get contents of subdirectory
                dir_url = item['url']
                response = requests.get(dir_url, headers=self.headers)
                if response.status_code == 200:
                    subdir_contents = response.json()
                    # Recursively process subdirectory
                    new_path = os.path.join(current_path, item['name'])
                    self.process_contents(subdir_contents, new_path)
                else:
                    print(f"Failed to access directory: {item['name']}")
    
    def download_folder(self) -> bool:
        owner, repo, branch, folder_path = self.parse_github_url()
        
        # Create API URL
        api_url = f"repos/{owner}/{repo}/contents/{folder_path}"
        if branch != "main":
            api_url += f"?ref={branch}"
            
        response = requests.get(urljoin(self.api_base, api_url), headers=self.headers)
        if response.status_code != 200:
            print(f"Error accessing GitHub API: {response.status_code} for {self.github_url}")
            if response.status_code == 403:
                print("Rate limit exceeded or authentication required")
                print("Please provide a GitHub token using the GITHUB_TOKEN environment variable")
            return False
            
        contents = response.json()
        
        # Create local directory if it doesn't exist
        os.makedirs(self.local_path, exist_ok=True)
        
        # Process contents recursively
        self.process_contents(contents)
        return True

def download_single_config(config: DownloadConfig, github_token: str) -> bool:
    """Helper function for concurrent downloads"""
    print(f"\nStarting download from: {config.github_url}")
    print(f"Downloading to: {config.local_path}")
    
    downloader = GitHubDownloader(config, github_token)
    success = downloader.download_folder()
    
    if success:
        print(f"Successfully downloaded markdown files to {config.local_path}")
    else:
        print(f"Failed to download files from {config.github_url}")
    
    return success

def main():
    # Get GitHub token from environment variable
    github_token = os.environ.get('GITHUB_TOKEN')
    
    print("Starting GitHub Folder Downloader")
    print(f"Found {len(DOWNLOAD_CONFIGS)} download configurations")
    print("Only .md files will be downloaded")
    if github_token:
        print("Using GitHub token from environment")
    else:
        print("No GitHub token found. API rate limits will be restricted")
    print("-" * 50)
    
    # Use ThreadPoolExecutor for concurrent downloads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Create a list of futures
        future_to_config = {
            executor.submit(download_single_config, config, github_token): config
            for config in DOWNLOAD_CONFIGS
        }
        
        # Process completed downloads
        successful_downloads = 0
        for future in concurrent.futures.as_completed(future_to_config):
            config = future_to_config[future]
            try:
                if future.result():
                    successful_downloads += 1
            except Exception as e:
                print(f"Error downloading from {config.github_url}: {str(e)}")
    
    # Print summary
    print("\nDownload Summary")
    print("-" * 50)
    print(f"Total configurations: {len(DOWNLOAD_CONFIGS)}")
    print(f"Successful downloads: {successful_downloads}")
    print(f"Failed downloads: {len(DOWNLOAD_CONFIGS) - successful_downloads}")

if __name__ == "__main__":
    main() 
