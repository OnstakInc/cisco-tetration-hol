# Cisco Tetration - Hands-On Lab
  
## Diagrams
  

### Diagrams for this Module
<a href="#diagram-000" style="font-weight:bold">Diagram 000</a>  
<a href="#diagram-001" style="font-weight:bold">Diagram 001</a>  
<a href="#diagram-002" style="font-weight:bold">Diagram 002</a>  
<a href="#diagram-003" style="font-weight:bold">Diagram 003</a>  
<a href="#diagram-004" style="font-weight:bold">Diagram 004</a>  
<a href="#diagram-005" style="font-weight:bold">Diagram 005</a>  
<a href="#diagram-006" style="font-weight:bold">Diagram 006</a>  
<a href="#diagram-007" style="font-weight:bold">Diagram 007</a>  
<a href="#diagram-008" style="font-weight:bold">Diagram 008</a>  
<a href="#diagram-009" style="font-weight:bold">Diagram 009</a>  
<a href="#diagram-010" style="font-weight:bold">Diagram 010</a>  
<a href="#diagram-011" style="font-weight:bold">Diagram 011</a>  
<a href="#diagram-012" style="font-weight:bold">Diagram 012</a>  
<a href="#diagram-013" style="font-weight:bold">Diagram 013</a>  

The URL to access all of the workloads and assets for your lab environment are unique to you and will be provided to you by the lab administrator in a CSV or XLS format. 

### Introduction to Lab Diagrams 

Throughout this lab guide you will find diagrams that can be helpful in visualizing the flow of information for a given topic. These diagrams will generally be included in the context of the task where they might add value. However, you may also wish to occasionally come back to this page to view all of the diagrams in one go. 

We recommend [Google Chrome](https://www.google.com/chrome/){:target="_blank"} for the best browsing experience.

#### A note on image sizes
If the images on any of the lab guide pages are too small, you may click on any image to open the link to its full size (fit to the browser window), and then click again if the magnifying glass shows up with a '+'. You also may prefer to see all images larger on any given page, in which case simply clicking `Ctrl +` multiple times on Windows, or `⌘ +` multiple times on a Mac, will zoom into the page size in most web browsers. However, it should be noted that if you zoom into the main documentation window, and then click on any image to open its native original, that the image may at that time be too large due to the zoom factor, and you may wish to zoom back out. To do so for Windows simply click `Ctrl -` multiple times, and for Mac click `⌘ -` multiple times, until you reach your desired size. Do note that this _may_ also change the zoom level of your main documentation window correspondingly and that you may wish to resize that window again to suit. 

### Diagrams

#### Live Interactive Diagram
You may prefer to utilize this [interactive LucidChart diagram](https://www.lucidchart.com/documents/view/425e1b97-194e-413a-b793-0df939a87501){:target="_blank"} while working on various modules in this lab. Should you choose to use the interactive diagram, follow the instructions on right of the diagram to toggle on/off various "flows", as seen in this image:

<div class="diagram" id="diagram-000"><a href="#diagram-000" style="font-weight:bold">Diagram 000</a></div><a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_000.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_000.png" style="width:35%;height:35%;"></a>  
  
To toggle flows on/off, follow the instructions for depending on whether you are using a Windows machine or a Mac. For Windows, press and hold `Shift + Ctrl`, then click. For Mac, press and hold `Shift + ⌘`, then click. When you press these key combinations, you should see the clickable links in the panel turn a sort of greenish color, as such:

<div class="diagram" id="diagram-001"><a href="#diagram-001" style="font-weight:bold">Diagram 001</a></div><a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_001.png" style="width:35%;height:35%;"></a>  


#### Base Diagram

<div class="diagram" id="diagram-002"><a href="#diagram-002" style="font-weight:bold">Diagram 002</a></div>  

As mentioned, here are are a collection of the diagram with each flow enabled, for concise reference. 

This first image is the base diagram which references the environment that _each_ learner will have access to. Note that every item you see here is completely unique and independant for each and every learner. This includes Windows VMs, Linux VMs, Active Directory, Ansible, ASAv, Tetration appliances, Lambda, Kubernetes - all of it. Each learner will also have their own unique instance of TaaS (Tetration-as-a-Service), as well. 

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_002.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_002.png" style="width:100%;height:100%;"></a>  
  

#### Incremental Diagrams with Flows

<div class="diagram" id="diagram-003"><a href="#diagram-003" style="font-weight:bold">Diagram 003</a></div>  

> NOTE: The URL to access all of the workloads and assets for your lab environment are unique to you and will be provided to you by the lab administrator in a CSV or XLS format. 

This is the flow that for a learner (that's you) accessing the lab environment. You will have been provided a unique URL and login for your TaaS instance, and will access it directly given that information (step 1 in this diagram). Step 2 in this diagram shows you accesing the lab guide documentation, which we will assume you have managed somehow since you are reading this on that documentation site, which is hosted with GitHub Pages. Step 3 on the diagram shows you accessing the three applications that you have unique to your lab environment. 

In your lab are one of each of the following apps:

   1. Windows app - "nopCommerce" - consisting of: 
      *  Win19 IIS WebApp server
      *  Win19 MS SQL DB server
   2. Linux app - "OpenCart"
      *  CentOS 7 Apache WebApp server
      *  CentOS 7 MySQL DB server
   4. Microservices Container app on Kubernetes - "Sock Shop"

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_003.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_003.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-004"><a href="#diagram-004" style="font-weight:bold">Diagram 004</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_004.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_004.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-005"><a href="#diagram-005" style="font-weight:bold">Diagram 005</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_005.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_005.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-006"><a href="#diagram-006" style="font-weight:bold">Diagram 006</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_006.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_006.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-007"><a href="#diagram-007" style="font-weight:bold">Diagram 007</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_007.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_007.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-008"><a href="#diagram-008" style="font-weight:bold">Diagram 008</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_008.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-009"><a href="#diagram-009" style="font-weight:bold">Diagram 009</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_009.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_009.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-010"><a href="#diagram-010" style="font-weight:bold">Diagram 010</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_010.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_010.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-011"><a href="#diagram-011" style="font-weight:bold">Diagram 011</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_011.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_011.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-012"><a href="#diagram-012" style="font-weight:bold">Diagram 012</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_012.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_012.png" style="width:100%;height:100%;"></a>  
  


<div class="diagram" id="diagram-013"><a href="#diagram-013" style="font-weight:bold">Diagram 013</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_013.png" style="width:100%;height:100%;"></a>  
  


  
[Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/)