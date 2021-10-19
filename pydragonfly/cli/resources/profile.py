import click
from rich import print as rprint

from pydragonfly import DragonflyException, TParams
from .._utils import (
    ClickContext,
    json_flag_option,
    add_options,
)
from ._renderables import _display_all_profile


@click.group("profile")
def profile():
    """
    Profile Management\n
    >>> [API] https://dragonfly.certego.net/api/profile\n
    >>> [GUI] https://dragonfly.certego.net/dashboard/profiles
    """


@profile.command("list", help="List all profiles")
@add_options(json_flag_option)
@click.pass_context
def profile_list(ctx: ClickContext, as_json: bool):
    ctx.obj._logger.info("Requesting list of profiles..")
    params = TParams(ordering=["-created_at"])
    try:
        response = ctx.obj.Profile.list(params=params)
        if as_json:
            rprint(response.data)
        else:
            _display_all_profile(response.data["results"])
        ctx.obj._logger.info(f"[+] GUI: {ctx.obj._server_url}/dashboard/profiles")
    except DragonflyException as exc:
        ctx.obj._logger.fatal(str(exc))


@profile.command("retrieve", help="Retrieve profile object")
@click.argument("profile_id", type=int)
@click.pass_context
def profile_retrieve(ctx: ClickContext, profile_id: int):
    ctx.obj._logger.info(f"Requesting profile [underline blue]#{profile_id}[/]..")
    try:
        response = ctx.obj.Profile.retrieve(
            object_id=profile_id, params=TParams(expand=["user"])
        )
        rprint(response.data)
    except DragonflyException as exc:
        ctx.obj._logger.fatal(str(exc))
