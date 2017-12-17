class Recordings:
    def __init__(self, recording, profile):
        self.recording = recording
        self.getRequest = recording.create_type('GetRecordingConfiguration')
        self.setRequest = recording.create_type('SetVideoEncoderConfiguration')
        self.getRequest.RecordingToken = profile.<<<>>>.token #not valid
        self.setRequest.Configuration = media.GetRecordingConfiguration(self.getRequest)

    def __applySettings(self):
        self.setRequest.ForcePersistence = True
        return self.recording.RECORGING_FUNC(self.setRequest)