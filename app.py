from flask import Flask
from config import Config
from controllers.lti import shared_lti

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(shared_lti)

# Injeta o app no LTI manualmente após registro
for rule in app.url_map.iter_rules():
    view_func = app.view_functions[rule.endpoint]
    if hasattr(view_func, '__lti_view_decorator__'):
        view_func.__globals__['app'] = app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)