from models.textModel import Text,db
from models.menuDataModel import MenuData
from flask import request, jsonify
import requests
def get_text():
    texts = Text.query.all()
    if texts:
        text_list = [{'content': text.content} for text in texts]
        return jsonify(text_list)
    else:
        return jsonify({'content': 'No texts available'})
def get_menu():
    menu = MenuData.query.all()
    if menu:
        menu_list = [{'label': item.label, 'rule': item.rule, 'type': item.type, 'params': item.params} for item in menu]
        return jsonify(menu_list)
    else:
        return jsonify({'data': 'No data available'})

def create_text():
    content = request.form.get('content')

    if not content:
        return jsonify({'message': 'Content is required'}), 400

    text = Text(content=content)
    db.session.add(text)
    db.session.commit()
    
    return jsonify({'message': 'Text created successfully', 'id': text.id}), 201

def add_menu_items():
    try:
        data = request.get_json()
        menu_data = data.get('menuData', [])
        menu_items = []

        for item in menu_data:
            label = item.get('label')
            rule = item.get('rule')
            item_type = item.get('type')
            params = item.get('params', {})

            menu_item = MenuData(
                label=label if label is not None else None,
                rule=rule if rule is not None else None,
                type=item_type if item_type is not None else None,
                params=params if params is not None else None
            )
            menu_items.append(menu_item)

        db.session.add_all(menu_items) 
        db.session.commit()

        return jsonify({"message": "Population records added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

   
def get_us_population_data():
    api_url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            population_data = [
                {
                    'year': int(entry['Year']),
                    'population': int(entry['Population'])
                }
                for entry in data['data']
            ]

            return jsonify(population_data)

        else:
            return jsonify({'error': 'Failed to fetch data from the external API'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500
