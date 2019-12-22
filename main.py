

class Simulation:
	def __init__(self, initial_alt, initial_speed, time_steps, mass, interval_update_rocket):
		self.initial_alt = initial_alt
		self.initial_speed = initial_speed
		self.time = 0
		self.time_steps = time_steps
		self.mass = mass

		self.alt = initial_alt
		self.speed = initial_speed

		self.max_alt = initial_alt
		self.rocket = None
		self.interval_update_rocket = interval_update_rocket

	def update(self, forces):
		
		self.resulting_force = 0
		for force in forces:
			self.resulting_force += force

		self.resulting_acc = self.resulting_force / self.mass
		self.speed += (self.resulting_acc*self.time_steps)
		self.alt += (self.speed*self.time_steps)

		self.time += self.time_steps

		if self.max_alt < self.alt:
			self.max_alt = self.alt

		if self.time % self.interval_update_rocket < self.time_steps:
			rocket.update()



class Sensor:
	def __init__(self, simulation):
		self.simulation = simulation
	
	def get_value(self):
		pass

	def __repr__(self):
		return "Default Sensor"


class Time_Sensor(Sensor):
	def get_value(self):
		return self.simulation.time

	def __repr__(self):
		return "Time : {}".format(self.simulation.time)


class Rocket:
	def __init__(self, simulation, sensor_time):
		self.simulation = simulation
		self.sensor_time = sensor_time
		self.sensors = [self.sensor_time]

	def show_status(self):
		for sensor in self.sensors:
			print(sensor)

	def update(self):
		print("Rocket update") 



s1 = Simulation(2, 244.4193118, 0.00001, 500, 0.0001)
time_sensor = Time_Sensor(s1)
rocket = Rocket(s1, time_sensor)
s1.rocket = rocket


while s1.alt >= 0:
	s1.update([-9.8*s1.mass])
	rocket.show_status()

print(f"max alt is {s1.max_alt}")