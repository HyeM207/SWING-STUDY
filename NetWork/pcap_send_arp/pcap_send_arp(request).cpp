#include <stdlib.h>
#include <stdio.h>

#include <pcap.h>


int main(int argc, char **argv)
{
pcap_t *fp;
char errbuf[PCAP_ERRBUF_SIZE];
u_char packet[100];
int i;

    /* Check the validity of the command line */
    if (argc != 2)
    {
        printf("usage: %s interface (e.g. 'rpcap://eth0')", argv[0]);
        return -1;
    }
    
    /* Open the output device */
    if ( (fp= pcap_open_live(argv[1],            // name of the device
                        100,                // portion of the packet to capture (only the first 100 bytes)
                        PCAP_OPENFLAG_PROMISCUOUS,  // promiscuous mode
                        1000,               // read timeout
                        errbuf              // error buffer
                        ) ) == NULL)
    {
        fprintf(stderr,"\nUnable to open the adapter. %s is not supported by WinPcap\n", argv[1]);
        return -1;
    }

    /* Supposing to be on ethernet, set mac destination to 1:1:1:1:1:1 */
    packet[0]=1;
    packet[1]=1;
    packet[2]=1;
    packet[3]=1;
    packet[4]=1;
    packet[5]=1;
    
    /* set mac source to 2:2:2:2:2:2 */
    packet[6]=2;
    packet[7]=2;
    packet[8]=2;
    packet[9]=2;
    packet[10]=2;
    packet[11]=2;

    /* set type to arp(0x0806) */
    packet[12]=8;
    packet[13]=6;

    /* #####set arp packet##### */
    /* set hardware Type */
    packet[14]=0;
    packet[15]=1;
    /* set protocol Type */
    packet[16]=8;
    packet[17]=0;
    /* set hardware size */
    packet[18]=6;
    /* set protocol size */
    packet[19]=4;
    /* set OPcode */
    packet[20]=0;
    packet[21]=1;
    /* set sender Mac to 2:2:2:2:2:2*/
    packet[22]=2;
    packet[23]=2;
    packet[24]=2;
    packet[25]=2;
    packet[26]=2;
    packet[27]=2;
    /* set sender IP to */
    packet[28]=192;
    packet[29]=168;
    packet[30]=211;
    packet[31]=129;
    /* set target Mac to 1:1:1:1:1:1 */
    packet[32]=1;
    packet[33]=1;
    packet[34]=1;
    packet[35]=1; 
    packet[36]=1;
    packet[37]=1;
    /* set target ip to  */
    packet[38]=192;
    packet[39]=168;
    packet[40]=211;
    packet[41]=127;
    /* Fill the rest of the packet */
    for(i=42;i<100;i++)
    {
        packet[i]=i%256;
    }

    /* Send down the packet */
    if (pcap_sendpacket(fp, packet, 100 /* size */) != 0)
    {
        fprintf(stderr,"\nError sending the packet: \n", pcap_geterr(fp));
        return -1;
    }

    return 0;
}