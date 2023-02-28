import click


'''
В данной версии типовые команды были изменены для более удобного и масштабируемого сохранения результатов своей работы
в context. 

Функционал сохранения был вынесен в отдельную функцию, теперь команды не требуют декоратора click.pass_context
'''


@click.pass_context
def save(ctx, arguments):
    ctx.obj[ctx.obj["iteration"]] = arguments
    ctx.obj["saved"].append(ctx.obj["iteration"])
    ctx.obj["iteration"] += 1


def move():
    click.echo("Shift transformation:")

    x = click.prompt('x-axis shift value', type=float)
    y = click.prompt('y-axis shift value', type=float)
    z = click.prompt('z-axis shift value', type=float)

    save({"type": "move", "coords": [x, y, z]})


def rotate():
    click.echo("Rotate transformation:")

    deg_rad = click.prompt('Value type', type=click.Choice(["Degree", "Radian"]))
    x = click.prompt('x-axis rotation angle', type=int)
    y = click.prompt('y-axis rotation angle', type=int)
    z = click.prompt('z-axis rotation angle', type=int)

    save({"type": "rotate", "mode": deg_rad, "coords": [x, y, z]})


def cut():
    click.echo("Cut operation:")

    num = click.prompt("Number of operations", type=int)

    corners = []

    for i in range(num):
        corners.append(click.prompt("Choose a corner to cut",
                                    type=click.Choice(["up-left", "up-right", "down-left", "down-right"])))

    save({"type": "cut", "corners": corners})


def patch():
    click.echo("Patch operation:")

    degree = click.prompt("Degree of interpolation", type=int)

    save({"type": "patch", "degree": degree})


def remove():
    click.echo("Removal operation:")

    height = click.prompt("height value", type=float)

    above_below = click.prompt("Remove all points above or below the given height",
                               type=click.Choice(["Above", "Below"]))

    save({"type": "remove", "height": height, "mode": above_below})


def mount():
    click.echo("Mount operation")

    path = click.prompt("Path to GeoTIFF picture to mount", type=click.Path(exists=True))

    save({"type": "mount", "path": path})


operations = {"move": move,
              "rotate": rotate,
              "cut": cut,
              "patch": patch,
              "remove": remove,
              "mount": mount}
