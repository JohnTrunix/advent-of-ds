docker build -t pg-database .
docker run -p 5432:5432 --name aods-database -d pg-database