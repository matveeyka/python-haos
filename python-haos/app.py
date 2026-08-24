import eiscp

receiver = eiscp.eISCP('192.168.98.127')

try:
    receiver.command('volume 55')
    print("Check volume")
except Exception as error:
    print(f"Error: {error}")
