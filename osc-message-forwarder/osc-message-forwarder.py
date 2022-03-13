from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

dispatcher = Dispatcher()

# ExampleClient = udp_client.SimpleUDPClient("127.0.0.1",####)
BuzzerClient = udp_client.SimpleUDPClient("127.0.0.1",9003)
FaceClient = udp_client.SimpleUDPClient("127.0.0.1",9004)   
SpartanClient = udp_client.SimpleUDPClient("127.0.0.1",9005)
HapticClient = udp_client.SimpleUDPClient("127.0.0.1",9006)


def send_handler(address, args):
# ExampleClient.send_message(f"{address}", args)        
    BuzzerClient.send_message(f"{address}", args)
    FaceClient.send_message(f"{address}", args)
    SpartanClient.send_message(f"{address}", args)
    HapticClient.send_message(f"{address}", args)

    # print(f"{address}: {args}")

dispatcher.map("*", send_handler)
server = BlockingOSCUDPServer(("127.0.0.1", 9001), dispatcher)
server.serve_forever()