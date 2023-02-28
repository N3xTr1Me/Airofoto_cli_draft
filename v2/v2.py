import click
import yaml

from new_commands import operations


'''
Была добавлена поддержка файла конфига, для удобства генерации типового конфиг файла на данный момент используется
приведенный ниже словарь args.

Логика CLI изменена для выделения дихотомии между обработкой аргументов напрямую из консоли и работой с файлом конфига.

Важно заметить, что независимо от выбранного пользователем способа взаимодействия с программой, файл конфига
будет создан.
'''


args = {"move": {"type": "move", "x": None, "y": None, "z": None},
                  "rotate": {"type": "rotate", "deg_rad": None, "x": None, "y": None, "z": None},
                  "cut": {"type": "cut", "num": None, "corners": []},
                  "patch": {"type": "patch", "degree": None},
                  "remove":{"type": "remove", "height": None, "above_below": None},
                  "mount": {"type": "mount", "path": None}
        }

default_config = ".\\config"

@click.group("CLI")
@click.pass_context
@click.argument("data", type=click.Path(exists=True))
@click.option("--dest", type=click.Path(), default='')
def cli(ctx, data, dest):
    ctx.ensure_object(dict)

    ctx.obj["src"] = data

    if dest:
        ctx.obj["dest"] = dest

    ctx.obj["iteration"] = 1
    ctx.obj["saved"] = []


@click.pass_context
def get_commands(ctx):
    num = click.prompt("Number of operations", type=int)

    ops = []

    for i in range(num):
        ops.append(click.prompt("Enter the desired operation", type=click.Choice(operations.keys())))

    ctx.obj["commands"] = ops

@cli.command("alter", short_help="Configure data transformation directly through console input")
@click.pass_context
def set_commands(ctx):
    get_commands()

    for command in ctx.obj["commands"]:
        operations[command]()

    dump_config()


@cli.command("config", short_help="Create a config file template or load an existing one")
@click.pass_context
@click.argument("mode", type=click.Choice(["create", "load"]))
def configure(ctx, mode: str):

    if mode not in ["create", "load"]:
        raise ValueError("Config mode not recognized!")

    ctx.obj["config_path"] = click.prompt("Config location", type=click.Path())

    get_commands()

    i = 0

    for command in ctx.obj["commands"]:
        i += 1

        ctx.obj[i] = args[command]
        ctx.obj["commands"][i - 1] = i

    dump_config()

@click.pass_context
def dump_config(ctx):
    ctx.obj.pop("iteration")

    if "saved" in ctx.obj:
        saved = ctx.obj.pop("saved")
    else:
        saved = []

    if "config_path" in ctx.obj:
        path = ctx.obj.pop("config_path")
    else:
        path = default_config

    for num in saved:
        ctx.obj["commands"][num - 1] =  num

    with open(path + "\\config.yml", "w+") as file:
        yaml.dump(ctx.obj, file)

def main():
    pass


if __name__ == "__main__":
    cli(obj={})
