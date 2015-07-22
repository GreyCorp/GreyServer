import tornado.ioloop
import tornado.web

import grey.config as CONFIG
from grey.routes.auth import AuthRoute
from grey.routes.user import UserRoute

def main(debug = True, port = CONFIG.PORT):
    application = tornado.web.Application([
        AuthRoute,
        UserRoute
    ], debug = debug
     , autoreload = debug)

    application.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
