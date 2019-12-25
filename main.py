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

	def run(self):
		self.count = 0

		while self.speed >= -5:
			self.update([-9.8*s1.mass])
			if self.count%100000 == 0:
				rocket.show_status()
			self.count += 1

		print(f"max alt is {s1.max_alt}")

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


class Accelerometer_Sensor(Sensor):
	def get_value(self):
		return self.simulation.resulting_acc

	def __repr__(self):
		return "Acc : {}".format(self.simulation.resulting_acc)

class Speed_Sensor(Sensor):
	def get_value(self):
		return self.simulation.speed

	def __repr__(self):
		return "Speed : {}".format(self.simulation.speed)

class Alt_Sensor(Sensor):
	def get_value(self):
		return self.simulation.alt

	def __repr__(self):
		return "Alt : {}".format(self.simulation.alt)

class Rocket:
	def __init__(self, simulation, time_sensor, acc_sensor, speed_sensor, alt_sensor):
		self.simulation = simulation
		self.time_sensor = time_sensor
		self.acc_sensor = acc_sensor
		self.speed_sensor = speed_sensor
		self.alt_sensor = alt_sensor
		self.sensors = [self.time_sensor, self.acc_sensor, self.speed_sensor, self.alt_sensor]

	def show_status(self):
		print("----------------")
		for sensor in self.sensors:
			print(sensor)

	def update(self):
		pass
		# print("Rocket update") 



if __name__ == '__main__':
	# goal is 3048m
	s1 = Simulation(2, 244.4193118, 0.00001, 500, 0.0001)
	time_sensor = Time_Sensor(s1)
	acc_sensor = Accelerometer_Sensor(s1)
	speed_sensor = Speed_Sensor(s1)
	alt_sensor = Alt_Sensor(s1)
	rocket = Rocket(s1, time_sensor, acc_sensor, speed_sensor, alt_sensor)
	s1.rocket = rocket


	s1.run()