from flask import Flask, render_template, url_for

app = Flask(__name__)


tours = {
    1: {
        "title": "GEOMETRIKA • lounge hotel",
        "description": "Красивое место, чистый воздух, сосновый лес, вид на гору, "
                       "которая радует буйством осенних красок. А самое привлекательное - "
                       "интересная архитектура домиков и название отеля им под стать.",
        "departure": "Новосибирск",
        "stars": "5,0", "reviews": "(1)",
        "picture": ""
    },
    2: {
        "title": "АЛТЕРИЯ Эко мини-отель",
        "description": "Мини отель находиться в поселке Чемал, на берегу Катуни!"
        "Номер идеальный, чистота, имеется все необходимое вплоть до зубных наборов, мыла и геля для душа!",
        "stars": "4,9", "reviews": "(82)",
        "picture": ""
    },
    3: {
        "title": "Парк-Отель Манжерок",
        "description": "Расположение отеля удобное, особенно для тех, кто прилетел на самолёте "
                       "и не имеет личного транспорта. Рядом река, в шаговой доступности магазины, рынок."
                       "В отеле завтрак это шведский стол. Все очень вкусное и свежее.",
        "stars": "4,4", "reviews": "566",
        "picture": ""
    }
}


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/Direction')
def direction():
    return render_template("Direction.html")


@app.route('/Tours')
def tour():

    return render_template("Tours.html")


@app.route('/super/mega/secret/code/password:3211488690000123')
def monkey():
    tours_1 = tours[1]
    tours_2 = tours[2]
    tours_3 = tours[3]
    return render_template("monkey.html", tours_1=tours_1, tours_2=tours_2, tours_3=tours_3)


if __name__ == "main":
    app.run(debug=True)
