import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

def calculate_company_age():
    birth_time = datetime(year=1920,day=1,month=1)
    company_age = birth_time.year - datetime.now().year

    return company_age

def convert_age_to_string(age):
    if age % 10 == 1 and age != 11:
        return f'{age} год'
    pass

if __name__ == "__main__":
    company_age = calculate_company_age()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
        )

    template = env.get_template('template.html')
    rendered_page = template.render(company_age=company_age)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()