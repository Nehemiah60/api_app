from flask import Blueprint, jsonify, request, abort
from .models import Plant

bp = Blueprint('main', __name__)

Plants_per_page = 5

@bp.route('/')
def get_plants():
    plants = Plant.query.all()
    formatted_output = [plant.format() for plant in plants]
    page = request.args.get('page', 1, type=int)
    start = (page-1) * Plants_per_page
    end = start + Plants_per_page
    return jsonify({'success':True,
                    'plants': formatted_output[start:end],
                    'total_plants':len(plants)})

@bp.route('/plants/<int:plant_id>')
def get_individual_plant(plant_id):
    plants = Plant.query.filter(Plant.id == plant_id).one_or_none()
    if plants is None:
        abort(404)
    else:
        return jsonify({'success': True,
                    'result': plants.format(),
                    'total_plants': len(Plant.query.all())})

@bp.route('/plants/delete/<int:plant_id>', methods=['DELETE'])
def delete_plant(plant_id):
    plants = Plant.query.filter(Plant.id== plant_id).one_or_none()
    if plants is None:
        abort(404)
    else:
        plants.delete()
        return jsonify({'success': True,
                        'deleted_plant':plants.id,
                        'total_plants':len(Plant.query.all())})

@bp.route('/new_plant', methods=['POST'])
def create_plant():
    body = request.get_json()
    
    new_name = body.get('name', None)
    new_scientific_name = body.get('scientific_name', None)
    new_is_poisonous = body.get('is_poisonous', None)
    new_primary_color = body.get('primary_color', None)

    try:
        plant = Plant(name=new_name, scientific_name=new_scientific_name, 
                        is_poisonous=new_is_poisonous, primary_color=new_primary_color)
        plant.insert()

        return jsonify({
            'success': True,
            'plant_created': plant.id,
            'total_plants': len(Plant.query.all())})
    except:
        abort(422)


@bp.errorhandler(404)
def not_found(error):
    return jsonify({'success':False,
                    'error':404,
                    'message': 'Resource not found'}), 404
    
