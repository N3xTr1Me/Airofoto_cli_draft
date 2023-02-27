import click

from commands import operations


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


