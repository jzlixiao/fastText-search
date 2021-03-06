# -*- coding: utf-8 -*-
from flask import render_template
from app.model import fit_model_vector, sim_pid_model, sim_text_model
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fit", methods=['GET'])
def fit_data():
    return fit_model_vector.fit()


@app.route("/sim_by_pid", methods=['GET', 'POST'])
def sim_by_pid():
    return sim_pid_model.get_by_pid()


@app.route("/sim_by_text", methods=['GET', 'POST'])
def sim_by_text():
    return sim_text_model.get_by_text()
