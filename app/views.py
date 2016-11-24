#coding: utf-8
from flask import render_template
from app import app

from .models import TrainStation
from .form import AddressForm

import api_services

@app.route('/', methods=['GET', 'POST'])

def index():
	form = AddressForm()
	if form.validate_on_submit():
		address=form.address.data.encode("utf-8")
		station = api_services.get_nearest_train_station(address)
		print "Station in views have been initialize"

		if isinstance(station, str):
			error = station
			return render_template('index.html', title='Nearest station', form=form, address=address, station=None, error=error)
		else:
			return render_template('index.html', title='Nearest station', form=form, address=address.decode("utf-8"), station=station, error="")
	return render_template('index.html', title='Nearest station', form=form, address="", station="", error="")
