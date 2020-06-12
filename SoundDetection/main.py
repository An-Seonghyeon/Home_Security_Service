import json
import http.client
from _util import get_sensor
import urllib.request
from alarm import send_mail
import math
import scipy.io.wavfile
from scipy.fftpack import fft, fftfreq
import numpy as np
import struct
import time

framerate = 8000
time_streaming = 5
stream_length = time_streaming * 4
nframes = int(stream_length * framerate / 4)
file_location = "/home/pi/SoundDetection/recordings.wav" #file path or name where you would save the sound recording in wav file

# Configuration section for uBEAC setting
UBEAC_URL = 'simonan.hub.ubeac.io' #uBeac URL
GATEWAY_URL = '/SoundDetector' #gateway URL
DEVICE_FRIENDLY_NAME = 'Sound Detector' #device name

with urllib.request.urlopen('http://192.168.0.15:8080/') as r: #update IP address from LANmic mobile application
    audio_start = r.read(44)
    while True:
        audio_add = r.read(framerate)
        for i in range(stream_length-1):
            audio_add += r.read(framerate)

        format_float = '<' + str(nframes) + 'i'
        testResult = struct.unpack(format_float, audio_add)

        nb = np.array(testResult)
        nm = np.max(np.abs(nb))
        sigf32 = (nb/nm).astype(np.float32)
        scipy.io.wavfile.write(file_location, framerate, sigf32)
        rate, data = scipy.io.wavfile.read(file_location)

        rms_amp = np.sqrt(np.mean(np.square(data)))
        logrms_amp = abs(round(20 * math.log10(rms_amp)))

        Amplitude = get_sensor("Average Amplitude", {"Amplitude": str(logrms_amp)})

        freqs = fftfreq(data.shape[0], 1/rate)
        freqspos = freqs[:int(freqs.size/2)]
        datafft = fft(data)
        fftabs = abs(datafft)[:int(freqs.size/2)]

        peakfreq = np.max(fftabs)
        locmaxfreq = np.argmax(fftabs)
        freqmax = round(freqspos[locmaxfreq])

        Frequency = get_sensor("Frequency", {"Max Frequency" : str(freqmax)})
        Peak = get_sensor("Max Peak", {"Amplitude" : str(locmaxfreq)})

        sensors = []
        sensors.append(Amplitude)
        sensors.append(Frequency)
        sensors.append(Peak)

        device = [{
            'id': "Android Microphone",
            'sensors': sensors
        }]

        connection = http.client.HTTPSConnection(UBEAC_URL)
        connection.request('POST', GATEWAY_URL, json.dumps(device))
        response = connection.getresponse()
        print(response.read().decode())
        
        if logrms_amp > 40:
            send_mail()

