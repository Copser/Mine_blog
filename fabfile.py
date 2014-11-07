from fabric.api import local

def deploy():
	"""
	Deploy the latest changes to Heroku
	"""
	# Push changes to master
	local("git push origin master")

	# Push changes to Heroku
	local("git push heroku master")

	# Run migrations on Heroku
	local("heroku run python manage.py migrate")