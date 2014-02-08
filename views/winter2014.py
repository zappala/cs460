from flask import render_template

from config import app
from schedule import *

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
    d.reading('Kevin Fall and Sally Floyd, Simulation-based Comparisons of Tahoe, Reno, and SACK TCP, ACM Computer Communications Review, Volume 26, Number 3, July, 1996','http://ilab.cs.byu.edu/cs460/papers/tcp/tcp-sack-ccr-96.pdf')

    d = s.day('February 14')
    d.lecture('Network Layer','The Network Layer and Routers')
    d.assignment('Homework: Transport Layer',term + 'homework/transport-layer')

    s.week()

    d = s.day('February 17')
    d.lecture('No Class','Presidents Day Holiday')

    d = s.day('February 18')
    d.lecture('Lab Day')
    d.assignment('Lab: Reliable Transport',term + 'labs/reliable-transport')

    d = s.day('February 19')
    d.lecture('Network Layer','IPv4 and IPv6')

    d = s.day('February 21')
    d.lecture('Network Layer','IPv4 and IPv6')

    s.week()

    d = s.day('February 24')
    d.lecture('Network Layer','IPv4 and IPv6')

    d = s.day('February 26')
    d.assignment('Midterm')

    d = s.day('February 28')
    d.lecture('Network Layer','Routing Algorithms')

    s.week()

    d = s.day('March 3')
    d.lecture('Network Layer','Routing in the Internet')

    d = s.day('March 5')
    d.lecture('Network Layer','Broadcast and Multicast Routing')

    d = s.day('March 7')
    d.lecture('Network Layer','Broadcast and Multicast Routing')

    s.week()

    d = s.day('March 10')
    d.lecture('Lab Day')

    d = s.day('March 12')
    d.lecture('Link Layer','Error Detection and Multiple Access')

    d = s.day('March 14')
    d.lecture('Link Layer','Switched Local Area Networks')

    s.week()

    d = s.day('March 17')
    d.lecture('Link Layer','MPLS, Data Center Networking, Retrospective')

    d = s.day('March 19')
    d.lecture('Wireless Networks','Wireless and WiFi')

    d = s.day('March 21')
    d.lecture('Wireless Networks','Cellular Networks and Mobility')

    s.week()

    d = s.day('March 24')
    d.lecture('Wireless Networks','Cellular Networks and Mobility')

    d = s.day('March 26')
    d.assignment('Midterm')

    d = s.day('March 28')
    d.lecture('Multimedia Networks','Multimedia Applications and Streaming Video')

    s.week()

    d = s.day('March 31')
    d.lecture('Multimedia Networks','Voice-Over-IP')

    d = s.day('April 2')
    d.lecture('Multimedia Networks','Network Support for Multimedia')

    d = s.day('April 4')
    d.lecture('Multimedia Networks','Network Support for Multimedia')

    s.week()

    d = s.day('April 7')

    d = s.day('April 9')

    d = s.day('April 11')

    s.week()

    d = s.day('April 14')

    d = s.day('April 19')
    d.assignment('Final Exam: 11:00am - 1:00pm')

    return render_template('winter-2014/schedule.html',active='schedule',
                           weeks=s.weeks)
