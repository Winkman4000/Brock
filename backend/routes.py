from flask import Blueprint, request, jsonify
from .models import db, Dataset, Model, TrainingRun

bp = Blueprint('api', __name__)


@bp.route('/datasets', methods=['GET', 'POST'])
def datasets_route():
    if request.method == 'POST':
        data = request.get_json() or {}
        dataset = Dataset(name=data.get('name'), description=data.get('description'))
        db.session.add(dataset)
        db.session.commit()
        return jsonify({'id': dataset.id, 'name': dataset.name}), 201
    datasets = Dataset.query.all()
    return jsonify([
        {'id': d.id, 'name': d.name, 'description': d.description}
        for d in datasets
    ])


@bp.route('/models', methods=['GET', 'POST'])
def models_route():
    if request.method == 'POST':
        data = request.get_json() or {}
        model = Model(name=data.get('name'), description=data.get('description'))
        db.session.add(model)
        db.session.commit()
        return jsonify({'id': model.id, 'name': model.name}), 201
    models = Model.query.all()
    return jsonify([
        {'id': m.id, 'name': m.name, 'description': m.description}
        for m in models
    ])


@bp.route('/training_runs', methods=['GET'])
def training_runs_route():
    runs = TrainingRun.query.all()
    return jsonify([
        {
            'id': r.id,
            'model_id': r.model_id,
            'dataset_id': r.dataset_id,
            'started_at': r.started_at,
            'finished_at': r.finished_at,
            'metrics': r.metrics,
        }
        for r in runs
    ])
