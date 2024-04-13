from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/petdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    photoUrls = db.Column(db.Text)  # Changed to Text for flexibility
    tags = db.Column(db.Text)       # Changed to Text for flexibility
    status = db.Column(db.String(50))

@app.route('/pet', methods=['POST', 'PUT'])
def add_or_update_pet():
    if request.method == 'POST':
        return add_pet()
    elif request.method == 'PUT':
        return update_pet()
    else:
        return jsonify({'error': 'Invalid request method'}), 405

def add_pet():
    data = request.json
    new_pet = Pet(
        id=data['id'],
        name=data['name'],
        category=data['category']['name'],  
        photoUrls=','.join(data['photoUrls']),  
        tags=','.join(tag['name'] for tag in data['tags']), 
        status=data['status']
    )
    db.session.add(new_pet)
    db.session.commit()
    return jsonify({'message': 'Pet added successfully'}), 200

def update_pet():
    data = request.json
    pet_id = data.get('id')
    if pet_id is None:
        return jsonify({'error': 'Pet ID not provided'}), 400

    pet = Pet.query.get(pet_id)
    if pet is None:
        return jsonify({'error': 'Pet not found'}), 404

    pet.name = data.get('name', pet.name)
    pet.category = data.get('category', pet.category).get('name',pet.category)
    pet.photoUrls = ','.join(data.get('photoUrls', pet.photoUrls.split(',')))
    pet.tags = ','.join(tag['name'] for tag in data.get('tags', []))
    pet.status = data.get('status', pet.status)

    db.session.commit()
    return jsonify({'message': 'Pet updated successfully'}), 200

@app.route('/pet/<int:pet_id>', methods=['GET', 'POST', 'DELETE'])
def handle_pet(pet_id):
    if request.method == 'GET':
        return get_pet(pet_id)
    elif request.method == 'POST':
        return update_pet2(pet_id)
    elif request.method == 'DELETE':
        return delete_pet(pet_id)
    else:
        return jsonify({'error': 'Invalid request method'}), 405

def get_pet(pet_id):
    try:
        pet = Pet.query.get_or_404(pet_id)
        return jsonify({
            'id': pet.id,
            'name': pet.name,
            'category': pet.category,
            'photoUrls': pet.photoUrls.split(',') if pet.photoUrls else [],
            'tags': pet.tags.split(',') if pet.tags else [],
            'status': pet.status
        })
    except ValueError:
        return jsonify({'error': 'Invalid pet ID'}), 400

def update_pet2(pet_id):
    pet = Pet.query.get(pet_id)
    if pet is None:
        return jsonify({'error': 'Pet not found'}), 404

    data = request.json
    pet.name = data.get('name', pet.name)
    pet.category = data.get('category', pet.category).get('name', pet.category)
    pet.photoUrls = ','.join(data.get('photoUrls', pet.photoUrls.split(',')))
    pet.tags = ','.join(tag['name'] for tag in data.get('tags', []))
    pet.status = data.get('status', pet.status)

    db.session.commit()
    return jsonify({'message': 'Pet updated successfully'}), 200

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': 'Bad request'}), 400

def delete_pet(pet_id):
    # Query the database to find the pet with the given ID
    pet = Pet.query.get(pet_id)
    
    # If the pet doesn't exist, return a 404 error
    if pet is None:
        return jsonify({'error': 'Pet not found'}), 404
    
    # Delete the pet from the database
    db.session.delete(pet)
    db.session.commit()
    
    # Return a success message
    return jsonify({'message': 'Pet deleted successfully'}), 200



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)