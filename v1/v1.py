import click

from commands import operations


'''
Ниже представлен первый прототип консольного интерфейса:

Основной идеей является требование от пользователя указания пути до исходных данных и указания одной или нескольких
типовых комманд по названиям. Опционально по ключу --dest пользователь может передать путь, по которому желает
сохранить результат работы программы.

Впоследствии задача по получению аргументов для указанных функций делегируется типовым командам, приведенным в файле
cli_commands.py в директории commands
'''


@click.command()
@click.pass_context
@click.argument("data", type=click.Path(exists=True))
@click.option("--dest", type=click.Path(), default='')
@click.argument("commands", nargs=-1, type=click.Choice(operations.keys()))
def CLI(ctx, data, dest, commands):
    ctx.ensure_object(dict)

    ctx.obj["src"] = data

    if dest:
        ctx.obj["dest"] = dest

    ctx.obj["exec"] = []

    for command in commands:
        operations[command]()
            

    click.echo(ctx.obj)


if __name__ == "__main__":
    CLI(obj={})


