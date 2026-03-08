from django.core.management.base import BaseCommand
from osi.models import Layer, InterviewQuestion
from protocols.models import Protocol
from quiz.models import Question

class Command(BaseCommand):
    help = 'Load sample data for OSI Model Interactive Guide'

    def handle(self, *args, **kwargs):
        self.stdout.write("Loading sample data...")
        
        # Clear existing data
        Layer.objects.all().delete()
        Protocol.objects.all().delete()
        Question.objects.all().delete()
        InterviewQuestion.objects.all().delete()
        
        # 1. OSI Layers
        layers_data = [
            (7, 'Application', 'Provides network services to the applications of the user.', 'Web Browser, Email Client', 'HTTP, HTTPS, FTP, SMTP, DNS'),
            (6, 'Presentation', 'Ensures that data is in a usable format and is where data encryption occurs.', 'Format translation, SSL/TLS Encryption', 'JPEG, ASCII, TLS'),
            (5, 'Session', 'Maintains connections and is responsible for controlling ports and sessions.', 'Logging into a website, establishing a session', 'NetBIOS, PPTP'),
            (4, 'Transport', 'Transmits data using transmission protocols including TCP and UDP.', 'TCP connection for a web page download', 'TCP, UDP, SCTP'),
            (3, 'Network', 'Decides which physical path the data will take (Routing).', 'A Router finding the best path to a server', 'IP, ICMP, IPsec, IGMP'),
            (2, 'Data Link', 'Defines the format of data on the network (Frames, MAC address).', 'Switch forwarding frames to a specific computer', 'Ethernet, ARP, PPP'),
            (1, 'Physical', 'Transmits raw bit stream over the physical medium.', 'Cables, Hubs, Wireless signals', '100BaseT, 802.11, ISDN')
        ]
        
        layers = {}
        for l_num, name, desc, ex, protos in layers_data:
            layer = Layer.objects.create(
                layer_number=l_num,
                name=name,
                description=desc,
                real_life_example=ex,
                protocols=protos
            )
            layers[l_num] = layer
            
        self.stdout.write("Layers loaded.")
        
        # 2. Protocols
        Protocol.objects.create(name='HTTP', layer=layers[7], default_port='80', description='Hypertext Transfer Protocol for web communication.')
        Protocol.objects.create(name='HTTPS', layer=layers[7], default_port='443', description='HTTP Secure with TLS encryption.')
        Protocol.objects.create(name='FTP', layer=layers[7], default_port='21', description='File Transfer Protocol.')
        Protocol.objects.create(name='TCP', layer=layers[4], default_port='N/A', description='Transmission Control Protocol, connection-oriented.')
        Protocol.objects.create(name='UDP', layer=layers[4], default_port='N/A', description='User Datagram Protocol, connectionless.')
        Protocol.objects.create(name='IPv4', layer=layers[3], default_port='N/A', description='Used for routing packets over the internet.')
        Protocol.objects.create(name='ARP', layer=layers[2], default_port='N/A', description='Address Resolution Protocol mapping IP to MAC.')
        
        self.stdout.write("Protocols loaded.")
        
        # 3. Questions
        Question.objects.create(
            question="Which protocol belongs to the Transport Layer?",
            option_a="HTTP", option_b="TCP", option_c="FTP", option_d="DNS",
            correct_answer="B",
            explanation="TCP (Transmission Control Protocol) operates at the Transport Layer.",
            layer_reference=layers[4]
        )
        Question.objects.create(
            question="At which layer do routers primarily operate?",
            option_a="Physical", option_b="Data Link", option_c="Network", option_d="Transport",
            correct_answer="C",
            explanation="Routers operate at the Network Layer (Layer 3) to route packets using IP addresses.",
            layer_reference=layers[3]
        )
        Question.objects.create(
            question="What is the primary function of the Presentation layer?",
            option_a="Establishing sessions", option_b="Routing packets", option_c="Data encryption and formatting", option_d="Physical transmission",
            correct_answer="C",
            explanation="The Presentation layer deals with syntax and semantics, including encryption.",
            layer_reference=layers[6]
        )
        Question.objects.create(
            question="MAC addresses are primarily used at which layer?",
            option_a="Network", option_b="Data Link", option_c="Physical", option_d="Transport",
            correct_answer="B",
            explanation="MAC addresses identify devices on the same local network at the Data Link layer.",
            layer_reference=layers[2]
        )
        Question.objects.create(
            question="Which transport protocol is connectionless and does NOT guarantee delivery?",
            option_a="TCP", option_b="IP", option_c="UDP", option_d="HTTP",
            correct_answer="C",
            explanation="UDP is connectionless and faster but does not guarantee packet delivery.",
            layer_reference=layers[4]
        )
        Question.objects.create(
            question="What is the PDU (Protocol Data Unit) called at the Network Layer?",
            option_a="Segment", option_b="Frame", option_c="Packet", option_d="Bit",
            correct_answer="C",
            explanation="At the Network Layer, the unit of data is called a Packet.",
            layer_reference=layers[3]
        )
        Question.objects.create(
            question="Which layer establishes, manages, and terminates connections between applications?",
            option_a="Session", option_b="Transport", option_c="Presentation", option_d="Application",
            correct_answer="A",
            explanation="The Session layer controls the dialogue between computers and manages the session.",
            layer_reference=layers[5]
        )
        Question.objects.create(
            question="Which layer is responsible for transmitting raw bit streams over a physical medium?",
            option_a="Data Link", option_b="Physical", option_c="Network", option_d="Transport",
            correct_answer="B",
            explanation="The Physical layer deals directly with the physical media (cables, radio waves) and raw bits.",
            layer_reference=layers[1]
        )
        Question.objects.create(
            question="Which of the following is considered an Application Layer protocol?",
            option_a="ARP", option_b="IPv4", option_c="SMTP", option_d="UDP",
            correct_answer="C",
            explanation="SMTP (Simple Mail Transfer Protocol) provides email services directly to the application layer.",
            layer_reference=layers[7]
        )
        Question.objects.create(
            question="Which layer ensures error-free transmission of data over a physical link?",
            option_a="Physical", option_b="Network", option_c="Data Link", option_d="Session",
            correct_answer="C",
            explanation="The Data Link layer handles error detection and node-to-node frame delivery.",
            layer_reference=layers[2]
        )
        
        self.stdout.write("Questions loaded.")
        
        # 4. Interview Questions
        InterviewQuestion.objects.create(
            question="What is the difference between OSI and TCP/IP?",
            answer="The OSI model is a 7-layer theoretical conceptual model, whereas TCP/IP is a 4-layer practical networking model on which the internet is based. TCP/IP groups the top three OSI layers into a single Application layer."
        )
        InterviewQuestion.objects.create(
            question="What protocol resolves IP addresses to MAC addresses?",
            answer="ARP (Address Resolution Protocol) uses a broadcast mechanism to find the MAC address corresponding to a known IP address on a local network segment."
        )
        
        self.stdout.write(self.style.SUCCESS("All sample data loaded successfully!"))
