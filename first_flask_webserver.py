# make flask webserver that does the same thing
import flask
app = flask.Flask(__name__)
# display people information
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)
people = []
people.append(Person("Hannah", 38))
people.append(Person("Sally", 23))
people.append(Person("Peter", 52))
people.append(Person("Mary", 19))
people.append(Person("John", 32))
@app.route("/")
def index():
    return flask.render_template("index.html", people=people)
app.run()
# Path: templates/index.html
# <html>
# <head>
#     <title>People</title>
# </head>
# <body>
#     <h1>People</h1>
#     <table>
#         <tr>
#             <th>Name</th>
#             <th>Age</th>
#         </tr>
#         {% for person in people %}
#         <tr>
#             <td>{{ person.name }}</td>
#             <td>{{ person.age }}</td>
#         </tr>
#         {% endfor %}
#     </table>
# </body>
# </html>