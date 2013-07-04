include_recipe "apt"
include_recipe "build-essential"
include_recipe "postgresql::server"

%w{postgresql git-core build-essential tree python ipython
   python-psycopg2 python-setuptools python-pip}.each do
|pkg|
  package pkg do
    action :install
  end
end

#
# Installing redis
#
bash "Installing redis..." do
    code <<-EOH
    cd /tmp
    mkdir redis && cd redis
    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make
    sudo make install
    EOH
end

#
# Installing python packages from pip
#
bash "Installing packages from requirements.txt with pip..." do
    code <<-EOH
    sudo pip install -r /home/vagrant/django_site/requirements.txt
    EOH
end

