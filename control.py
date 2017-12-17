from onvif import ONVIFCamera
from time import sleep
from audioVideoConfigurations import AudioConfigurations
from imaging import Imaging

camera = ONVIFCamera('192.168.13.51', 80, 'admin', 'Supervisor', 'C:/Python36/Lib/site-packages/wsdl', no_cache=False)




# imaging = camera.create_imaging_service()
# 
# device = camera.create_devicemgmt_service()
# print(device.GetDeviceInformation())

media = camera.create_media_service()
profile = media.GetProfiles()[0]

# img = Imaging(imaging, profile)
# img.setFocus('Manual')

# recording = camera.create_recording_service()

# print(recording.GetRecordings())

# print(device.GetServices({'IncludeCapability': True}))

# request = imaging.create_type('GetImagingSettings')
# request.VideoSourceToken = profile.VideoSourceConfiguration.SourceToken

# request.ProfileToken = profile.token #add token

# print(imaging.GetImagingSettings(request))

ims = AudioConfigurations(media, profile)
print(ims.encoding("AAC"))

# request = media.create_type('GetVideoEncoderConfiguration')
# request.ConfigurationToken = profile.VideoEncoderConfiguration.token
# print(request)
# print(media.GetVideoEncoderConfiguration(request))
# print(profile)
# print(profile)