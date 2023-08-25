import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

def calculate_company_age():
    birth_time = datetime(year=1920,day=1,month=1)
    company_age = datetime.now().year - birth_time.year

    return company_age

def convert_age_to_string(age):

    if age % 100 < 21 and age % 100 > 4:
        return f'{age} лет'
    elif age % 10 == 1:
        return f'{age} год'
    else:
        return f'{age} года'

def preprocess_wine_df(df: pd.DataFrame):
    df.columns = ['name', 'type', 'price', 'image']
    wines = df.to_dict('records')
    return wines

if __name__ == "__main__":
    company_age = calculate_company_age()
    company_age_context = convert_age_to_string(company_age)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
        )
    template = env.get_template('template.html')
    df = pd.read_excel('wine.xlsx')
    wines = preprocess_wine_df(df)
    rendered_page = template.render(company_age_context=company_age_context,
                                    wines=wines)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
