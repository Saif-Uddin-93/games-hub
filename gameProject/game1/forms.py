from django.forms import Form, CharField, TextInput, Textarea

class GameTitle(Form):
    attrs = {
        "data": {
            "wrapperClass": "form"
        },
        "type": "text",
        "id": "game-title",
        "placeholder": "Enter title here"
    }
    user_input = CharField(widget=TextInput(attrs=attrs), label="Game Title:")

class GameDescription(Form):
    attrs = {
        "data": {
            "wrapperClass": "form"
        },
        "type": "text",
        "id": "game-description",
        "placeholder": "Enter description here"
    }
    user_input = CharField(widget=Textarea(attrs=attrs), label="Game Description:")