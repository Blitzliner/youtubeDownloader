import os
import subprocess

def main():
    current_dir = "C:\\Users\\Blitzliner\\Documents\\git\\youtubeDownloder\\out"
    
    if not os.path.isdir(current_dir):
        os.mkdir(current_dir)
        
    current_dir = os.path.join(current_dir, "%(title)s.%(ext)s")
    
    with open('parse_links.txt', 'r') as myfile:
        data = myfile.read()
        
    split_data = data.split("\n")
    for link in split_data:
        if not link.startswith("#"):
            print(link)
            args = ["youtube-dl", "--extract-audio", "--audio-format", "mp3", "--audio-quality", "0", "--youtube-skip-dash-manifest", "-o", current_dir, link]
            call_str = " ".join(args)
            print(call_str)
            
            subprocess.call(args)
    
    
if __name__== "__main__":
  main()