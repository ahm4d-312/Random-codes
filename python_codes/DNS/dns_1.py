import dns.resolver as ds

response = ds.resolve("www.facebook.com", "A", raise_on_no_answer=False)
for i in response:
    print(f"host--> {i.to_text()}")
print(response.port)
