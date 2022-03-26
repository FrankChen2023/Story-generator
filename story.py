from flask import Flask, render_template
from faker import Faker
from faker.providers import company, job, person, geo, lorem

app = Flask(__name__)

def story():
    fake = Faker()
    company = fake.company()
    language_name = fake.language_name()
    domain_word = fake.domain_word()
    name = fake.name()
    catch_phrase = fake.catch_phrase()
    job = fake.job()
    file_name = fake.file_name()
    sentence = fake.sentence()
    mystory = (
        f"In a(n) {company}"
        f" a young {language_name} stumbles across a(n) "
        f"{domain_word} which spurs him into conflict with " 
        f"{name} an {catch_phrase}"
        f" with the help of a(n) {job} "
        f" and her {file_name} culminating in a struggle in "
        f"{company} where someone shouts: '{sentence}'"
    )
    return mystory

@app.route('/')
def index():
    storys = []
    for i in range(5):
        storys.append(story())
    return render_template("index.html", storys = storys)