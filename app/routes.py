from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

BREWERIES = [
    {
        'name': 'Sunset Brewing Co.',
        'city': 'Austin',
        'state': 'Texas',
        'style': 'IPA'
    },
    {
        'name': 'North Ridge Brewery',
        'city': 'Denver',
        'state': 'Colorado',
        'style': 'Stout'
    },
    {
        'name': 'Harbor Lights Brew',
        'city': 'Seattle',
        'state': 'Washington',
        'style': 'Pilsner'
    }
]


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('index.html', breweries=BREWERIES)


@bp.route('/breweries')
def breweries():
    return "<p>Welcome to Breweries!</p>"


@bp.route('/beer')
def beer_():
    return "<p>Welcome to beer types!</p>"


@bp.route('/about')
def about():
    return "<p>welcome to about us</p>"
