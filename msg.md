How Can i use docker exec pid instead of it's filepath here:
docker exec --env "DOCKER_EXEC_PID_FILE_PATH=$DOCKER_EXEC_PID_FILE_PATH" --interactive  $CONTAINER_NAME "$@"