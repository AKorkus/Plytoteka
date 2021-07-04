from flask import Flask, request, redirect, render_template, url_for
from forms import AlbumForm
from models import albums
from os import path


UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/albums/", methods=["GET", "POST"])
def albums_list():
    here = path.join(app.config['UPLOAD_FOLDER'])
    print(here)
    form = AlbumForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            file = request.files['file']
            file.save(path.join(app.config['UPLOAD_FOLDER'], file.filename))
            albums.create(form.data, file.filename)
            albums.save_all()

        return redirect(url_for("albums_list"))

    return render_template("albums.html", form=form, albums=albums.all(), error=error)


@app.route("/albums/<int:album_id>/", methods=["GET", "POST"])
def album_details(album_id):

    album = albums.get(album_id - 1)
    form = AlbumForm(data=album)
    # print(album)
    if request.method == "POST":
        if form.validate_on_submit():
            file = request.files['file']
            file.save(path.join(app.config['UPLOAD_FOLDER'], file.filename))
            albums.update(album_id - 1, form.data, file.filename)

        return redirect(url_for("albums_list"))

    return render_template("album.html", form=form, album_id=album_id, cover=album['cover'])


# LAUNCH.........................................................................................................................
if __name__ == "__main__":
    app.run(debug=False)
