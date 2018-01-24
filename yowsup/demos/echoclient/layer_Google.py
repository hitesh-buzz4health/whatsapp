from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from google import google
import requests

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        # Setup Microsoft
        subscription_key = "96d05359d76f4e758906539daeab939e"
        assert subscription_key   
        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
        params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        search_results["webPages"]["value"][0]["snippet"]


        refined_results = ""
        term = messageProtocolEntity.getBody()            
        if term.startswith( '#' ):
            term.replace("#","site:medscape.com")
            term.replace("#","")

            num_page = 3
            search_results = google.search(term, num_page)
            refined_results = search_results[0].description# + "   \n" + "Source: " + search_results[0].link# + search_results[1].description + search_results[2].description
        else:
            refined_results = "BOOTNI KE HASH DAAL PEHLE " + messageProtocolEntity.getBody()                
        messageProtocolEntity.setBody(refined_results) 
        self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    def searchForTerm(self, messageProtocolEntity):
        if term.startswith( '#' ):
            term.replace("#","")
            num_page = 3
            search_results = google.search(term, num_page)
            refined_results = search_results[0].description #+ search_results[1].description + search_results[2].description
            return refined_results
        else:
            return messageProtocolEntity.getBody()    
            
    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        print("Rcedddddd")
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
