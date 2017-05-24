# facebook-messenger-bot-tutorial

 教你建立自己的 facebook-messenger-bot 使用 Python Django 📝

facebook-messenger-bot-tutorial use Python Django

* [Youtube Tutorial](https://youtu.be/6DQ6v1hcNyk)

* [Youtube Demo](https://youtu.be/DzT6mZw3rds)

## 執行畫面

![alt tag](http://i.imgur.com/FS83MG4.jpg)

![alt tag](http://i.imgur.com/nJn2ozI.jpg)

![alt tag](http://i.imgur.com/kKD7a30.jpg)

![alt tag](http://i.imgur.com/r2Av5Vo.jpg)

![alt tag](http://i.imgur.com/WoDdetG.jpg)

![alt tag](http://i.imgur.com/goZP7i4.jpg)

![alt tag](http://i.imgur.com/71FAoj3.jpg)

![alt tag](http://i.imgur.com/nb9DL4B.jpg)

![alt tag](http://i.imgur.com/W07B7Bk.jpg)

希望這個 阿肥bot 能幫助大家，程式碼基本上就是很簡單的爬蟲。

如果需要其他的功能，可以給小弟一點建議，我會盡量完成他。

## 教學

請先到 [facebook-developers](https://developers.facebook.com/) 這裡登入自己原本的 facebook 帳號，然後點選 右上角 選 **新增應用程式**

![alt tag](http://i.imgur.com/g4TrPVL.jpg)

填寫一些設定，填完後，按 **建立應用程式編號**

![alt tag](http://i.imgur.com/7EvjG6X.jpg)

接下來，先選擇左方的 新增產品 ，  再選擇 Messenger

![alt tag](http://i.imgur.com/K97O3BL.jpg)

再設定裡面的 **權杖產生** 裡，必須先申請一個 粉絲專頁，如果沒有請先申請，直接點選即可申請

![alt tag](http://i.imgur.com/duTUQk5.jpg)

![alt tag](http://i.imgur.com/wmNRyqs.jpg)

新增完粉絲專業之後，可以看到自己的 token (權杖)，記得選自己的粉絲專頁

![alt tag](http://i.imgur.com/oUcxLWJ.jpg)

接著把 [fb_setting.py](https://github.com/twtrubiks/facebook-messenger-bot-tutorial/blob/master/mybot/fb_setting.py) 裡面的內容改成自己的，如下

ACCESS_TOKEN 就是你的 token  (權杖)

VERIFY_TOKEN 可以隨便打

```python
ACCESS_TOKEN = "xxxx"

VERIFY_TOKEN = "1234567890"
```

接著先將程式執行起來。

### 如何使用 ngrok

請去下載 [ngrok](https://ngrok.com/) ，免安裝版本，解壓縮即可使用，

是什麼呢?  簡單說，就是讓自己的內網 ( 也就是 localhost) 可以讓別人看的到，

好處是什麼呢?  讓我們可以在本機測試自己的 bot

那該如何使用

首先，請用 cmd 切換到 ngrok.exe 路徑底下，然後輸入

```cmd
ngrok http 8000
```

![alt tag](http://i.imgur.com/p9lczTx.jpg)

如果路徑正確，你應該會看到下圖

紅色框框就是你要用的網址，記得選 https

![alt tag](http://i.imgur.com/W1qdiFE.jpg)

接著找到 Webhooks ，然後按編輯 (如果你找不到，第一次他會在 Messenger 裡面)

![alt tag](http://i.imgur.com/SGYsfvT.jpg)

將 **網址** 以及你的 **VERIFY_TOKEN**  貼到下方 ，

**網址**: [https://5d3e3183.ngrok.io/fb_mybot/callback/]( https://6bba624c.ngrok.io) (請貼你自己的)

**VERIFY_TOKEN** : 1234567890 (自己任意設定即可)

![alt tag](http://i.imgur.com/hq3ACIo.jpg)

如果你設定完全正確，你的 cmd 應該會顯示 200 OK

![alt tag](http://i.imgur.com/CNEQAab.jpg)

如果沒顯示 200 OK，請再查查看哪裡錯誤了，

檢查是不是忘記訂閱 Webhooks 了

![alt tag](http://i.imgur.com/3mE60G1.jpg)

### 佈署

目前沒有部屬，因為 FACEBOOK 審核我覺得有點麻煩，所以就暫時沒有佈署了。

## 其他補充

* 目前僅有本機測試 ( 未部屬 heroku 以及 通過 FB 的審核)，直接密粉絲團 bot 不會有反應。

* 只要有使用到網址，請記得一定都要用 **https**。

* [ngrok](https://ngrok.com/) 如果重開，網址會改變，需要重新設定你的 Webhooks。 ( 設定完之後，有時候會慢一點才會有反應)

## 執行環境

* Python 3.4.3 + Django

## Reference

* [facebook messengerr-platform](https://developers.facebook.com/docs/messenger-platform)
* [Django](https://github.com/django/django)

## License

MIT license
