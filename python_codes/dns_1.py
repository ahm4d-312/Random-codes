import dns.resolver as ds

target = input("enter the domain:")
types = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]

for i in types:
    try:
        response = ds.resolve(target, i, raise_on_no_answer=False)
        if response.rrset:
            print(response.rrset)
    except Exception as e:
        print(f"Error: {e}")
