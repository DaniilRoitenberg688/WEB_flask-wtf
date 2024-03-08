from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/<title>')
# @app.route('/index/<title>')
# def index(title):
#     return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('index1.html', title=prof, prof=prof)


@app.route('/list_prof/<list_type>')
def professions(list_type):
    profs = ["слесарь", "врач", "инженер", "строитель", "программист"]
    return render_template('index2.html', list=list_type, profs=profs)


@app.route('/distribution/<all_members>')
def write_all_members(all_members):
    print(all_members)
    return render_template('home_1.html', people=all_members.split())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')