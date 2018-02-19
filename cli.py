import click
from uploader import Uploader

@click.command()
@click.option('--filename', help='a csv file to upload with header (name, description, quantity, price)')
def upload(filename):
    click.echo("Uploading {}...".format(filename))
    Uploader().read_products(filename)
    click.echo("Done!")

if __name__ == '__main__':
    upload()
