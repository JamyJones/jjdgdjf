Am not understanding a thing here innthe text below , explain it waht it means 
```
The termux-packages git repo directory from which a container is created when run-docker.sh is first run is mounted at /home/builder/termux-packages inside the docker container as a docker volume. The original volume source mount path (termux-packages git repo directory) does not change for the life of the container. So if running run-docker.sh from a different termux-packages git repo directory (cwd), like of a fork, the original volume source mount path will be what is used for building instead of the current repo root/cwd and any changes in the later would not get used.

So each termux-packages git repo directory must have its own docker container to build packages. Multiple containers may also be needed if the docker image required for the current branch is newer or older than the branch with which container was created. The default or the first docker container is created with the name termux-package-builder. To create a new container for the current repo that can be used build its packages, export the $CONTAINER_NAME environment variable with a different name and run run-docker.sh again.

CONTAINER_NAME=termux-package-builder-fork ./scripts/run-docker.sh
List all docker containers created by running. The IMAGE column will show the image id for which the container was created for. The command will list non-Termux containers too.

docker container ls --all --size
List all docker image for Termux packages docker image by running.

docker image ls --all --filter "reference=ghcr.io/termux/package-builder"
Cus
```