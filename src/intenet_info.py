
import os
import file_reader
import data_classes

def get_net_info():
    try:
        data = []
        with open("/proc/net/dev", 'r') as file:
            file.readline()
            file.readline()# Throwaway useless lines LOL
            while True:
                
                line = file.readline()
                
                if not line:  # Check if the line is empty, indicating end of file
                    break

                line = line.strip()
                name, _, line = line.partition(':')
                numbers = file_reader.get_numbers_list(line)
                
                # Fill dataclass

                if "lo" in name:
                    name = "Local internet traffic"
                elif "enp" in name:
                    name = "Ethernet connection traffic"
                elif "enx" in name:
                    name = "Ethernet connection via USB adapter"
                elif "wl" in name:
                    name = "Wireless connection"
                #print(name)
                data.append(data_classes.InternetInfo(name, numbers[0], numbers[1], numbers[2], numbers[3], numbers[8], numbers[9], numbers[10], numbers[11]))
            
            return data

    except FileNotFoundError:
        print(f"Error: The file for internet was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

if __name__ == "__main__":
    print(get_net_info())