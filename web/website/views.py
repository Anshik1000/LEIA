from flask import Blueprint,render_template,request,Flask,redirect,url_for,flash
import base64
from PIL import Image
from io import BytesIO
import os
from flask_login import  login_required,current_user
import numpy as np
import tensorflow as tf

views = Blueprint('views',__name__)
appli = Flask(__name__)
@views.route('/')
def home():
    if current_user.is_authenticated:
          return redirect(url_for('views.homepage'))
    return render_template("index.html")

@views.route('/quiz')
def quiz():
    return render_template("quiz2.html")

@views.route('/game',methods=['GET','POST'])
@login_required
def game():
        # Get the image data URL from the request
        if (request.method == 'POST'):
             
            data = request.json
            image_data_url = data.get("image_data")
            
            # Remove the "data:image/png;base64," prefix
            image_data = image_data_url.split(",")[1]

            # Decode the base64 image data
            image_data_decoded = base64.b64decode(image_data)

            # Create a PIL image from the decoded image data
            image = Image.open(BytesIO(image_data_decoded))

            # Save the image to a file (optional)
            image_path = os.path.join(appli.root_path, "watchgame","dataset","single_prediction","images.png" )
            image.save(image_path)

            # Perform any other processing here
            print("Image saved!!")

            test_image = tf.keras.preprocessing.image.load_img(image_path, target_size = (64, 64))
            test_image = tf.keras.preprocessing.image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            cnn = tf.keras.models.load_model(os.path.join(appli.root_path, "watchgame","nn.keras" ))
            result = cnn.predict(test_image/255)
            print(result[0][0])
            if result[0][0] > 0.5:
                flash_message = 'Awesome! You drew a watch! See what features you are missing.'
                flash(flash_message, category='success')
                print(flash_message)
            else:
                flash_message = "You weren't able to draw most of the features! See what you did wrong."
                flash(flash_message, category='error')
                print(flash_message)

            
        return render_template('recognition.html')


@views.route('/home')
@login_required
def homepage():
    return render_template('learnerpath.html')
