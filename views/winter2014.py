from flask import render_template

from config import app
from .schedule import *

@app.route('/winter-2014/schedule')
def schedule():
    static = '/static/lectures/winter-2014/'
    term = '/winter-2014/'
    s = Schedule()

    s.week()

    d = s.day("January 6")
    d.lecture('Introduction','Defining the Internet')
    d.reading('Chapter 1.1 - 1.3')
    d.reading('Defining the Internet',static + 'defining-the-internet.pdf')
    d.reading('Homework: Networks and Delay',term + 'homework/networks-and-delay')

    d = s.day("January 8")
    d.lecture('Introduction','Defining the Internet')

    d = s.day("January 10")
    d.lecture('Introduction','Delay, Loss, and Throughput')
    d.reading('Chapter 1.4')
    d.reading('Delay, Loss, and Throughput',static + 'delay-loss-and-throughput.pdf')

    s.week()

    d = s.day("January 13")
    d.lecture('Lab Day')
    d.reading('Lab: Network Simulation',term + 'labs/network-simulation')
    d = s.day("January 15")
    d.lecture('Introduction','Internet Architecture, Security, History')
    d.reading('Chapter 1.5 - 1.8')
    d.reading('Internet Architecture',static + 'internet-architecture.pdf')
    d.reading('David Clark, The Design Philosophy of the DARPA Internet Protocols, ACM SIGCOMM, 1988','http://ilab.cs.byu.edu/cs460/papers/architecture/design-philosophy-sigcomm-88.pdf')
    d.reading('A Brief History of the Internet','http://www.isoc.org/internet/history/brief.shtml')

    d = s.day("January 17")
    d.lecture('Application Layer','Email')
    d.reading('Chapter 2.4')
    d.reading('Email',static + 'email.pdf')
    d.assignment('Homework: Networks and Delay',term + 'homework/networks-and-delay')

    s.week()

    d = s.day("January 20")
    d.lecture('No Class','Martin Luthor King Jr. Holiday')

    d = s.day("January 22")
    d.lecture('Application Layer','Peer-to-Peer Networking')
    d.reading('Chapter 2.6')
    d.reading('Peer-to-Peer Networking',static + 'peer-to-peer-networking.pdf')

    d = s.day('January 24')
    d.lecture('Application Layer','Peer-to-Peer Networking')
    d.reading('Homework: Applications',term + 'homework/applications')
    d.assignment('Lab: Network Simulation',term + 'labs/network-simulation')

    s.week()

    d = s.day('January 27')
    d.lecture('Transport Layer','Transport Layer and UDP')
    d.reading('Chapter 3.1 - 3.3')
    d.reading('Transport Layer and UDP',static + 'transport-layer-and-udp.pdf')

    d = s.day('January 29')
    d.reading('Chapter 3.4')
    d.lecture('Transport Layer','Reliable Transport Fundamentals')
    d.reading('Reliable Transport Fundamentals',static + 'reliable-transport-fundamentals.pdf')
    d.reading('Homework: Transport Layer',term + 'homework/transport-layer')
    d.assignment('Homework: Applications',term + 'homework/applications')

    d = s.day('January 31')
    d.lecture('Transport Layer','TCP Reliability')
    d.reading('TCP Reliability',static + 'tcp-reliability.pdf')

    s.week()

    d = s.day('February 3')
    d.lecture('Lab Day')

    d = s.day('February 5')
    d.lecture('Transport Layer','TCP Reliability')

    d = s.day('February 7')
    d.lecture('Transport Layer','Congestion Control')
    d.reading('Congestion Control',static + 'congestion-control.pdf')

    s.week()

    d = s.day('February 10')
    d.lecture('Transport Layer','Congestion Control')
  
    d = s.day('February 12')
    d.lecture('Transport Layer','Congestion Control')

    d = s.day('February 14')
    d.lecture('Transport Layer','Congestion Control')
    d.reading('Kevin Fall and Sally Floyd, Simulation-based Comparisons of Tahoe, Reno, and SACK TCP, ACM Computer Communications Review, Volume 26, Number 3, July, 1996','http://ilab.cs.byu.edu/cs460/papers/tcp/tcp-sack-ccr-96.pdf')
    d.assignment('Homework: Transport Layer',term + 'homework/transport-layer')
    d.reading('Homework: Network Layer',term + 'homework/network-layer')

    s.week()

    d = s.day('February 17')
    d.lecture('No Class','Presidents Day Holiday')

    d = s.day('February 18')
    d.lecture('Network Layer','The Network Layer and Routers')
    d.reading('The Network Layer and Routers',static + 'network-layer-and-routers.pdf')
    d.assignment('Lab: Reliable Transport',term + 'labs/reliable-transport')

    d = s.day('February 19')
    d.reading('IPv4 and IPv6',static + 'ipv4-and-ipv6.pdf')
    d.lecture('Network Layer','IPv4 and IPv6')

    d = s.day('February 21')
    d.lecture('Network Layer','IPv4 and IPv6')

    s.week()

    d = s.day('February 24')
    d.lecture('Lab Day')

    d = s.day('February 26')
    d.assignment('Midterm')

    d = s.day('February 28')
    d.lecture('Network Layer','Routing Algorithms')
    d.reading('Routing Algorithms',static + 'routing-algorithms.pdf')

    s.week()

    d = s.day('March 3')
    d.lecture('Network Layer','Routing in the Internet')
    d.reading('Routing in the Internet',static + 'routing-in-the-internet.pdf')

    d = s.day('March 5')
    d.lecture('Network Layer','Broadcast and Multicast Routing')
    d.reading('Broadcast and Multicast Routing',static + 'broadcast-and-multicast-routing.pdf')

    d = s.day('March 7')
    d.lecture('Network Layer','Broadcast and Multicast Routing')

    s.week()

    d = s.day('March 10')
    d.lecture('Link Layer','Error Detection and Multiple Access')
    d.reading('Error Detection and Multiple Access',static + 'error-detection-and-multiple-access.pdf')
    d.assignment('Lab: Congestion Control',term + 'labs/congestion-control')

    d = s.day('March 12')
    d.lecture('No Class','')

    d = s.day('March 14')
    d.lecture('No Class','')

    s.week()

    d = s.day('March 17')
    d.assignment('Homework: Network Layer',term + 'homework/network-layer')
    d.lecture('Lab Day')

    d = s.day('March 19')
    d.lecture('Link Layer','Switched Local Area Networks')
    d.reading('Switched Local Area Networks',static + 'switched-local-area-networks.pdf')

    d = s.day('March 21')
    d.lecture('Link Layer','MPLS, Data Center Networking, Retrospective')
    d.reading('MPLS, Data Center Networking, Retrospective',static + 'mpls-data-centers-retrospective.pdf')

    s.week()
    d = s.day('March 24')
    d.lecture('Wireless Networks','Wireless and WiFi')
    d.reading('Wireless and WiFi',static + 'wireless-and-wifi.pdf')

    d = s.day('March 26')
    d.lecture('Wireless Networks','Cellular Networks and Mobility')
    d.reading('Cellular Networks and Mobility',static + 'cellular-networks-and-mobility.pdf')

    d = s.day('March 28')
    d.assignment('Midterm')

    s.week()

    d = s.day('March 31')
    d.lecture('Wireless Networks','')
    d.assignment('Homework: Link Layer',term + 'homework/link-layer')

    d = s.day('April 2')
    d.lecture('Multimedia Networks','Multimedia Applications and Streaming Video')
    d.reading('Multimedia Applications and Streaming Video',static + 'multimedia-applications-and-streaming-video.pdf')

    d = s.day('April 4')
    d.lecture('Multimedia Networks','Voice-Over-IP')
    d.reading('Voice-Over-IP',static + 'voice-over-ip.pdf')

    s.week()

    d = s.day('April 7')
    d.lecture('Multimedia Networks','Network Support for Multimedia')
    d.reading('Network Support for Multimedia',static + 'network-support-for-multimedia.pdf')

    d = s.day('April 9')
    d.lecture('Multimedia Networks','Network Support for Multimedia')
    d.assignment('Homework: Wireless',term + 'homework/wireless')

    d = s.day('April 11')

    s.week()

    d = s.day('April 14')
    d.assignment('Homework: Multimedia Networks',term + 'homework/multimedia-networks')
    d.assignment('Lab: Routing',term + 'labs/routing')

    d = s.day('April 19')
    d.assignment('Final Exam: 11:00am - 1:00pm')

    return render_template('winter-2014/schedule.html',active='schedule',
                           weeks=s.weeks)
