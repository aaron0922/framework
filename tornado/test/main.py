import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    # 此函式處理 GET Request，並輸出文字訊息
    def get(self):
        self.write("Hello, Tornado!")
        # 若想拋出 HTTP 錯誤，如 403
        # raise tornado.web.HTTPError(403)

    # 此函式處理 POST Request，並輸出文字訊息
    def post(self):
        self.write("Hello, Tornado!")

if __name__ == "__main__":
    # 自訂 Request 派送機制
    application = tornado.web.Application([
        # 設定 Request URL 為 http://your.site/ 時由 IndexHandlder 負責處理
        (r"/", IndexHandler)
    ])
    # 設定 port 為 8888
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()