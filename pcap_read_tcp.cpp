#include<arpa/inet.h>
#include<net/ethernet.h>
#include<netinet/ip.h>
#include<cstdio>
#include<iostream>
#include<cstring>
#include<pcap.h>
#include<netinet/tcp.h>

using namespace std;

void dump_pkt(const u_char *pkt_data, struct pcap_pkthdr* header);

void usage()
{
    printf("syntax : pcap-test <interface>\n");
    printf("sample : pcap-test wlan0\n");
}

int main(int argc,char * argv[]){
    if(argc!=2){
        usage();
        return -1;
    }

    char * dev= argv[1];
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t * handle =pcap_open_live(dev, BUFSIZ, 1,1000,errbuf); //packet descriptor
    
    if(handle==nullptr){
        fprintf(stderr, "pcap_open_live(%s) return nullptr - $s\n",dev,errbuf);
    }
    
    while(true){
        struct pcap_pkthdr* header; //pkt+hdr=packet+header
        const u_char * packet;
        int res = pcap_next_ex(handle, &header, &packet); //res : return ; &packet :packet data
        if (res ==0) continue;
        if (res==-1 | res ==-2){
            printf("pcap_next_ex return %d(%s)\n",res, pcap_geterr(handle));
        }
        dump_pkt(packet,header);
    }
    pcap_close(handle);
}

void dump_pkt(const u_char *pkt_data, struct pcap_pkthdr* header){
    struct ether_header * eth_hdr=(struct ether_header *)pkt_data;

    u_int16_t eth_type=ntohs(eth_hdr->ether_type);   // ntohs : sort byte

    //if type is not IP, return function
    if(eth_type!=ETHERTYPE_IP) return;

    struct ip * ip_hdr=(struct ip*)(pkt_data+sizeof(ether_header));

    
   //if type is not TCP , return function
    if(ip_hdr->ip_p!=6) return;
    
    //size !!!!
    u_short ip_length= ip_hdr-> ip_len;
    struct tcphdr * tcp_hdr=(struct tcphdr*)(pkt_data+sizeof(ether_header)+ntohs(ip_length)/2);  

    u_int8_t ip_type=ip_hdr->ip_p;
    u_int8_t ip_offset=ip_hdr->ip_hl;

    printf("\nPacket Info=======================\n");
        // printf("sizeof(ether_header): %d\n",sizeof(ether_header));
        //printf("sizeof(ip_hdr): %d\n",sizeof(ip_hdr));
        //printf("ip_length : %d\n",ntohs(ip_length)/2);
        //if type is not TCP , return function
        //printf("ip type : %x\n",ip_hdr->ip_p);
    
    //print pkt length
    printf("%u bytes captured\n", header->caplen);

    //print mac addrl
    u_int8_t *dst_mac=eth_hdr ->ether_dhost;
    u_int8_t * src_mac=eth_hdr->ether_shost;

    printf("Dst MAC : %0x:%0x:%0x:%0x:%0x:%0x\n",
        dst_mac[0], dst_mac[1],dst_mac[2],dst_mac[3],dst_mac[4],dst_mac[5]);
    printf("Src MAC : %0x:%0x:%0x:%0x:%0x:%0x\n",
        src_mac[0], src_mac[1],src_mac[2],src_mac[3],src_mac[4],src_mac[5]); 

    //print ip addr
    char src_ip[16],dst_ip[16];
    char *tmp = inet_ntoa(ip_hdr -> ip_src);
    strcpy(src_ip, tmp);
    tmp=inet_ntoa(ip_hdr->ip_dst);
    strcpy(dst_ip,tmp);

    printf("Src IP  : %s\n", src_ip);
    printf("Dst IP : %s\n", dst_ip);


    //print port
    u_int16_t tcp_sport=ntohs(tcp_hdr->th_sport);
    u_int16_t tcp_dport=ntohs(tcp_hdr->th_dport);
    printf("tcp_sport : %d \n",tcp_sport);
    printf("tcp_dport : %d \n",tcp_dport);

    
    
}