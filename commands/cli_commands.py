import click


@click.pass_context
def move(ctx):
    click.echo("Shift transformation:")

    x = click.prompt('x-axis shift value', type=float)
    y = click.prompt('y-axis shift value', type=float)
    z = click.prompt('z-axis shift value', type=float)

    ctx.obj["exec"].append({"type": "move", "coords": (x, y, z)})


@click.pass_context
def rotate(ctx):
    click.echo("Rotate transformation:")

    deg_rad = click.prompt('Value type', type=click.Choice(["Degree", "Radian"]))
    x = click.prompt('x-axis rotation angle', type=int)
    y = click.prompt('y-axis rotation angle', type=int)
    z = click.prompt('z-axis rotation angle', type=int)

    ctx.obj["exec"].append({"type": "rotate", "mode": deg_rad, "coords": (x, y, z)})


@click.pass_context
def cut(ctx):
    click.echo("Cut operation:")

    num = click.prompt("Number of operations", type=int)

    corners = []

    for i in range(num):
        corners.append(click.prompt("Choose a corner to cut",
                                    type=click.Choice(["up-left", "up-right", "down-left", "down-right"])))

    ctx.obj["exec"].append({"type": "cut", "corners": corners})


@click.pass_context
def patch(ctx):
    click.echo("Patch operation:")

    degree = click.prompt("Degree of interpolation", type=int)

    ctx.obj["exec"].append({"type": "patch", "degree": degree})


@click.pass_context
def remove(ctx):
    click.echo("Removal operation:")

    height = click.prompt("height value", type=float)

    above_below = click.prompt("Remove all points above or below the given height",
                               type=click.Choice(["Above", "Below"]))

    ctx.obj["exec"].append({"type": "remove", "height": height, "mode": above_below})


@click.pass_context
def mount(ctx):
    click.echo("Mount operation")

    path = click.prompt("Path to GeoTIFF picture to mount", type=click.Path(exists=True))

    ctx.obj["exec"].append({"type": "mount", "path": path})


operations = {"move": move,
              "rotate": rotate,
              "cut": cut,
              "patch": patch,
              "remove": remove,
              "mount": mount}