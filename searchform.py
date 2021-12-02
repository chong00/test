from wtforms import Form, StringField
from wtforms.validators import InputRequired

class SearchForm(Form):
    search = StringField("Search", [
    InputRequired()
])
