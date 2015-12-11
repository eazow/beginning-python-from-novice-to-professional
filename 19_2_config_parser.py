from ConfigParser import ConfigParser

CONFIG_FILE = "19_1_configure.txt"

config = ConfigParser()

config.read(CONFIG_FILE)

print config.get('messages', 'greeting')

radius = input(config.get('messages', 'question') + ' ')

print config.get('messages', 'result_message'),

print config.getfloat('numbers', 'pi') * radius**2
