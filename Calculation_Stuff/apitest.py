import solarapi

req = solarapi.Request("equinox", 2026, 7, 9)

result = solarapi.handle_request(req)

print(result.response)
print(result.payload)
print(result.error)