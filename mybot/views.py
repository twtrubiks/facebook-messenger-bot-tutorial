import random
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from mybot.model_cmd import *
from mybot.messenger_api import *
from mybot.fb_setting import *


def post_facebook_message(fbid, recevied_message):
    # user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    # user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    # user_details = requests.get(user_details_url, user_details_params).json()

    fb = FbMessageApi(fbid)

    if recevied_message == "eyny":
        content = eynyMovie()
        fb.text_message(content)
        return 0
    if recevied_message == "蘋果即時新聞":
        content = appleNews()
        fb.text_message(content)
        return 0
    if recevied_message == "近期上映電影":
        content = movie()
        fb.text_message(content)
        return 0
    if recevied_message == "科技新報":
        content = technews()
        fb.text_message(content)
        return 0
    if recevied_message == "PanX泛科技":
        content = panx()
        fb.text_message(content)
        return 0
    if recevied_message == "PTT 表特版 近期大於 10 推的文章":
        content = pttBeauty()
        fb.text_message(content)
        return 0
    if recevied_message == "一張正妹圖片" or recevied_message == "二張正妹圖片" or recevied_message == "三張正妹圖片":
        count = 0
        if recevied_message[0] == "一":
            count = 1
        if recevied_message[0] == "二":
            count = 2
        if recevied_message[0] == "三":
            count = 3
        for i in range(count):
            index_pic = random.randint(0, len(picture) - 1)
            fb.image_message(picture[index_pic])
        return 0
    if recevied_message == "開始玩":
        data = [
            {
                "type": "postback",
                "title": "新聞",
                "payload": "新聞"
            },
            {
                "type": "postback",
                "title": "電影",
                "payload": "電影"
            },
            {
                "type": "postback",
                "title": "正妹",
                "payload": "正妹"
            }
        ]
        fb.template_message(
            title="選擇服務",
            image_url="https://i.imgur.com/xQF5dZT.jpg",
            subtitle="請選擇",
            data=data)
        return 0
    if recevied_message == "新聞":
        data = [
            {
                "type": "postback",
                "title": "蘋果即時新聞",
                "payload": "蘋果即時新聞"
            },
            {
                "type": "postback",
                "title": "科技新報",
                "payload": "科技新報"
            },
            {
                "type": "postback",
                "title": "PanX泛科技",
                "payload": "PanX泛科技"
            }
        ]
        fb.template_message(
            title="新聞類型",
            image_url="https://i.imgur.com/vkqbLnz.png",
            subtitle="請選擇",
            data=data)
        return 0
    if recevied_message == "電影":
        data = [
            {
                "type": "postback",
                "title": "近期上映電影",
                "payload": "近期上映電影"
            },
            {
                "type": "postback",
                "title": "eyny",
                "payload": "eyny"
            }
        ]
        fb.template_message(
            title="服務類型",
            image_url="https://i.imgur.com/sbOTJt4.png",
            subtitle="請選擇",
            data=data)

        return 0
    if recevied_message == "正妹":
        data = [
            {
                "type": "postback",
                "title": "PTT 表特版 近期大於 10 推的文章",
                "payload": "PTT 表特版 近期大於 10 推的文章"
            },
            {
                "type": "postback",
                "title": "正妹圖片",
                "payload": "正妹圖片"
            }
        ]
        fb.template_message(
            title="服務類型",
            image_url="https://i.imgur.com/qKkE2bj.jpg",
            subtitle="請選擇",
            data=data)
        return 0
    if recevied_message == "正妹圖片":
        data = [
            {
                "content_type": "text",
                "title": "一張正妹圖片",
                "payload": "一張正妹圖片"
            },
            {
                "content_type": "text",
                "title": "二張正妹圖片",
                "payload": "二張正妹圖片"
            },
            {
                "content_type": "text",
                "title": "三張正妹圖片",
                "payload": "三張正妹圖片"
            }
        ]
        fb.quick_reply_message(
            text="想要看幾張正妹圖片呢?",
            quick_replies=data)
        return 0
    data = [
        {
            "type": "postback",
            "title": "開始玩",
            "payload": "開始玩"
        },
        {
            "type": "web_url",
            "url": "https://github.com/twtrubiks/facebook-messenger-bot-tutorial",
            "title": "如何建立自己的 bot"
        }, {
            "type": "web_url",
            "url": "https://www.facebook.com/TWTRubiks?ref=bookmarks",
            "title": "聯絡作者"
        }
    ]
    fb.template_message(
        title="服務類型",
        image_url="https://i.imgur.com/kzi5kKy.jpg",
        subtitle="請選擇",
        data=data)


class MyBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    # pprint(message)
                    print('message')
                    try:
                        post_facebook_message(message['sender']['id'], message['message']['text'])
                    except:
                        return HttpResponse()
                if 'postback' in message:
                    # pprint(message)
                    print('postback')
                    try:
                        post_facebook_message(message['sender']['id'], message['postback']['payload'])
                    except:
                        return HttpResponse()

        return HttpResponse()
