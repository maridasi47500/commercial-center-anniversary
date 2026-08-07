from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_showcase", methods=["GET","POST"])
def add_one_showcase():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into showcase (css_style,html_page,next_opening) values (:css_style,:html_page,:next_opening)",hey)
        user = query_db('select * from showcase')

        return render_template("showcaseform.html", showcases=user, one_user=one_user, the_title="add new showcase")


    user = query_db('select * from showcase')
    one_user = query_db("select * from showcase limit 1", one=True)
    return render_template("showcaseform.html", showcases=user, one_user=one_user, the_title="add new showcase")

@app.route("/add_one_shop", methods=["GET","POST"])
def add_one_shop():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesshop_type= query_db("select * from shop_type")

        one_user = query_db("insert into shop (name,shop_type_id,opened_on) values (:name,:shop_type_id,:opened_on)",hey)
        user = query_db('select * from shop')

        return render_template("shopform.html", shops=user, one_user=one_user, the_title="add new shop", touslesshop_type=touslesshop_type)


    touslesshop_type= query_db("select * from shop_type")

    user = query_db('select * from shop')
    one_user = query_db("select * from shop limit 1", one=True)
    return render_template("shopform.html", shops=user, one_user=one_user, the_title="add new shop", touslesshop_type=touslesshop_type)

@app.route("/add_one_shop_type", methods=["GET","POST"])
def add_one_shop_type():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into shop_type (name,description) values (:name,:description)",hey)
        user = query_db('select * from shop_type')

        return render_template("shop_typeform.html", shop_types=user, one_user=one_user, the_title="add new shop_type")


    user = query_db('select * from shop_type')
    one_user = query_db("select * from shop_type limit 1", one=True)
    return render_template("shop_typeform.html", shop_types=user, one_user=one_user, the_title="add new shop_type")

@app.route("/add_one_anniversary", methods=["GET","POST"])
def add_one_anniversary():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesshop= query_db("select * from shop")

        one_user = query_db("insert into anniversary (shop_id,year,message) values (:shop_id,:year,:message)",hey)
        user = query_db('select * from anniversary')

        return render_template("anniversaryform.html", anniversarys=user, one_user=one_user, the_title="add new anniversary", touslesshop=touslesshop)


    touslesshop= query_db("select * from shop")

    user = query_db('select * from anniversary')
    one_user = query_db("select * from anniversary limit 1", one=True)
    return render_template("anniversaryform.html", anniversarys=user, one_user=one_user, the_title="add new anniversary", touslesshop=touslesshop)

