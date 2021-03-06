from flask import request
from flask import render_template
from datetime import datetime, timedelta
from app.controllers.graphic import Graphic, pytz

# Index
def index():
    # Datas para preenchimento do formulário
    tz_local = pytz.timezone('America/Bahia')
    if request.method != "POST":
        dfinal = str(datetime.now().astimezone(tz_local)).replace(" ", "T")[:16]
        dinicial = str((datetime.now() - timedelta(days=1)).astimezone(tz_local)).replace(" ", "T")[:16]
    else:
        dfinal = request.form["dfinal"]
        dinicial = request.form["dinicial"]

    return render_template("index.html", graph=Graphic(), dfinal=dfinal, dinicial=dinicial)
