from app import create_app
from app.db_config import db
from flask import render_template

app = create_app()

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)