#utility.py
import requests

def searchForTerm(term):
    
    if term.startswith( '#' ):
        #term.replace("#","site:medscape.com")
        term = term.replace("#","site:medscape.com filetype:pdf ")
        print("Searching for " + term)
        # Setup Microsoft
        subscription_key = "96d05359d76f4e758906539daeab939e"
        assert subscription_key   
        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
        params  = {"q": term, "textDecorations":True, "textFormat":"HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        refined_results = search_results["webPages"]["value"][0]["snippet"]
        refined_results = refined_results.replace("<b>","*")
        refined_results = refined_results.replace("</b>","*") #+ "  " + search_results["webPages"]["value"][0]["snippet"]# + search_results["Entity"]["image"][0]["hostUrl"] + search_results["webPages"]["value"][0]["url"]
        refined_results = refined_results + " " + search_results["webPages"]["value"][0]["url"]



    else:
        refined_results = "*Echoing your message: " + term + "* For search type # followed by search term "     

    return refined_results 
