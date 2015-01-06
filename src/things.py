import falcon

class ThingsResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nhello world\n\n')

app = falcon.API()
things = ThingsResource()
app.add_route('/things', things)
