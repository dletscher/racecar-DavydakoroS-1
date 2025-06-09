import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']
        left_far, left_near, front, right_near, right_far = lidar



        left = (left_far + left_near) / 2
        right = (right_near + right_far) / 2
        width = left + right

        offset = (right - left) / max(width, 0.01)
        curve_signal = (right_far + right_near - left_far - left_near) / max(left_far + left_near + right_far + right_near, 0.01)

        steer = 3.0 * offset + 1.5 * curve_signal
        if steer > 0.05:
            steering = 'right'
        elif steer < -0.05:
            steering = 'left'
        else:
            steering = 'straight'

        base = 0.1 + 0.2 * min(front, width)

        cap= 0.18
        thresholds =[
            (4, 4, 0.3, 0.35),
            (5, 5, 0.25, 0.45),
            (6, 6, 0.20, 0.55),
            (8, 7, 0.15, 0.65),
            (10, 8, 0.10, 0.75),
        ]

        for front_threshold, width_threshold, offset_threshold, new_cap in thresholds:
            if front > front_threshold and width > width_threshold and abs(offset) < offset_threshold:
                cap = new_cap

        target = min(base, cap)

        if abs(curve_signal) > 0.3:
            target = min(target, 0.25)
        if front < 0.5:
            target = min(target, 0.15)
        if abs(offset) > 0.7 or front < 0.3:
            target = min(target, 0.1)


        if velocity < target - 0.05:
            action = 'accelerate'
        elif velocity > target + 0.05:
            action = 'brake'
        else:
            action = 'coast'

        return (steering, action)