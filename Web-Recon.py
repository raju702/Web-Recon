import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

interesting_extensions = [".js", ".json", ".xml", ".config", ".conf", ".env"]

def is_interesting_file(url):
    return any(url.lower().endswith(ext) for ext in interesting_extensions)

def create_domain_folder(base_url):
    parsed = urlparse(base_url)
    domain = parsed.netloc.replace("www.", "")
    script_dir = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(script_dir, "download", domain)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def fetch_interesting_files(base_url):
    folder = create_domain_folder(base_url)
    try:
        print(f"[+] Scanning {base_url}")
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all(["script", "link", "a"], src=True) + \
               soup.find_all(["script", "link", "a"], href=True)

        urls = set()
        for tag in tags:
            attr = "src" if tag.has_attr("src") else "href"
            file_url = urljoin(base_url, tag.get(attr))
            if is_interesting_file(file_url):
                urls.add(file_url)

        for file_url in urls:
            try:
                parsed = urlparse(file_url)
                filename = os.path.basename(parsed.path)
                if not filename:
                    continue
                print(f"[+] Downloading {file_url}")
                file_resp = requests.get(file_url, timeout=10)
                file_resp.raise_for_status()

                with open(os.path.join(folder, filename), 'w', encoding='utf-8') as f:
                    f.write(file_resp.text)
            except Exception as fe:
                print(f"[-] Failed to fetch {file_url}: {fe}")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL (e.g. https://example.com): ").strip()
    fetch_interesting_files(target_url)
