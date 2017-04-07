from flask_assets import Environment,Bundle
from .. import app

bundles = {

	'_css' : Bundle(
		'css/style.min.css',
		'css/material-design-kit.css',
		'css/sidebar-collapse.min.css',
		'404/css/font-awesome.min.css',
		output='gen/default.css'),

	'_js' : Bundle(
		'js/colors.js',
		'js/main.min.js',
		'js/jquery.min.js',
		'js/tether.min.js',
		'js/bootstrap.min.js',
		'js/dom-factory.js',
		'js/material-design-kit.js',
		'js/sidebar-collapse.js',
		'js/main.min.js',
		output='gen/default.js'),

	'404_css' : Bundle(
		'404/css/bootstrap.min.css',
		'404/css/font-awesome.min.css',
		'404/css/style.min.css',
		'404/css/vegas.min.css',
		output='gen/404default.css'),

	'404_js' : Bundle(
		'404/js/jquery-1.12.3.min.js',
		'404/js/bootstrap.min.js',
		'404/js/mozaic.js',
		output='gen/404default.js'),

	# '404_css' : Bundle(
	# 	'css/404/normalize.css',
	# 	'css/404/main.css',
	# 	'css/404/bootstrap.min.css',
	# 	'css/404/animate.min.css',
	# 	'css/404/font-awesome.min.css',
	# 	'css/404/style.css',
	# 	output='gen/404default.css'),

	# '404_js' : Bundle(
	# 	'js/404/modernizr-2.8.3.min.js',
	# 	'js/404/jquery-2.2.4.min.js',
	# 	'js/404/plugins.js',
	# 	'js/404/bootstrap.min.js',
	# 	'js/404/wow.min.js',
	# 	'js/404/main.js',
	# 	output='gen/404default.js'),
}

assets = Environment(app)
assets.register(bundles)