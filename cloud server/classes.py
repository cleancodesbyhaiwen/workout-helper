class Sensor:
    def __init__(self):
        self.yaw, self.pitch, self.roll = 0,0,0 # ORIENTATION
        self.last_distance = 0
        self.distance = 0
    def update(self,data):
        self.yaw = float(data['yaw']) if abs(float(data['yaw'])) > 1 else 0
        self.pitch = float(data['pitch']) if abs(float(data['pitch'])) > 1 else 0
        self.roll = float(data['roll']) if abs(float(data['roll'])) > 1 else 0
        self.last_distance = self.distance
        self.distance = int(data['distance'])

    def print_data(self):
        print('yaw:{:.1f}, pitch:{:.1f}, roll:{:.1f}, distance{:.1f}'
        .format(self.yaw,self.pitch,self.roll,self.distance))     


class Barbell:
    def __init__(self):
        self.unbalanced = False
        self.hitting = False
        self.same_distance_counter = 0
        self.hit_check = False
    def hit_detect(self,user,sensor):
        if user.exercise == 'bench press':
            if not self.hitting and sensor.distance > user.bench_press_distance:
                self.hitting = True
                user.rep_count += 1
                self.hit_check = True
                self.hitting = True
            elif self.hitting and sensor.distance < user.bench_press_distance:
                self.hitting = False
            elif self.hitting and sensor.distance > user.bench_press_distance: 
                self.hit_check = False
        elif user.exercise == 'squat':
            if not self.hitting and sensor.distance < user.squat_distance:
                self.hitting = True
                user.rep_count += 1
                self.hit_check = True
                self.hitting = True
            elif self.hitting and sensor.distance > user.squat_distance:
                self.hitting = False
            elif self.hitting and sensor.distance < user.squat_distance: 
                self.hit_check = False       


class User:
    def __init__(self):
        self.resting = False
        self.exercise = ''
        self.set_count = 0
        self.rep_count = 0
        self.height = 0
        self.arm_length = 0
        self.rest_counter = 0
        self.bench_press_distance = 15
        self.squat_distance = 5
        self.alarming = False
        self.rest_time = 200
    
    def rest_detect(self, sensor):
        print(self.rest_counter)
        if sensor.distance == sensor.last_distance:
            self.rest_counter += 1
        else:
            self.rest_counter = 0
            self.resting = False
            self.alarming = False
        if self.rest_counter >= 50 and self.alarming == False:
            if self.rep_count >= 6 and self.resting == False:
                self.set_count += 1
                self.rep_count = 0
            self.resting = True

        if self.rest_counter >= self.rest_time:
            self.resting = False
            self.alarming = True
    def change_exercise(self, input_exercise):
        if self.exercise != input_exercise:
            self.set_count = 0
            self.rep_count = 0
            self.exercise = input_exercise
            self.resting = False
            self.alarming = False
            self.rest_counter = 0
