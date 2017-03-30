from flask_assets import Environment,Bundle
from .. import app

bundles = {

	'_css' : Bundle(
		'css/style.min.css',
		'vendor/material-design-kit.css',
		'vendor/sidebar-collapse.min.css',
		output='gen/default.css'),

	'_js' : Bundle(
		'js/color.js',
		'js/main.min.js',
		output='gen/default.js')
}

assets = Environment(app)
assets.register(bundles)