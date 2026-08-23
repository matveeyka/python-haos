try:
    import eiscp

    print("EISCP works!", flush=True)
    print(f"EISCP location: {eiscp.__file__}", flush=True)

except Exception as error:
    print(f"Something happened: {error}", flush=True)

