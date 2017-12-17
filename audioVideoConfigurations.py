class VideoConfigurations:
    def __init__(self, media, profile):
        self.media = media
        self.getRequest = media.create_type('GetVideoEncoderConfiguration')
        self.setRequest = media.create_type('SetVideoEncoderConfiguration')
        self.getRequest.ConfigurationToken = profile.VideoEncoderConfiguration.token
        self.setRequest.Configuration = media.GetVideoEncoderConfiguration(self.getRequest)

    def __applySettings(self):
        self.setRequest.ForcePersistence = True
        return self.media.SetVideoEncoderConfiguration(self.setRequest)
        
    def encoding(self, codec): #Баг: по эксепшену ошибка (JPEG), но функция работает.
        self.setRequest.Configuration.Encoding = codec
        return self.__applySettings()
    
    def bitrateLimit(self, bitrateLimit = 4096):
        self.setRequest.Configuration.RateControl.BitrateLimit = bitrateLimit
        return self.__applySettings()
    
    def frameRateLimit(self, frameRateLimit = 30):
        self.setRequest.Configuration.RateControl.FrameRateLimit = frameRateLimit
        return self.__applySettings()

    def H264(self, GovLength = 0, H264Profile = None):
        if GovLength != 0:
            self.setRequest.Configuration.H264.GovLength = GovLength
        if H264Profile is not None:
            self.setRequest.Configuration.H264.H264Profile = H264Profile
        return self.__applySettings()
    
    def resolution(self, Width = 1920, Height = 1080): #Нужно научиться получать ДОСТУПНЫЕ ВАРИАНТЫ
        self.setRequest.Configuration.Resolution.Width = Width
        self.setRequest.Configuration.Resolution.Height = Height
        return self.__applySettings()
    

class AudioConfigurations:
    def __init__(self, media, profile):
        self.media = media
        self.getRequest = media.create_type('GetAudioEncoderConfiguration')
        self.setRequest = media.create_type('SetAudioEncoderConfiguration')
        self.getRequest.ConfigurationToken = profile.AudioEncoderConfiguration.token
        self.setRequest.Configuration = media.GetAudioEncoderConfiguration(self.getRequest)
        
    def __applySettings(self):
        self.setRequest.ForcePersistence = True
        print(type(self.setRequest))
        return self.media.SetAudioEncoderConfiguration(self.setRequest)
    
    def encoding(self, audioCodec):
        self.setRequest.Configuration.Encoding = audioCodec
        return self.__applySettings()
    
    def bitrate(self, bitrate):
        self.setRequest.Configuration.Bitrate = bitrate
        return self.__applySettings()
    
    def sampleRate(self, sampleRate):
        self.setRequest.Configuration.SampleRate = sampleRate
        return self.__applySettings()