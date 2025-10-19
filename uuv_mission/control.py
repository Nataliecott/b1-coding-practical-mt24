import numpy as np

class PDcontroller:
    def __init__(self, kp: float = 0.1, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = None

    def compute_action(self, reference, observation):
        # support scalars and vectors
        ref = np.asarray(reference, dtype=float)
        obs = np.asarray(observation, dtype=float)
        if self.prev_error is None or self.prev_error.shape != ref.shape:
            self.prev_error = np.zeros_like(ref)

        error = ref - obs
        control = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        # return scalar for scalar inputs, otherwise numpy array
        return float(control) if control.size == 1 else control