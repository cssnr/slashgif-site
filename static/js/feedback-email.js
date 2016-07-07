/*<![CDATA[*/
var emailriddlerarray=[102,101,101,100,98,97,99,107,64,115,108,97,115,104,103,105,102,46,99,111,109]
var encryptedemail_id75='' //variable to contain encrypted email 
for (var i=0; i<emailriddlerarray.length; i++)
 encryptedemail_id75+=String.fromCharCode(emailriddlerarray[i])
document.write('<a href="mailto:'+encryptedemail_id75+'?subject=SlashGIF Feedback">'+encryptedemail_id75+'</a>')
/*]]>*/