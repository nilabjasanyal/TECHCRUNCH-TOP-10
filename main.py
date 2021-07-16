import smtplib

import requests
from  datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

response = requests.get(url=f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=59d39e95596540b8b8cc34b45495310d")

@app.route('/')
def hello():
    return render_template('index.html',details=response.json()['articles'])

@app.route('/<date>')
def post(date):
    for data in response.json()['articles']:
        if data['publishedAt']==date:
            title = data['title']
            content = data['content']
            url = data['url']
            img = data['urlToImage']

    return render_template('post.html',title=title,content=content,url=url,img=img)



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login',methods=["POST"])
def send_mail():
    name = request.form['name']
    contact = request.form['contact']
    message= request.form['message']
    email = request.form['email']
    # return f'<h1>{first_name}</h1>\n<h1>{contact}\n{message}\n{email}</h1>'

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user='nilabja.2000@gmail.com', password='18sep2000')

        connection.sendmail(from_addr='nilabja.2000@gmail.com',
                            to_addrs=email,
                            msg=f'Subject: FROM WEBPAGE\nNAME:{name}\nCONTACT:{contact}\n{message}')

    return render_template('sent.html')


if __name__ == '__main__':
    app.run(debug=True)


