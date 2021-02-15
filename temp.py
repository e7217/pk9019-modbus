from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def processResponse(result):
    log.debug(result)

UNIT = 0x01

client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600)
# client = ModbusClient(port='/dev/ttyUSB0', stopbits=1, bytesize=8, baudrate=9600)
conn = client.close()
print(conn)
conn = client.connect()
print(conn)

# rr = client.read_coils(1, 5, unit=UNIT)
# rr = client.read_discrete_inputs(1, 10, unit=UNIT)
rr = client.read_holding_registers(0, 10, unit=UNIT)
# rr = client.read_input_registers(1, 10, unit=UNIT)
log.debug(rr.registers)
# rr.addCallback(processResponse)

print(rr)
client.close()