#include <iostream>
#include "lib/server/server.h"

int main() {
    Server httpServer(8080);
    httpServer.Start();
    return 0;
}