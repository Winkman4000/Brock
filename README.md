# Brock

## Database Example

This repository includes a `weights_database.sql` script that defines a simple
schema for storing datasets, models, layers, and weights used when training a
neural network. Import it into your SQL server to experiment with managing your
own neural-network data.

## Backend Server

A small Flask backend is provided in the `backend/` directory. Install
requirements and run `backend/run.py` to start a REST API for interacting with
these tables:

```bash
pip install -r requirements.txt
python backend/run.py
```

The API exposes basic endpoints under `/api` for datasets, models, and training
runs.
