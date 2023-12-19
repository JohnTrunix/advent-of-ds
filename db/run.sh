# stop and remove container
docker stop aods-database
docker rm aods-database

# build and run container
docker build -t pg-database .
docker run -p 5432:5432 --name aods-database -d pg-database