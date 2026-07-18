#!/usr/bin/python3

import json
import csv

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

    items_list = data.get("items", [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    # sourcing
    source = request.args.get('source')
    product_id = request.args.get('id')
    # if statement between csv or json
    if source == "json":
        try: 
            with open("products.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error="products.json not found")
            

    elif source == "csv":
        try:
            data = []
            with open("products.csv", 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                    data.append(row)
        except FileNotFoundError:
            return render_template('product_display.html', error="products.csv not found")
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Invalid id")
        
        filtered = [product for product in data if product["id"] == product_id]

        if not filtered:
            return render_template('product_display.html', error="Product not found")
        
        data = filtered
    # the found template
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

