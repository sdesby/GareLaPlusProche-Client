#coding: utf-8

class TrainStation:

	def initialize(self, m_id, name, howbig, latitude, longitude, postalCode, city, department, region):
		self.m_id=m_id
		self.prettyName=name
		self.howbig = howbig
		self.latitude=latitude
		self.longitude=longitude
		self.postal_code = postalCode
		self.city = city
		self.department = department
		self.region = region

	def _get_prettyName(self):
		return self.prettyName.decode("utf-8")

	def _set_prettyName(self, name):
		self.prettyName = name

	def _get_howbig(self):
		return self.howbig

	def _get_latitude(self):
		return self.latitude
	def _get_longitude(self):
		return self.longitude

	def _get_postal_code(self):
		return self.postal_code
	def _get_city(self):
		return self.city
	def _get_department(self):
		return self.department
	def _get_region(self):
		return self.region.decode("utf-8")
