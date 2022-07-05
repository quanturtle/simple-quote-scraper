# Simple scraper using requests and docker

Add `credentials.cfg`
```
DATABASE_URI = 'postgres://<username>:<password>@<ip_addr>:5432/<database_name>
```

Build image
```
cd simple-quote-scraper
sudo docker build -t scraper .
```

Run container, you must have a `postgresql` database running on `localhost`
```
sudo docker run --net=host scraper
```
