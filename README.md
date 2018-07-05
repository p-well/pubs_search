# Nearest Moscow Bars

This script will help you to navigate better in the diversity of Moscow bars - it can find the biggest and the smallest bars <br />
as well as the closest bar to you.

The input data is retrieved by scrits from the Moscow City Government Open Data [data.mos.ru](https://data.mos.ru/) in JSON format.


Pavel Kadantsev, 2018. <br/>
p.a.kadantsev@gmail.com


# Installation

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and install dependencies using ```pip install -r requirements.txt``` in CLI. <br />
It is recommended to use virtual environment to keep clean your global scope.


# Usage

To execute the script use the following command in CLI: ```python bars.py```
You need to except some delays when running script due to the connection and server response.

To find the nearest bar your have to enter your GPS coordinates: latitude and longitude respectively.


# Example of Script Launch

<pre>
<b> >python bars.py </b>

The biggest Moscow bar is "Спорт бар «Красная машина»".
It has 450 seats and located at "Автозаводская улица, дом 23, строение 1".

The smallest Moscow bar is "Сушистор".
It has 0 seats and located at "город Москва, Михалковская улица, дом 8".

Now let's find the closest to you bar. Type your coordinates -
latitude and longitude, like: 55.753215 и 37.622504.

Latitude:55.753215
Longitude:37.622504

The closest bar is "ТД ГУМ Кафе фестивальное Бар Кинозал" with 40 seats. Address: "город Москва, Красная площадь, дом 3".
</pre>


# Project Goals

The code is written for educational purposes. Training course for web-developers -[DEVMAN.org](https://devman.org)
