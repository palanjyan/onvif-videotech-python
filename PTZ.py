from time import sleep
from copy import copy


class PTZ:
    def __init__(self, ptz, profile):
        self.ptz = ptz
        self.profile = copy(profile)
        self.profile.PTZConfiguration.DefaultPTZSpeed.Zoom.x = 0.0
        self.request = ptz.create_type('ContinuousMove')
        self.request.ProfileToken = profile.token #add token
    
    def perform_move(self):
        sleep(1)
        self.request.Velocity = self.profile.PTZConfiguration.DefaultPTZSpeed
        self.ptz.ContinuousMove(self.request)
        sleep(0.5)
        self.ptz.Stop({'ProfileToken': self.request.ProfileToken})
    
    def moveRight(self):
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.x = 1.0
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.y = 0.0
        self.perform_move()
    
    def moveLeft(self):
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.x = -1.0
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.y = 0.0
        self.perform_move()
    
    def moveDown(self):
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.x = 0.0
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.y = -1.0
        self.perform_move()
    
    def moveUp(self):
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.x = 0.0
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.y = 1.0
        self.perform_move()
    
    def zoom(self, zoom):
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.x = 0.0
        self.profile.PTZConfiguration.DefaultPTZSpeed.PanTilt.y = 0.0
        self.profile.PTZConfiguration.DefaultPTZSpeed.Zoom.x = zoom
        self.perform_move()
