Is this code correct
#include <stdio.h>
#include <grp.h>
#include <unistd.h>

int main() {
    gid_t gid = getgid();
    struct group grp;
    char buffer[1024];
    struct group *result;

    // Using getgrgid_r to get group information
    if (getgrgid_r(gid, &grp, buffer, sizeof(buffer), &result) == 0 && result != NULL) {
        printf("Group Name: %s\n", grp.gr_name);
    } else {
        perror("getgrgid_r failed");
    }

    return 0;
}