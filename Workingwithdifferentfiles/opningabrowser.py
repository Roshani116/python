#open a web browser in a python script its useful if your building a automation script that does a bunch of task 
#and at the end you have to open up a browser window,for example,lets say you want to build a script to deploy your website 
#so build your website locally on your development machine,when you are done run the script to deploy to a web server, at the end 
#you will have to open a browser type the address on your website and press int.python sript to deploy at the end
import webbrowser

print("Deployment completed")
webbrowser.open("https://www.geeksforgeeks.org/difference-between-rest-api-and-soap-api/")
