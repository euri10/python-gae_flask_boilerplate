from flask import render_template

from . import api


@api.route('/toto')
def toto():

    return render_template('api/toto.html')
