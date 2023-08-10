"""SoloCampaign entry point"""
# CLI_Pages/__main__.py

from CLI_pages import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == '__main__':
    main()
