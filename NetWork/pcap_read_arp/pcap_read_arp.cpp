#include<arpa/inet.h>
#include<net/ethernet.h>
#include<netinet/ip.h>
#include<cstdio>
#include<iostream>
#include<cstring>
#include<pcap.h>

using namespace std;

    struct arp{
    u_int16_t hardType;
    u_int16_t protoType;
    u_int8_t hardAddLength;
    u_int8_t protoAddLength;
    u_int16_t opCode;
    u_int8_t senderMac[6];
    u_int8_t senderIp[4];
    u_int8_t targetMac[6];
    u_int8_t  targetIp[4];

};


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
        int res = pcap_next_ex(handle, &header, &packet); //read packet
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

    
    //if type is not ARP, return function
    if(eth_type!=2054) return;
   
    struct arp * arp_hdr= (struct arp*)(pkt_data+sizeof(ether_header));
   
    printf("\nPacket Info=======================\n");
    
    //print pkt length
    printf("%u bytes captured\n", header->caplen);

    //print mac addr
    u_int8_t *dst_mac=eth_hdr ->ether_dhost;
    u_int8_t * src_mac=eth_hdr->ether_shost;

    printf("Dst MAC : %0x:%0x:%0x:%0x:%0x:%0x\n",
        dst_mac[0], dst_mac[1],dst_mac[2],dst_mac[3],dst_mac[4],dst_mac[5]);
    printf("Src MAC : %0x:%0x:%0x:%0x:%0x:%0x\n",
        src_mac[0], src_mac[1],src_mac[2],src_mac[3],src_mac[4],src_mac[5]); 

   
    // print reply or request (arp opcode)
    if(ntohs(arp_hdr->opCode)==1){
        printf("(Request)\n");
    }
    else if(ntohs(arp_hdr->opCode)==2){
        printf("(Reply)\n");
    }
    else if(ntohs(arp_hdr->opCode)==3){
        printf("(RARP Reply)\n");
    }
    else if(ntohs(arp_hdr->opCode)==4){
        printf("(RARP Request)\n");
    }
        /*
        printf("hardtype: %04x\n",ntohs(arp_hdr->hardType));
        printf("prototype: %04x\n",ntohs(arp_hdr->protoType));
        printf("hardAddpength: %02x\n",ntohs(arp_hdr->hardAddLength));
        printf("protoAddlength: %02x\n",ntohs(arp_hdr->protoAddLength));
        printf("opcode: %04x\n",ntohs(arp_hdr->opCode));
        */
        
        //print sender/target IP&MAC
        unsigned char * sender_mac=arp_hdr->senderMac;
        unsigned char * target_mac=arp_hdr->targetMac;

        unsigned char * sender_ip=arp_hdr->senderIp;
        unsigned char * target_ip=arp_hdr->targetIp;
    
        printf("Sender MAC : %0x:%0x:%0x:%0x:%0x:%0x\n",sender_mac[0],sender_mac[1],sender_mac[2],sender_mac[3],sender_mac[4],sender_mac[5]);
        printf("Sender IP : %d.%d.%d.%d  \n",sender_ip[0],sender_ip[1],sender_ip[2],sender_ip[3]);
        printf("Target MAC : %0x:%0x:%0x:%0x:%0x:%0x\n",target_mac[0],target_mac[1],target_mac[2],target_mac[3],target_mac[4],target_mac[5]);
        printf("Target IP :  %d.%d.%d.%d  \n",target_ip[0],target_ip[1],target_ip[2],target_ip[3]); 
}