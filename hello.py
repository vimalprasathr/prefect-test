from prefect import flow

@flow
def hello(name="World"):
    print(f"Hello {name}!")

hello("Vimal Prasath")
