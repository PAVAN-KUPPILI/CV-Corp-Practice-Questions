def connect(host,port=3306,protocol="TCP"):
    print(host)
    print(port)
    print(protocol)
connect("local")
connect("local",5000)
connect("local",8000,"ip")