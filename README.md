# 配置方法

## cpython运行方法及依赖：

```sh
sudo apt-get update
sudo apt-get install nginx -y
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
```

```sh
pip install gunicorn
pip install flask
pip install flask_cors
```

*注：在gunicorn中 -w是进程数，t是超时时间，b是绑定ip和端口，app是app名称（app不需要写扩展名）*

### http访问

```sh
gunicorn -w 4 -t 30 -b 0.0.0.0:3920 ling_blog_background:app
```

### https访问(需要域名及ssl证书，选择nginx那个下载就行)

```sh
gunicorn -w 4 -t 30 -b 0.0.0.0:3920 --certfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.pem --keyfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.key  ling_blog_background:app
```

### http访问(后台运行)

```sh
nohup gunicorn -w 4 -t 30 -b 0.0.0.0:3920 ling_blog_background:app > nohup.out & disown
```

### https访问(需要域名及ssl证书，选择nginx那个下载就行)(后台运行)

```sh
nohup gunicorn -w 4 -t 30 -b 0.0.0.0:3920 --certfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.pem --keyfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.key  ling_blog_background:app > nohup.out & disown
```

## pypy3运行方法及依赖(性能更好)：

```sh
sudo apt-get install nginx -y
sudo apt-get install pypy3 -y
sudo apt-get install python3-dev libpq-dev -y
sudo apt-get install pypy3-dev libpq-dev -y
sudo apt-get install libpq-dev postgresql-server-dev-all -y
```

```sh
pypy3 -m pip install psycopg2
pypy3 -m pip install flask
pypy3 -m pip install flask_cors
pypy3 -m pip install Flask-CORS
pypy3 -m pip install gunicorn
```

### http访问

```sh
pypy3 -m gunicorn -w 4 -t 30 -b 0.0.0.0:3920 ling_blog_background:app
```

### https访问(需要域名及ssl证书，选择nginx那个下载就行)

```sh
pypy3 -m gunicorn -w 4 -t 30 -b 0.0.0.0:3920 --certfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.pem --keyfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.key  ling_blog_background:app
```

### http访问(后台运行)

```sh
nohup pypy3 -m gunicorn -w 4 -t 30 -b 0.0.0.0:3920 ling_blog_background:app > nohup.out & disown
```

### https访问(需要域名及ssl证书，选择nginx那个下载就行)(后台运行)

```sh
nohup pypy3 -m gunicorn -w 4 -t 30 -b 0.0.0.0:3920 --certfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.pem --keyfile=/var/www/html/ling-root/ling-ssl/ling2023.xyz.key  ling_blog_background:app > nohup.out & disown
```
