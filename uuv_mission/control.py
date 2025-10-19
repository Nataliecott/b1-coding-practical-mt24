class PDcontroller:
    def_init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0
    
    def compute_action(self, reference: float, observation: float) -> float:
        error = reference - observation
        control = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return control