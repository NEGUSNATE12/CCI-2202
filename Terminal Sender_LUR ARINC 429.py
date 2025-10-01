
#Terminal 01
# class cyse465
# ARINC 429 Transmitter Simulation over CAN Bus
# This script simulates an ARINC 429 transmitter by sending messages over a virtual CAN bus.
# Each message represents data from different LRUs (Line Replaceable Units) such as NAV, ALT, SPD, and HDG.
import can
import time
import struct

def arinc_transmitter():
    # Connect to virtual CAN bus
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    print("ARINC 429 Transmitter started...")
    
    # Simulate ARINC 429 data (simplified)
    lru_messages = {
        'NAV': 0x100,
        'ALT': 0x200, 
        'SPD': 0x300,
        'HDG': 0x400
    }
    
    count = 0
    try:
        while True:
            for lru, base_id in lru_messages.items():
                # Simulate ARINC 429-like data (32-bit words)
                arinc_data = [count % 256, (count + 1) % 256, (count + 2) % 256, (count + 3) % 256]
                
                message = can.Message(
                    arbitration_id=base_id + (count % 16),
                    data=arinc_data,
                    is_extended_id=False
                )
                
                bus.send(message)
                print(f"TX [{lru}]: ID=0x{message.arbitration_id:03X}, Data={[hex(x) for x in arinc_data]}")
                
                time.sleep(1)
            count += 1
            print("--- Cycle complete ---")
            
    except KeyboardInterrupt:
        print("\nTransmitter stopped")
    finally:
        bus.shutdown()

if __name__ == "__main__":
    arinc_transmitter()