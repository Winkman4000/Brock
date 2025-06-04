from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Dataset(db.Model):
    __tablename__ = 'datasets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())


class Sample(db.Model):
    __tablename__ = 'samples'
    id = db.Column(db.Integer, primary_key=True)
    dataset_id = db.Column(db.Integer, db.ForeignKey('datasets.id'), nullable=False)
    features = db.Column(db.LargeBinary)
    label = db.Column(db.String(100))
    dataset = db.relationship('Dataset', backref=db.backref('samples', lazy=True))


class Model(db.Model):
    __tablename__ = 'models'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())


class Layer(db.Model):
    __tablename__ = 'layers'
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('models.id'), nullable=False)
    layer_index = db.Column(db.Integer)
    layer_type = db.Column(db.String(50))
    parameters = db.Column(db.JSON)
    model = db.relationship('Model', backref=db.backref('layers', lazy=True))


class Weight(db.Model):
    __tablename__ = 'weights'
    id = db.Column(db.Integer, primary_key=True)
    layer_id = db.Column(db.Integer, db.ForeignKey('layers.id'), nullable=False)
    weight_data = db.Column(db.LargeBinary)
    bias_data = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    layer = db.relationship('Layer', backref=db.backref('weights', lazy=True))


class TrainingRun(db.Model):
    __tablename__ = 'training_runs'
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('models.id'), nullable=False)
    dataset_id = db.Column(db.Integer, db.ForeignKey('datasets.id'), nullable=False)
    started_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    finished_at = db.Column(db.DateTime)
    metrics = db.Column(db.JSON)
    model = db.relationship('Model', backref=db.backref('training_runs', lazy=True))
    dataset = db.relationship('Dataset', backref=db.backref('training_runs', lazy=True))
