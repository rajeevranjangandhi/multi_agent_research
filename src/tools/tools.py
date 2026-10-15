from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os
from tavily import TavilyClient
from rich import print
load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query:str)->str:
    """Search the web for recent and reliable information on a topic. Return titles, url """
    results = tavily.search(query=query,max_result=5)
    print(results)
    output=[]
    for r in results['results']:
        output.append(f"Title:{r['title']}\nURL:{r['url']}\nContent:{r['content']}\n")


    return output