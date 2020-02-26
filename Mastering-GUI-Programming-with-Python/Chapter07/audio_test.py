from PySide2.QtCore import *
from PySide2.QtMultimedia import *

app = QCoreApplication([])

r = QAudioRecorder()

print('Inputs: ', r.audioInputs())
print('Codecs: ', r.supportedAudioCodecs())
print('Sample Rates: ', r.supportedAudioSampleRates())
print('Containers: ', r.supportedContainers())
