from crypt import methods
from flask import render_template

from . import app
from .forms import ImageRequestForm


@app.route('/', methods=["GET", "POST"]) 
def index():
    print('index')
    form = ImageRequestForm()
    if form.validate_on_submit():
        image_description = form.image_description.data
        print(f'Request for image recived: f{image_description}')
        form.image_description.data = ''
    return render_template('index.jinja-html', form=form)


@app.route('/anerkjennelser') 
def attributions():
    print('Render attributions')
    return render_template('attributions.jinja-html')
