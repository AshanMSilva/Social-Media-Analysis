from social_media_analysis import create_app

app = create_app()
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
 
if __name__ == '__main__':
    app.run(debug=True)
