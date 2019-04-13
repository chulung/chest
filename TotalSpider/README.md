
brew install python3
brew install mysql-connector-c
edit mysql_config (locate it: which mysql_config)
correct this in mysql_config:

# Create options 
libs="-L$pkglibdir"
libs="$libs -l "
It shoud be:

# Create options 
libs="-L$pkglibdir"
libs="$libs -lmysqlclient -lssl -lcrypto"

pip3 install mysqlclient
pip3  install scrapy
pip3 install pandas 