from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import sounddevice as sd
import soundfile as sf

dispatcherC = Dispatcher()
sd.default.samplerate = 44100
sd.default.device = ("creative bluetooth audio w2), Windows DirectSound")
    
#Left Buzz
LeftFile = 'leftbuzz.wav'
LeftData, Leftfs = sf.read(LeftFile, dtype='float32')
    
#Right Buzz
RightFile = 'rightbuzz.wav'
RightData, Rightfs = sf.read(RightFile, dtype='float32')
    
#BothBuzz
BothFile = 'centerbuzz.wav'
BothData, Bothfs = sf.read(BothFile, dtype='float32')   
    
#TailBuzz
TailFile = 'tailbuzz.wav'
TailData, Tailfs = sf.read(TailFile, dtype='float32') 
    
#IdleBuzz
IdleFile = 'keepalive.wav'
IdleData, Idlefs = sf.read(IdleFile, dtype='float32')   
sd.play(IdleData, Idlefs,loop=True)
    
def haptic_handler(*args: bool):
    #(location, trigger) = args
    if args == ("/avatar/parameters/HapticLeft", 1):
        sd.play(LeftData, Leftfs,loop=True)
        print("Touching Left")
    elif args == ("/avatar/parameters/HapticRight", 1):
        sd.play(RightData, Rightfs,loop=True)
        print("Touching Right")        
    elif args == ("/avatar/parameters/HapticBoth", 1):
        sd.play(BothData, Bothfs,loop=True)
        print("Touching Center")  
    elif args == ("/avatar/parameters/HapticTail", True):
        sd.play(TailData, Tailfs,loop=True)
        print(red("Tail pulled!"), ("It was probably Jones."))
    else:
        sd.play(IdleData, Idlefs,loop=True)
                        
dispatcherC.map("/avatar/parameters/Haptic*", haptic_handler)
server = BlockingOSCUDPServer(("127.0.0.1", 9006), dispatcherC)
server.serve_forever()