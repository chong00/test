from flask import Flask, render_template, request
import bleach
from searchform import SearchForm
import copy
from waitress import serve

# Initilization
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"




@app.route("/", methods=["POST", "GET"])
def home():
    form = SearchForm(request.form)

    if request.method == "POST" and form.validate():
        search = form.search.data
        temp = copy.deepcopy(search)
        temp = bleach.clean(temp)
        print(temp)
        print(search)

        if temp == search:
            return render_template("result.html", search=search)
        else:
            return render_template("home.html", form=SearchForm())


    return render_template("home.html", form=form)



# Run server
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")