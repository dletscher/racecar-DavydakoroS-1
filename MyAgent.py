import random

class Agent:
        def chooseAction(self, observations, possibleActions):

                lidar = observations['lidar']
                velocity = observations['velocity']


                left_avg = (lidar[0] + lidar[1]) / 2
                right_avg = (lidar[3] + lidar[4]) / 2
                center = lidar[2]

                if left_avg < right_avg - 0.1:
                        steering = 'right'
                elif right_avg < left_avg - 0.1:
                        steering = 'left'
                else:
                        steering = 'straight'

                if center < 0.6:
                        action = 'brake'
                elif velocity < 0.27:
                        action = 'accelerate'
                else:
                        action = 'coast'

                return (steering, action)