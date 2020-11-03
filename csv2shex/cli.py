"""DC Application Profile (DCAP) from CSV to ShEx"""

import ruamel.yaml as yaml
import click
from .config import CSV_ELEMENTS
from .csvreader import csvreader
from .csvrows import list_csvrowobjs
from .csvshapes import pprint_schema, list_csvshapeobjs

# pylint: disable=unused-argument,no-value-for-parameter
# => unused-argument: Allows placeholders for now.
# => no-value-for-parameter: Okay in cli.py


@click.group()
@click.version_option("0.2.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(context):
    """DC Application Profile (DCAP) from CSV to ShEx"""


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.option("--verbose", is_flag=True)
@click.help_option(help="Show help and exit")
@click.pass_context
def inspect(context, csvfile, verbose):
    """Inspect CSV file contents, normalized"""
    csvrowobjs_list = list_csvrowobjs(csvreader(csvfile))
    shapes_list = list_csvshapeobjs(csvrowobjs_list)
    pprint_output = pprint_schema(shapes_list)
    for line in pprint_output:
        print(line)


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def model(context):
    """Show DCAP model built-ins for ready reference"""

    csv_elements = yaml.safe_load(CSV_ELEMENTS)
    print("DCAP")
    for element_group in ["shape_elements", "statement_elements"]:
        print(f"    {element_group}:")
        for element in csv_elements[element_group]:
            print(f"        {element}")
