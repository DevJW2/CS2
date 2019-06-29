#!/usr/bin/python
print "content-type: text/html\n"

import cgi
results= cgi.FieldStorage()

def writeOrReplace(filename,username,name,month,day,year,email,url):
    #check if you need to remove old values
    f = open(filename,'r').read().split("\n");
    data = [each.split(',') for each in f]
    write = False
    for i in range(len(data))[::-1]:
        if data[i]==['']:
            write = True
            data.pop(i)
        elif data[i][0]==username:
            data.pop(i)
            write = True
    ##remove a line if needed
    if write:
        res = ""
        for each in data:
            res+= ",".join(each)+"\n"
        f = open(filename,'w')
        f.write(res)
        f.close()
    #append the line to the file
    f = open(filename,'a')
    f.write(username+","+str(name)+","+str(month)+'/'+str(day)+'/'+str(year)+','+str(email)+','+str(url)+"\n")
    f.close()

f = open('../data/loggedin.txt','r')
users=f.read()
users=users.split('\n')
if '' in users:
    users.remove('')
username=users[-1].split(',')[0]

print '''
<form method="GET" action="profileedit.py">
    NAME: <input type="text" name="name" ><br>
    BIRTHDAY:<br>
    Month:<select name="month">
    <option>January</option>
    <option>February</option>
    <option>March</option>
    <option>April</option>
    <option>May</option>
    <option>June</option>
    <option>July</option>
    <option>August</option>
    <option>September</option>
    <option>October</option>
    <option>November</option>
    <option>December</option>
    </select>
    Day:<select name="day">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    <option>5</option>
    <option>6</option>
    <option>7</option>
    <option>8</option>
    <option>9</option>
    <option>10</option>
    <option>11</option>
    <option>12</option>
    <option>13</option>
    <option>14</option>
    <option>15</option>
    <option>16</option>
    <option>17</option>
    <option>18</option>
    <option>19</option>
    <option>20</option>
    <option>21</option>
    <option>22</option>
    <option>23</option>
    <option>24</option>
    <option>25</option>
    <option>26</option>
    <option>27</option>
    <option>28</option>
    <option>29</option>
    <option>30</option>
    <option>31</option>
    </select>
    Year:<input type="text" name="year" size="4"><br>
    Email:<input type="text" name="email"><br>
    <img src="notw_silhouette-1.jpg"><br>
    New picture url:<input type="text" name="url"><br>
    <input type="submit" name="submit" value="save changes">
</form>'''

if len(results)>0:
    writeOrReplace('../data/userinfo.txt',username,results.getvalue('name'),results.getvalue('month'),results.getvalue('day'),results.getvalue('year'),results.getvalue('email'),results.getvalue('url'))
    print 'Changes saved. Click <a href="profile.py">here</a> to go back.'
    
