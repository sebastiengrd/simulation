import random


class Simulation:
	def __init__(self, initial_alt, initial_speed, time_steps, mass):
		self.initial_alt = initial_alt
		self.initial_speed = initial_speed
		self.time = 0
		self.time_steps = time_steps
		self.mass = mass

		self.alt = initial_alt
		self.speed = initial_speed

	def update(self, forces):
		
		self.resulting_force = 0
		for force in forces:
			self.resulting_force += force

		self.resulting_acc = self.resulting_force / self.mass
		self.speed += (self.resulting_acc*self.time_steps)
		self.alt += (self.speed*self.time_steps)

		self.time += self.time_steps



class Sensor:
	def __init__(self, simulation):
		self.simulation = simulation
	
	def get_value(self):
		pass


class Time_Sensor(Sensor):
	def get_value(self):
		return self.simulation.time


class Rocket:
	def __init__(self, simulation, sensor_time):
		self.simulation = simulation
		self.sensor_time = sensor_time
		self.sensors = [self.sensor_time]

	def show_status(self):
		for sensor in self.sensors:
			print(sensor.get_value())



s1 = Simulation(0, 9, 0.1, 1)
time_sensor = Time_Sensor(s1)
rocket = Rocket(s1, time_sensor)

while s1.alt >= 0:
	s1.update([-9.8])
	rocket.show_status()