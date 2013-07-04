include_recipe "apt"
include_recipe "build-essential"
include_recipe "postgresql::server"

%w{postgresql git-core build-essential tree python ipython
   python-psycopg2 python-setuptools python-pip gettext redis-server}.each do
|pkg|
  package pkg do
    action :install
  end
end

#
# Installing python packages from pip
#
bash "Installing packages from requirements.txt with pip..." do
    code <<-EOH
    sudo pip install -r /home/vagrant/django_site/requirements.txt
    EOH
end

