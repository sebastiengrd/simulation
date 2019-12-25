import matplotlib.pyplot as plt

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

		self.speeds = []
		self.alts = []
		self.accs = []
		self.times = []

	def calcul_aero_force(self, c, p, u, a):
		return 0.5*p*(u**2)*c*a


	def run(self):
		self.count = 0

		while self.speed >= -5:
			self.update([-9.8*s1.mass, self.calcul_aero_force(0.04, 1.268, self.speed, 0.0707)*-1])
			if self.count%100000 == 0:
				rocket.show_status()
			self.count += 1

		print(f"max alt is {s1.max_alt} m and {s1.max_alt * 3.280839895} feets")
		self.show_graphs()

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

		self.alts.append(self.alt)
		self.speeds.append(self.speed)
		self.accs.append(self.resulting_acc)
		self.times.append(self.time)
 
	def show_graphs(self):
		fig, axs = plt.subplots(3, sharex=True, sharey=False)
		fig.suptitle('Rocket Status')
		axs[0].set_title('Altitude (m)')
		axs[1].set_title('Speed (m/s)')
		axs[2].set_title('Acceleration (m/s^2)')
		axs[0].plot(self.times, self.alts)
		axs[1].plot(self.times, self.speeds)
		axs[2].plot(self.times, self.accs)

		axs[0].axhline(y=3048,linewidth=1, color='k')
		plt.subplots_adjust(top=0.88, bottom=0.11, left=0.11, right=0.9, hspace=0.6, wspace=0.2)
		plt.show()



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
		self.coeff_drag = 0.04
		self.coeff_drag_brakes = 0.1

	def show_status(self):
		print("----------------")
		for sensor in self.sensors:
			print(sensor)



	def update(self):
		pass
		



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