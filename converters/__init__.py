
def create_serializer(name):
    if name == 'json':
        print("JSON")
        return

    if name == 'pickle':
        print("PICKLE")
        return

    if name == 'toml':
        print("TOML")
        return

    if name == 'yaml':
        print("YAML")
        return

    print("HZ Language")
    exit(1)
