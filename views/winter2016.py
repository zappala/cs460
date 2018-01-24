from flask import render_template

from config import app
from .schedule import *

@app.route('/winter-2016/schedule')
def winter2016schedule():
    static = '/static/lectures/winter-2015/'
    term = '/winter-2016/'
    s = Schedule()

    s.week()

    d = s.day("January 5")
    d.lecture('Introduction','Defining the Internet')
    d.reading('Chapter 1.1 - 1.3')
    d.reading('Defining the Internet',static + 'defining-the-internet.pdf')
    d.reading('Homework: Networks and Delay',term + 'homework/networks-and-delay')

    d = s.day("January 7")
    d.lecture('Introduction','Delay, Loss, and Throughput')
    d.reading('Chapter 1.4')
    d.reading('Delay, Loss, and Throughput',static + 'delay-loss-and-throughput.pdf')
    d.reading('Queueing Theory',static + 'queueing-theory.pdf')
    
    s.week()

    d = s.day("January 12")
    d.lecture('Introduction','Internet Architecture, Security, History')
    d.reading('Chapter 1.5 - 1.8')
    d.reading('Internet Architecture',static + 'internet-architecture.pdf')
    d.reading('David Clark, The Design Philosophy of the DARPA Internet Protocols, ACM SIGCOMM, 1988','http://ilab.cs.byu.edu/cs460/papers/architecture/design-philosophy-sigcomm-88.pdf')
    d.reading('A Brief History of the Internet','http://www.isoc.org/internet/history/brief.shtml')
    d.reading('Lab: Network Simulation',term + 'labs/network-simulation')

    d = s.day("January 14")
    d.reading('TBD')

    s.week()

    d = s.day("January 19")
    d.lecture('Application Layer','Email')
    d.reading('Chapter 2.4')
    d.reading('Email',static + 'email.pdf')
    d.reading("Understanding the Domain Registration Behavior of Spammers (optional)","http://conferences.sigcomm.org/imc/2013/papers/imc247-haoA.pdf")
    d.reading('The Long "Taile" of Typosquatting Domain Names (optional, domains)',"https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/szurdi")
    d.reading("Understanding the Dark Side of Domain Parking (optional, domains)","https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/alrwais")
    d.assignment('Homework: Networks and Delay',term + 'homework/networks-and-delay')

    d = s.day("January 21")
    d.lecture('Application Layer','Peer-to-Peer Networking')
    d.reading('Chapter 2.6')
    d.reading('Peer-to-Peer Networking',static + 'peer-to-peer-networking.pdf')
    d.reading('Homework: Applications',term + 'homework/applications')

    s.week()

    d = s.day('January 26')
    d.lecture('Application Layer','Peer-to-Peer Networking')
    d.assignment('Lab: Network Simulation',term + 'labs/network-simulation')

    d = s.day('January 28')
    d.lecture('Transport Layer','Transport Layer and UDP and Reliable Transport Fundamentals')
    d.reading('Chapter 3.1 - 3.4')
    d.reading('Transport Layer and UDP',static + 'transport-layer-and-udp.pdf')
    d.reading('Reliable Transport Fundamentals',static + 'reliable-transport-fundamentals.pdf')
    d.reading('Homework: Transport Layer',term + 'homework/transport-layer')

    s.week()

    d = s.day('February 2')
    d.lecture('Transport Layer','TCP Reliability')
    d.reading('Chapter 3.5')
    d.reading('TCP Reliability',static + 'tcp-reliability.pdf')
    d.assignment('Homework: Applications',term + 'homework/applications')
    d.reading('Lab: Reliable Transport',term + 'labs/reliable-transport')

    d = s.day('February 4')
    d.reading('Chapter 3.6 - 3.7')
    d.lecture('Transport Layer','TCP Reliability')    

    s.week()

    d = s.day('February 9')
    d.lecture('Transport Layer','TCP Reliability')    
  
    d = s.day('February 11')

    s.week()

    d = s.day('February 16')
    d.lecture('No Class','Monday Instruction')

    d = s.day('February 18')
    d.lecture('Transport Layer','Congestion Control')
    d.reading('Congestion Control',static + 'congestion-control.pdf')


    d = s.day('February 20')
    d.assignment('Lab: Reliable Transport',term + 'labs/reliable-transport')

    s.week()

    d = s.day('February 23')
    d.lecture('Transport Layer','Congestion Control')
    d.reading('Kevin Fall and Sally Floyd, Simulation-based Comparisons of Tahoe, Reno, and SACK TCP, ACM Computer Communications Review, Volume 26, Number 3, July, 1996','http://ilab.cs.byu.edu/cs460/papers/tcp/tcp-sack-ccr-96.pdf')
    d.reading('Lab: Congestion Control Part 1',term + 'labs/congestion-control-part-1')
    

    d = s.day('February 25')
    d.lecture('Network Layer','The Network Layer and Routers')
    d.reading('Chapter 4.1 - 4.3')
    d.reading('The Network Layer and Routers',static + 'network-layer-and-routers.pdf')
    d.reading('Homework: Network Layer',term + 'homework/network-layer')
    d.assignment('Homework: Transport Layer',term + 'homework/transport-layer')

    s.week()

    d = s.day('March 1')
    d.lecture('Network Layer','IPv4 and IPv6')
    d.reading('Chapter 4.4')
    d.reading('IPv4 and IPv6',static + 'ipv4-and-ipv6.pdf')
   
    d = s.day('March 3')
    d.lecture('Network Layer','IPv4 and IPv6')
    d.reading('Chapter 4.4')
    d.reading('IPv4 and IPv6',static + 'ipv4-and-ipv6.pdf')

    s.week()

    d = s.day('March 8')
    d.assignment('Midterm')
     
    d = s.day('March 10')
    d.lecture('Network Layer','Routing')
    d.reading('Chapter 4.5 - 4.6')
    d.reading('Routing Algorithms',static + 'routing-algorithms.pdf')
    d.reading('Routing in the Internet',static + 'routing-in-the-internet.pdf')

    s.week()

    d = s.day('March 14')
    d.assignment('Lab: Congestion Control Part 1',term + 'labs/congestion-control-part-1')

    d = s.day('March 15')
    d.lecture('Network Layer','Broadcast and Multicast Routing')
    d.reading('Chapter 4.7')
    d.reading('Broadcast and Multicast Routing',static + 'broadcast-and-multicast-routing.pdf')
    d.reading('Lab: Congestion Control Part 2',term + 'labs/congestion-control-part-2')

    d = s.day('March 17')
    d.lecture('Network Layer','Broadcast and Multicast Routing')

    s.week()
    d = s.day('March 22')
    d.lecture('Link Layer','Error Detection and Multiple Access')
    d.reading('Chapter 5.1 - 5.3')
    d.reading('Error Detection and Multiple Access',static + 'error-detection-and-multiple-access.pdf')
    
    d = s.day('March 24')
    d.lecture('Link Layer','Switched Local Area Networks, MPLS, Data Center Networking, Retrospective')
    d.reading('Chapter 5.4 - 5.7')
    d.reading('Switched Local Area Networks',static + 'switched-local-area-networks.pdf')
    d.reading('MPLS, Data Center Networking, Retrospective',static + 'mpls-data-centers-retrospective.pdf')
    d.assignment('Homework: Network Layer',term + 'homework/network-layer')

    d = s.day('March 26')    
    d.assignment('Lab: Congestion Control Part 2',term + 'labs/congestion-control-part-2')

    s.week()

    d = s.day('March 29')
    d.lecture('Wireless Networks','Wireless and WiFi')
    d.reading('Chapter 6.1 - 6.3')
    d.reading('Wireless and WiFi',static + 'wireless-and-wifi.pdf')
    d.reading('Lab: Routing',term + 'labs/routing')

    d = s.day('April 31')
    d.lecture('Wireless Networks','Cellular Networks and Mobility')
    d.reading('Chapter 6.4 - 6.8')
    d.reading('Cellular Networks and Mobility',static + 'cellular-networks-and-mobility.pdf')

    s.week()

    d = s.day('April 5')
    d.reading('Chapter 7.1 - 7.3')
    d.lecture('Multimedia Networks','Multimedia Applications and Streaming Video, Voice-Over-IP')
    d.reading('Multimedia Applications and Streaming Video',static + 'multimedia-applications-and-streaming-video.pdf')
    d.reading('Voice-Over-IP',static + 'voice-over-ip.pdf')
    d.assignment('Homework: Link Layer',term + 'homework/link-layer')
    
    d = s.day('April 7')
    d.lecture('Multimedia Networks','Network Support for Multimedia')
    d.reading('Chapter 7.4 - 7.5')
    d.reading('Network Support for Multimedia',static + 'network-support-for-multimedia.pdf')
    d.assignment('Homework: Wireless (extra credit)',term + 'homework/wireless')

    s.week()

    d = s.day('April 12')
    d.lecture('Multimedia Networks','Network Support for Multimedia')
    d.assignment('Homework: Multimedia Networks (extra credit)',term + 'homework/multimedia-networks')
    d.assignment('Lab: Routing',term + 'labs/routing')

    d = s.day('April 15')
    d.assignment('Final Exam: 7:00am - 10:00am')

    return render_template('winter-2016/schedule.html',active='schedule',
                           weeks=s.weeks)
