/*<![CDATA[*/
var emailriddlerarray=[115,104,97,110,101,64,115,108,97,115,104,103,105,102,46,99,111,109]
var encryptedemail_id62='' //variable to contain encrypted email 
for (var i=0; i<emailriddlerarray.length; i++)
 encryptedemail_id62+=String.fromCharCode(emailriddlerarray[i])
document.write('<a href="mailto:'+encryptedemail_id62+'?subject=SlashGIF Inquiry">'+encryptedemail_id62+'</a>')
/*]]>*/
