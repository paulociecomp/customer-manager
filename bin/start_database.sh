#!/usr/bin/env bash
set +e
EXEC_OPTION=$1
ENV_OPTION=$2
SCRIPT_DIR=$(dirname $0)
SOURCE_DIR=$(pwd)

set -euo pipefail
IFS=$'\n\t'

IMAGE_DB_NAME=postgres-customer-manager
CONTAINER_DB_NAME=postgres-customer-manager-container
GRADLE_DB_SERVER=local

stop_container() {
  if [[ -n $(docker ps -q -f name=$CONTAINER_DB_NAME) ]]; then
    echo "Stopping container ${CONTAINER_DB_NAME}"
    docker stop $(docker ps -q -f name=$CONTAINER_DB_NAME)
  fi
}

remove_container() {
  if [[ -n $(docker ps -q -a -f name=$CONTAINER_DB_NAME) ]]; then
    echo "Removing container ${CONTAINER_DB_NAME}"
    docker rm $(docker ps -q -a -f name=$CONTAINER_DB_NAME)
  fi
}

remove_image() {
  if [[ -n $(docker  images -q $IMAGE_DB_NAME) ]]; then
    echo "Removing image ${IMAGE_DB_NAME}"
    docker rmi -f $(docker  images -q $IMAGE_DB_NAME)
  fi
}

build_image() {
  echo "Building image ${IMAGE_DB_NAME}"
  docker build --no-cache -t $IMAGE_DB_NAME .
}

start_container() {
  echo "Starting container ${CONTAINER_DB_NAME}"
  docker run --name=$CONTAINER_DB_NAME --restart=unless-stopped -p 5439:5432 -d $IMAGE_DB_NAME
}

build_image_process() {
  cd $SCRIPT_DIR
  stop_container
  remove_container
  remove_image
  build_image
  start_container
}

recreate_container_process() {
  stop_container
  remove_container
  start_container
}

run() {
  if [[ $EXEC_OPTION == "build_image" ]]; then
    build_image_process
  elif [[ $EXEC_OPTION == "recreate" ]]; then
    recreate_container_process
  elif [[ -z $EXEC_OPTION ]]; then
    build_image_process
  fi
}

run




