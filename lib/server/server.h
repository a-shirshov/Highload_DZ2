#include <iostream>


class Server {
public:
    Server(uint16_t port);
    ~Server();
    void Start();

private:
    uint16_t _port;

    static void Serve(int *sockfd);
    static void *Handle(void *arg);
};