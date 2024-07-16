import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def gpt(auth: bool = False):
    if auth:
        print("Authenticating to OpenAI..")
    else:
        print("test")


if __name__ == "__main__":
    app()
