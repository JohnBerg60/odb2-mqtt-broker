import sys

# info: https://python-obd.readthedocs.io/en/latest/
import obd

obd.logger.setLevel(obd.logging.DEBUG)

def openConnection(port):
    connection = obd.OBD('/dev/rfcomm1', baudrate=38400, protocol='6') 

    print (connection.status())

    print(connection.supported_commands)

    cmd = obd.commands.ELM_VOLTAGE
    response = connection.query(cmd) 
    print(response.value) 

    cmd = obd.commands.AMBIANT_AIR_TEMP
    response = connection.query(cmd) 
    print(response.value)

    return connection 


#
#   Main program 
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', nargs='?', 
        help='the comm port to the bms (default: %(default)s)', default='/dev/rfcomm1')
    args = parser.parse_args()
    conn = openConnection(args.port)
    if not conn:
        print('cannot open serial port %s, terminating' % (args.port))
        exit(1)
