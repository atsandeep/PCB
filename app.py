# app.py

from flask import Flask, render_template, request
from pcbuilder2 import PCBuilder  # Import your PC Builder program

app = Flask(__name__)
pc_builder = PCBuilder()  # Initialize PCBuilder instance


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/build_pc', methods=['POST'])
def build_pc():
    # Retrieve user inputs from the form
    budget = float(request.form['budget'])
    usage = request.form['usage']
    storage = request.form['storage']
    storage_type = request.form['storage_type']
    graphics_card = request.form['graphics_card']
    processor_preference = request.form['processor_preference']

    # Set user specifications
    pc_builder.specifications['budget'] = budget
    pc_builder.specifications['usage'] = usage
    pc_builder.specifications['storage'] = storage
    pc_builder.specifications['storage_type'] = storage_type
    pc_builder.specifications['graphics_card'] = graphics_card
    pc_builder.specifications['processor_preference'] = processor_preference

    # Build PC and get recommendations
    recommendations = pc_builder.build_pc()
    return render_template('result.html',recommendation=recommendations)


if __name__ == '__main__':
    app.run(debug=True)