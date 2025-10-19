class PDcontroller:
    def __init__(self, kp: float = 0.18, kd: float = 0.75):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0
    
    def compute_action(self, reference: float, observation: float) -> float:
        error = reference - observation
        control = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return control