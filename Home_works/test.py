import dns.resolver

response = dns.resolver.resolve("www.google.com", "A", raise_on_no_answer=False)

for i in response:
    print(f"host--> {i.to_text()}")
print(response)
