import click
from rich import print as rprint

from pydragonfly import DragonflyException, TParams
from .._utils import (
    ClickContext,
    json_flag_option,
    add_options,
)
from ._renderables import _display_all_rule


@click.group("rule")
def rule():
    """
    Rule Management\n
    >>> [API] https://dragonfly.certego.net/api/rule\n
    >>> [GUI] https://dragonfly.certego.net/dashboard/rules
    """


@rule.command("list", help="List all rules")
@add_options(json_flag_option)
@click.pass_context
def rule_list(ctx: ClickContext, as_json: bool):
    ctx.obj._logger.info("Requesting list of rules..")
    params = TParams(ordering=["-created_at"])
    try:
        response = ctx.obj.Rule.list(params=params)
        if as_json:
            rprint(response.data)
        else:
            _display_all_rule(response.data["results"])
        ctx.obj._logger.info(f"[+] GUI: {ctx.obj._server_url}/dashboard/rules")
    except DragonflyException as exc:
        ctx.obj._logger.fatal(str(exc))


@rule.command("retrieve", help="Retrieve rule object")
@click.argument("rule_id", type=int)
@click.pass_context
def rule_retrieve(ctx: ClickContext, rule_id: int):
    ctx.obj._logger.info(f"Requesting rule [underline blue]#{rule_id}[/]..")
    try:
        response = ctx.obj.Rule.retrieve(
            object_id=rule_id, params=TParams(expand=["user"])
        )
        rprint(response.data)
    except DragonflyException as exc:
        ctx.obj._logger.fatal(str(exc))
