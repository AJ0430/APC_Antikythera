import solarapi

request = solarapi.Request("moon", 2026, 7, 16)
reply = solarapi.handle_request(request)
print(reply.payload)
print(reply.response)
print(reply.error)

request = solarapi.Request("jmoons", 2026, 7, 16)
reply = solarapi.handle_request(request)
print(reply.payload)
print(reply.response)
print(reply.error)

request = solarapi.Request("planets", 2026, 7, 16)
reply = solarapi.handle_request(request)
print(reply.payload)
print(reply.response)
print(reply.error)