from django.core.management.base import BaseCommand
from osi.models import OsiLayer

class Command(BaseCommand):
    help = 'Loads professional sample data for the OSI Model layers'

    def handle(self, *args, **kwargs):
        data = [
            {
                'layer_number': 7,
                'name': 'Application',
                'description': 'The Application Layer provides direct network services to the user applications. It is the topmost layer and serves as the window for users and application processes to access network services.',
                'real_life_example': 'Opening a web browser and communicating with a web server to retrieve an academic article. The browser acts as the client applying HTTP to request the resource.',
                'protocols': 'HTTP, HTTPS, FTP, SMTP, DNS'
            },
            {
                'layer_number': 6,
                'name': 'Presentation',
                'description': 'The Presentation Layer ensures that data is in a usable format and is where data encryption, compression, and translation occur. It acts as the syntax layer for the network.',
                'real_life_example': 'Encrypting a sensitive login password using SSL before transmission, or displaying a JPEG image correctly on the screen.',
                'protocols': 'SSL, TLS, ASCII, JPEG, MPEG'
            },
            {
                'layer_number': 5,
                'name': 'Session',
                'description': 'The Session Layer is responsible for establishing, managing, and terminating communication sessions between two computers. It manages the dialogue control.',
                'real_life_example': 'A continuous video conference call where a continuous connection must be maintained exactly while the event is ongoing.',
                'protocols': 'NetBIOS, PPTP, RPC, SAP'
            },
            {
                'layer_number': 4,
                'name': 'Transport',
                'description': 'The Transport Layer provides transparent transfer of data between end users. It breaks data into segments and guarantees reliable or unreliable delivery by utilizing error recovery and flow control mechanisms.',
                'real_life_example': 'Sending a registered letter through the postal service which strictly requires a signature upon receipt (similar to TCP error checking).',
                'protocols': 'TCP, UDP'
            },
            {
                'layer_number': 3,
                'name': 'Network',
                'description': 'The Network Layer dictates how data packets traverse the network. It provides logical addressing (IP) and determines the best physical path (routing) to move data from the source to the destination.',
                'real_life_example': 'A GPS navigation system reading a map array to determine the most optimal driving route from one physical location to another.',
                'protocols': 'IP (IPv4, IPv6), ICMP, IPsec'
            },
            {
                'layer_number': 2,
                'name': 'Data Link',
                'description': 'The Data Link Layer controls node-to-node data transfer. It packages raw bitstreams into frames, handles hardware addressing (MAC addresses), and provides local error detection.',
                'real_life_example': 'Conversing with someone directly in the exact same room, requiring no external post office or routing mechanism.',
                'protocols': 'Ethernet, MAC, ARP, PPP'
            },
            {
                'layer_number': 1,
                'name': 'Physical',
                'description': 'The Physical Layer covers the physical means of transmitting unstructured raw bitstreams over a network architecture. It manages electrical, mechanical, and procedural checks.',
                'real_life_example': 'The actual physical fiber-optic cables, copper wires, or radio waves transmitting signals globally.',
                'protocols': 'USB, Bluetooth, IEEE 802.3 (Ethernet cabling), DSL'
            }
        ]

        # Reset existing records
        OsiLayer.objects.all().delete()
        
        # Load the newly established ones
        for item in data:
            OsiLayer.objects.create(**item)
            
        self.stdout.write(self.style.SUCCESS('Successfully loaded academic OSI Model data!'))
