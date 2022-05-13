from pprint import pprint

from newsapi.newsapi_client import NewsApiClient
from googletrans import Translator

def news(q,i):
    if q=="Дощ" or q=="дощ" or q=="rain" or q=="Rain":
        raise Exception
    translator = Translator()
    newsapi = NewsApiClient(api_key="e9b6e421ccb44bad912783bcd8800b43")
    if "lang=en" in (str(translator.detect(q))):
        newss = translator.translate(q,src="en",dest="en").text
        data_2 = newsapi.get_top_headlines(q=f"{newss}")
        dict_news = {
            "title": f'{translator.translate((data_2["articles"][i]["title"]), dest="uk").text}',
            "author": f'{translator.translate((data_2["articles"][i]["author"]), dest="uk").text}',
            "urltoimage": f'{data_2["articles"][i]["urlToImage"]}',
            "url": f'{data_2["articles"][i]["url"]}',
            "description": f'{translator.translate((data_2["articles"][i]["description"]), dest="uk").text}',
            "data": data_2
        }
        return dict_news
    else:
        try:
            b=str(translator.detect(translator.translate(q, src="uk", dest="en")))
            if "lang=en" in b:
                newss = translator.translate(q, src="uk", dest="en").text
                data_2 = newsapi.get_top_headlines(q=f"{newss}")
                dict_news = {
                    "title": f'{translator.translate((data_2["articles"][i]["title"]), dest="uk").text}',
                    "author": f'{translator.translate((data_2["articles"][i]["author"]), dest="uk").text}',
                    "urltoimage": f'{data_2["articles"][i]["urlToImage"]}',
                    "url": f'{data_2["articles"][i]["url"]}',
                    "description": f'{translator.translate((data_2["articles"][i]["description"]), dest="uk").text}',
                    "data": data_2
                }
                return dict_news
            else:
                raise Exception
        except:
            return None
