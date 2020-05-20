from social_media_analysis import create_app
from social_media_analysis.config import Config
app = create_app(config_class=Config)

if __name__ == '__main__':
    app.run(debug=True)
