# commands/web.py
import webbrowser

def search_web(query: str):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
