from flask import Flask
from API.Routes.DelRoutes import api as del_api
from API.Routes.GetRoutes import api as get_api
from API.Routes.PostRoutes import api as post_api
from API.Routes.PutRoutes import api as put_api
from API.Routes.PatchRoutes import api as patch_api

app = Flask(__name__)

app.register_blueprint(del_api)
app.register_blueprint(get_api)
app.register_blueprint(post_api)
app.register_blueprint(put_api)
app.register_blueprint(patch_api)
if __name__ == '__main__':
    app.run(debug=True)
