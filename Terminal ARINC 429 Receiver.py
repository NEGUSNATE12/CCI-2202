# 
# #Terminal 01
# class cyse46
# ARINC 429 Receiver Simulation
# Listens for messages from various LRUs and prints them to the console
import can
import time

def arinc_receiver():
    # Connect to virtual CAN bus
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    print("ARINC 429 Receiver started...")
    print("Listening for LRU messages...")
    
    lru_names = {
        0x100: 'NAV', 0x200: 'ALT', 
        0x300: 'SPD', 0x400: 'HDG'
    }
    
    try:
        while True:
            message = bus.recv(timeout=1.0)
            if message is not None:
                lru_type = lru_names.get(message.arbitration_id & 0xF00, 'UNKNOWN')
                print(f"RX [{lru_type}]: ID=0x{message.arbitration_id:03X}, Data={[hex(x) for x in message.data]}")
                
    except KeyboardInterrupt:
        print("\nReceiver stopped")
    finally:
        bus.shutdown()

if __name__ == "__main__":
    arinc_receiver()