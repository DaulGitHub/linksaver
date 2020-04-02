### Links saver
1. in stall redis database<br>
2. activate virtualenv
3. install requirements.txt<br>
<code>$ pip install -r requirements.txt</code>
4. run application<br>
<code>flask run</code>

##### test
manual:<br>
 please open console<br>
<code>$ curl --header "Content-Type: application/json"   --request POST   --data '{ "links": ["https://ya.ru", "https://ya.ru?q=123", "funbox.ru", "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"] }' http://localhost:5000/visited_links</code>

<code>$ "http://localhost:5000/visited_domains?from=1385640049&to=1885840286"</code>

for run  autotests, execute<br> 
<code>$ python -m pytest</code>