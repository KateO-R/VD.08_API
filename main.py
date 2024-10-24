from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
   weather = None #формируем условия проверки метода. Форму пока не создавали, но из неё будем брать только город.
   quote = get_random_quote()
   if request.method == 'POST':
       city = request.form['city']  #этот определенный город будем брать для запроса API
       weather = get_weather(city)
   return render_template("index.html", weather=weather, quote=quote)

def get_weather(city):
    api_key = "bfb2bef52e1935d5ff2a3156c9fc3402"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_random_quote():
    # Возвращаем цитату
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            return {
                "content": data["content"],
                "author": data["author"]
            }
        else:
            print("Error fetching quote:", response.status_code)
            return {
                "content": "Be yourself; everyone else is already taken.",
                "author": "Oscar Wilde"
            }
    except Exception as e:
        print("Exception occurred:", e)
        return {
            "content": "Be yourself; everyone else is already taken.",
            "author": "Oscar Wilde"
        }

if __name__ == "__main__":
    app.run(debug=True)
