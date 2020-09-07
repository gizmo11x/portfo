from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

    # !!!!!!!! https://flask.palletsprojects.com/en/1.1.x/quickstart/
# activating the virtual environment we created: venv\Scripts\activate
# in the console(powershell) we need to run these 2 commands every time: $env:FLASK_APP = "server.py" and flask run


# dinamically so we don't have to do approute for every page
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# data is in a dictionary so we can manipulate its parts


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # passing data on to the writer directly as a list
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # we grab the data the user submitted and put into a dictionary variable
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        # when the form is submitted we get redirected to the thankyou html
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'
