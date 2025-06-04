-- SQL script to create a generic database for storing neural network
-- datasets, models, and the associated weights.

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS nn_weights_db;
USE nn_weights_db;

-- Table of datasets used for training
CREATE TABLE datasets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Samples belonging to a dataset
CREATE TABLE samples (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dataset_id INT NOT NULL,
    features BLOB,
    label VARCHAR(100),
    FOREIGN KEY (dataset_id) REFERENCES datasets(id)
);

-- Definition of a neural network model
CREATE TABLE models (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Individual layers that compose a model
CREATE TABLE layers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    layer_index INT,
    layer_type VARCHAR(50),
    parameters JSON,
    FOREIGN KEY (model_id) REFERENCES models(id)
);

-- Weights associated with a layer
CREATE TABLE weights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    layer_id INT NOT NULL,
    weight_data BLOB,
    bias_data BLOB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (layer_id) REFERENCES layers(id)
);

-- Training runs that produce weights for a model
CREATE TABLE training_runs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    dataset_id INT NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP NULL,
    metrics JSON,
    FOREIGN KEY (model_id) REFERENCES models(id),
    FOREIGN KEY (dataset_id) REFERENCES datasets(id)
);
