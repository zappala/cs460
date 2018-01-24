from flask import render_template

from config import app
from .schedule import *

@app.route('/winter-2017/schedule')
def winter2017schedule():
    static = '/static/lectures/winter-2015/'
    latest = '/static/lectures/winter-2017/'
    term = '/winter-2017/'
    s = Schedule()

    s.week()

    d = s.day("January 9")
    d.lecture('Introduction','Defining the Internet')
    d.reading('Chapter 1.1 - 1.3')
    d.reading('Defining the Internet',static + 'defining-the-internet.pdf')
    d.reading('Homework: Networks and Delay',term + 'homework/networks-and-delay')

    d = s.day("January 11")
    d.lecture('Introduction','Delay, Loss, and Throughput')
    d.reading('Chapter 1.4')
    d.reading('Delay, Loss, and Throughput',static + 'delay-loss-and-throughput.pdf')
    d.reading('Queueing Theory',static + 'queueing-theory.pdf')

    d = s.day("January 13")
    d.lecture('Introduction','Delay, Loss, and Throughput')
    d.reading('Lab: Network Simulation',term + 'labs/network-simulation')
    
    s.week()

    d = s.day("January 16")
    d.lecture("No Class", "Martin Luther King Jr. Day")

    d = s.day("January 18")
    d.lecture('Introduction','Internet Architecture, Security, History')
    d.reading('Chapter 1.5 - 1.8')
    d.reading('Internet Architecture',static + 'internet-architecture.pdf')
    d.reading('David Clark, The Design Philosophy of the DARPA Internet Protocols, ACM SIGCOMM, 1988','http://ilab.cs.byu.edu/cs460/papers/architecture/design-philosophy-sigcomm-88.pdf')
    d.reading('A Brief History of the Internet','http://www.isoc.org/internet/history/brief.shtml')

    d = s.day("January 20")
    d.lecture('Introduction','Internet Architecture, Security, History')

    s.week()

    d = s.day("January 23")
    d.lecture('Application Layer','Email')
    d.reading('Chapter 2.4')
    d.reading('Email',static + 'email.pdf')
    d.assignment('Homework: Networks and Delay',term + 'homework/networks-and-delay')

    #d.reading("Understanding the Domain Registration Behavior of Spammers (optional)","http://conferences.sigcomm.org/imc/2013/papers/imc247-haoA.pdf")
    #d.reading('The Long "Taile" of Typosquatting Domain Names (optional, domains)',"https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/szurdi")
    #d.reading("Understanding the Dark Side of Domain Parking (optional, domains)","https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/alrwais")

    d = s.day("January 25")
    d.lecture('Application Layer','DNS')
    d.reading('From .academy to .zone: An Analysis of the New TLD Land Rush','https://ian.ucsd.edu/papers/imc15-tld.pdf')
    d.reading('Homework: Applications',term + 'homework/applications')
    
    d = s.day("January 27")
    d.lecture('Application Layer','DNS')
    d.reading('From .academy to .zone: An Analysis of the New TLD Land Rush','https://ian.ucsd.edu/papers/imc15-tld.pdf')

    s.week()

    d = s.day('January 30')
    d.lecture("No Class")

    d = s.day('February 1')
    d.lecture('Application Layer','Peer-to-Peer Networking')
    d.reading('Chapter 2.5')
    d.reading('Peer-to-Peer Networking',latest + 'peer-to-peer-networking.pdf')

    d = s.day('February 3')
    d.lecture('Application Layer','Video Streaming and CDNs')
    d.reading('Video Streaming and CDNs',latest + 'video-streaming-and-cdns.pdf')
    d.reading('Chapter 2.6')
    d.assignment('Lab: Network Simulation',term + 'labs/network-simulation')
    
    s.week()

    d = s.day('February 6')
    d.lecture('Transport Layer','Reliable Transport Fundamentals')
    d.reading('Chapter 3.1 - 3.4')
    d.reading('Transport Layer and UDP',static + 'transport-layer-and-udp.pdf')
    d.reading('Reliable Transport Fundamentals',static + 'reliable-transport-fundamentals.pdf')
    d.reading('Homework: Transport Layer',term + 'homework/transport-layer')
    d.reading('Lab: Reliable Transport',term + 'labs/reliable-transport')

    d = s.day('February 8')
    d.lecture('Transport Layer','Reliable Transport Fundamentals')
    d.assignment('Homework: Applications',term + 'homework/applications')

    d = s.day('February 10')    
    d.lecture('Transport Layer','TCP Reliability')
    d.reading('Chapter 3.5')
    d.reading('TCP Reliability',static + 'tcp-reliability.pdf')

    s.week()

    d = s.day('February 13')
    d.lecture('Transport Layer','TCP Reliability')    
  
    d = s.day('February 15')
    d.lecture('Transport Layer','TCP Reliability')

    d = s.day('February 17')
    d.reading('Lab: Reliable Transport',term + 'labs/reliable-transport')

    s.week()

    d = s.day('February 20')
    d.lecture('No Class','Monday Instruction')

    d = s.day('February 21')
    d.lecture('Transport Layer','Congestion Control')
    d.reading('Congestion Control',static + 'congestion-control.pdf')

    d = s.day('February 22')
    d.lecture('Transport Layer','Congestion Control')

    d = s.day('February 24')
    d.lecture('Transport Layer','Congestion Control')
    d.reading('Kevin Fall and Sally Floyd, Simulation-based Comparisons of Tahoe, Reno, and SACK TCP, ACM Computer Communications Review, Volume 26, Number 3, July, 1996','http://www.icir.org/floyd/papers/sacks.pdf')
    d.assignment('Lab: Reliable Transport',term + 'labs/reliable-transport')

    s.week()

    d = s.day('February 27')
    d.lecture('Transport Layer','Congestion Control')
    d.reading('Lab: Congestion Control Part 1',term + 'labs/congestion-control-part-1')

    d = s.day('March 1')
    d.assignment('Homework: Transport Layer',term + 'homework/transport-layer')
    
    d = s.day('March 3')
    d.assignment('Midterm')
    
    s.week()

    d = s.day('March 6')
    d.lecture('Network Layer','The Network Layer and Routers')
    d.reading('Chapter 4.1 - 4.2')
    d.reading('The Network Layer and Routers',static + 'network-layer-and-routers.pdf')
    d.reading('Homework: Network Layer',term + 'homework/network-layer')
   
    d = s.day('March 8')
    d.lecture('Network Layer','The Network Layer and Routers')

    d = s.day('March 10')
    d.lecture('Network Layer','IPv4 and IPv6')
    d.reading('Chapter 4.3')
    d.reading('IPv4 and IPv6',latest + 'ipv4-and-ipv6.pdf')

    s.week()

    d = s.day('March 13')
    d.lecture('Network Layer','IPv4 and IPv6')
     
    d = s.day('March 15')
    d.lecture('Network Layer','IPv4 and IPv6')

    d = s.day('March 17')
    d.lecture("No Class","Spring Break")
    
    s.week()

    d = s.day('March 20')
    d.lecture('Network Layer','Routing Algorithms')
    d.reading('Routing Algorithms',latest + 'routing-algorithms.pdf')
    d.reading('Chapter 5.1 - 5.3')
    d.reading('Lab: Congestion Control Part 2',term + 'labs/congestion-control-part-2')
    d.assignment('Lab: Congestion Control Part 1',term + 'labs/congestion-control-part-1')

    d = s.day('March 22')
    d.lecture('Network Layer','Routing Algorithms')

    d = s.day('March 24')
    d.lecture('Network Layer','BGP')
    d.reading('BGP',latest + 'bgp.pdf')
    d.reading('Chapter 5.4')

    s.week()
    d = s.day('March 27')
    d.lecture('Network Layer','SDN')
    d.reading('SDN',latest + 'sdn.pdf')
    d.reading('Chapter 4.4, 5.5')
    
    d = s.day('March 29')
    d.lecture('Network Layer','Broadcast and Multicast Routing')
    d.reading('Broadcast and Multicast Routing',static + 'broadcast-and-multicast-routing.pdf')
    d.assignment('Homework: Network Layer',term + 'homework/network-layer')
    

    d = s.day('March 31')
    d.assignment('Midterm')
    
    s.week()

    d = s.day('April 3')
    d.lecture('Link Layer','Error Detection and Multiple Access')
    d.reading('Chapter 6.1 - 6.3')
    d.reading('Error Detection and Multiple Access',static + 'error-detection-and-multiple-access.pdf')
    d.assignment('Lab: Congestion Control Part 2',term + 'labs/congestion-control-part-2')
    d.reading('Lab: Routing',term + 'labs/routing')

    d = s.day('April 5')
    d.lecture('Link Layer','Switched Local Area Networks, MPLS, Data Center Networking, Retrospective')
    d.reading('Chapter 6.4 - 6.7')
    d.reading('Switched Local Area Networks',static + 'switched-local-area-networks.pdf')
    d.reading('MPLS, Data Center Networking, Retrospective',static + 'mpls-data-centers-retrospective.pdf')

    d = s.day('April 7')
    d.lecture('Wireless Networks','Wireless and WiFi')
    d.reading('Chapter 7.1 - 7.3')
    d.reading('Wireless and WiFi',static + 'wireless-and-wifi.pdf')
    d.assignment('Homework: Link Layer',term + 'homework/link-layer')

    s.week()

    d = s.day('April 10')
    d.lecture('Wireless Networks','Cellular Networks and Mobility')
    d.reading('Chapter 7.4 - 7.8')
    d.reading('Cellular Networks and Mobility',static + 'cellular-networks-and-mobility.pdf')

    d = s.day('April 12')
    d.reading('Chapter 9.1 - 9.3')
    d.lecture('Multimedia Networks','Multimedia Applications and Streaming Video, Voice-Over-IP')
    d.reading('Multimedia Applications and Streaming Video',static + 'multimedia-applications-and-streaming-video.pdf')
    d.reading('Voice-Over-IP',static + 'voice-over-ip.pdf')
    d.assignment('Homework: Wireless',term + 'homework/wireless')

    d = s.day('April 14')
    d.lecture('Multimedia Networks','Network Support for Multimedia')
    d.reading('Chapter 9.4 - 9.5')
    d.reading('Network Support for Multimedia',static + 'network-support-for-multimedia.pdf')

    s.week()

    d = s.day('April 17')
    d.lecture('Networking Research')
    d.assignment('Lab: Routing',term + 'labs/routing')

    d = s.day('April 19')
    d.lecture('Networking Research')

    d.assignment('Homework: Multimedia Networks',term + 'homework/multimedia-networks')

    s.week()

    d = s.day('April 25')
    d.assignment('Final Exam: 7:00am - 10:00am')

    return render_template('winter-2017/schedule.html',active='schedule',
                           weeks=s.weeks)
