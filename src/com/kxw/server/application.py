import tornado.ioloop
import tornado.web
import subprocess


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        branch = self.get_argument('branch')
        url = self.get_argument('url')
        commitid = ''
        cmd = '/usr/bin/git ls-remote %s' % (url)
        handle = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        for line in handle.stdout.read().split('\n'):
                tokens = line.split('\t')
                if (len(tokens) == 2 and tokens[1] == branch):
                        commitid = tokens[0]
                        break
        self.write(commitid)


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
