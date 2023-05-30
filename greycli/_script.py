import click
import os
import subprocess
import sys
import functools

run_cmd = functools.partial(subprocess.run, shell=True, capture_output=True, text=True)

to_print = """
    ____                 ____ _     ___ 
    / ___|_ __ ___ _   _ / ___| |   |_ _|
    | |  _| '__/ _ \ | | | |   | |    | | 
    | |_| | | |  __/ |_| | |___| |___ | | 
    \____|_|  \___|\__, |\____|_____|___|
                    |___/ 
"""

config_template = """
TOKEN={}
OWNER_IDS=[{}]
"""


@click.command()
@click.argument("name")
@click.option(
    "--force",
    is_flag=True,
    help="Clear the directory and make the project",
    default=False,
)
def main(name, force):
    if os.path.isdir(name) and not force:
        click.echo("That folder already exists if you want to delete its contents do the command with the --force flag")
        return
    if os.path.isdir(name) and force:
        run_cmd(f"rm -rf {name}")
    click.echo(to_print, color="cyan")
    token = input("Token:")
    user_id = input("\nYour discord user ID:")
    if sys.platform not in ("win32", "cygwin", "cli"):
        run_cmd(
            f"git clone https://github.com/Sengolda/greybot.git && mv greybot {name}"
        )
        run_cmd(f"cd {name} && rm -f config.py.example")
        config = config_template.format(token, user_id)
        run_cmd(f"touch {name}/config.py")
        with open(f"{name}/config.py", "w") as f:
            f.write(config)

        click.echo("[+] Added env file.")
        click.echo(
            f"[+] Success, your template is ready\nto start it just do `cd {name} && pip install -Ur requirements.txt && python3 launch.py`",
        )
    else:
        print("Sorry, your system is not supported by GreyCLI.")


if __name__ == "__main__":
    main()
