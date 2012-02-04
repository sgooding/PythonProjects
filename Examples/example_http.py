
import httplib
conn = httplib.HTTPConnection("www.python.org");
conn.request("GET","/index.html");
r1 = conn.getresponse();
print r1.status, r1.reason
data1 = r1.read();
conn.request("GET","/parrot.spam");
r2 = conn.getresponse();
print r2.status, r2.reason;
conn.close();

conn2 = httplib.HTTPConnection("msrmaps.com");
conn2.request("GET","/download.aspx?T=4&S=8&Z=13&X=9292&Y=87307&W=1&qs=91+sun+way%7cbailey%7cco%7c&Addr=91+Sun+Way%2c+Bailey%2c+CO+80421&ALon=-105.4108149&ALat=39.4372766")
r3 = conn2.getresponse();


this_file = open("image.html","w");
this_file.write(r3.read());
this_file.close();
