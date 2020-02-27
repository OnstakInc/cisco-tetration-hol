# Cisco Tetration - Hands-On Lab
  
## Module01: Introduction

This lab guide has been developed in close coordination with the Cisco Tetration product team in order to provide you, the learner, with a complete experience of deploying, configuring, and truly getting the most out of Cisco Tetration. 

Cisco Tetration is a powerful tool that allows organizations to easily define and maintain centralized, intent-driven policy, made possible by collecting advanced telemetry with complete visibility of every packet, action, and process happening across every single workload, regardless of floor tile. Whether your workloads live in your own data centers, someone elses such as a CoLo or even public cloud provider, or any combination thereof, Cisco Tetration has you covered. 

### Structure and Layout of this Lab Guide

This lab is structured in a way that allows the learner to follow along a consistent path on the journey of designing and configuring Cisco Tetration to an effective working state. Throughout this guide, each module will begin with a video that walks through every task that the learner will accomplish. Following the video, screenshots along with instructions will highlight the important steps that the learner is intended to perform. It is important to note that while the screens should appear quite consistent with what the learner will experience in their own environment, the *values* input into those screens, such as IP addresses and even perhaps AWS regions may (and will likely, though not always) be quite different than those seen in the videos and accompanying screenshots. While hostnames are not always usually very important in this lab, for the most part they should remain the same, with the possible exception of ISE. 

> NOTE: Values such as IP addresses **WILL** be different from student to student, and the learner **MUST** always refer to their own CSV or Excel spreadsheet for any IP addressing, public URLs, unique AWS credentials (Access & Secret keys), EKS cluster endpoints, etc. 

Every student will be provided with an Excel or CSV file and is encouraged open a browser window to our choice here for an [online CSV/Excel viewer](https://sheet.zoho.com/sheet/excelviewer), drop your CSV/XLS file there, and continue to reference that file throughout your interaction with this lab environment, as seen here in the short video below.


<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module01/images/module01_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_001.png" style="width:50%;height:50%;"></a>  


<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/01a_online_csv_viewer.mp4" style="font-weight:bold"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video of interaction with the student CSV and online viewer.</a>



PASSWORDS
`tet123$$!`

GUAC


<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/01b_guac_user_access.mp4" style="font-weight:bold"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video of interaction with the student Guacamole webUI console.</a>


### Integrations with Tetration

Included in this lab are multiple integrations with Tetration, including:

* Cisco Identity Services Engine (ISE) for user-based authentication with TrustSec SGTs
* Cisco ASAv Firewall with NAT Flow Stiching
* Windows Active Directory LDAP (currently via Tet Edge & ISE)
* AWS VPC Flow Logs (for visibility outside of agent communication)
* AWS Tags (for dynamic VM-based policy)
* Kubernetes Labels (for dynamic container-based policy)

### Lab Environment

The lab environment accompanying this lab guide lives entirely in the cloud. This starts with the Cisco Tetration product itself which is a SaaS product - referred to throughout this lab guide as "TaaS" or "Tetration as a Service". As for the Windows, Linux, and Container-based applications and workloads that make them up, the end-user simulated machines, the ASA firewall that separates the simulated Internet from the simulated corporate environment, the Tetration appliances, and even the web-based proxy that gives you access to the whole thing - that all lives in the public cloud, as well. This was chosen as the most scalable and predictable way to allow this lab to be redistributed freely and ensure that the exact same experience was had by every learner, regardless of where in the world you happened to be. 

Every learner working with this Lab Guide has a __*complete*__ lab evironment for themselves. 

This consists of every item seen in the following diagram, which is enumerated in more detail below the diagram. The diagram below actually links to a live, interactive diagram that you may like to use throughout your lab experience, [which you can read more about here on the diagrams page](https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/). There will also be more diagrams used throughout this lab guide, and they will all correspond with the Diagram ### found on that diagrams page. 

<div class="diagram" id="diagram-003"><a href="#diagram-003" style="font-weight:bold">Diagram 003</a></div>   
<a href="https://www.lucidchart.com/documents/view/425e1b97-194e-413a-b793-0df939a87501" target="_blank"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_003.png" style="width:100%;height:100%;"></a>  

Your complete lab environment consists of the following assets:

##### "Internal/Corporate" Subnet (inside firewall)

###### Apps
   * Windows app - "nopCommerce" 
      * IIS App server (Win19)
      * MS SQL DB server (Win19)
   * Linux app - "OpenCart" 
      * Apache App server (CentOS 7)
      * MySQL DB server (CentOS 7)
   * Container-based app on Kubernetes (microservices) - "Sock Shop"
      * AWS Elastic Load Balancer
      * AWS EKS Master Node
      * AWS EKS Worker Node (Ubuntu 16.04)
        * Containers/Services
          * Front End service
          * Payment service
          * Shipping service
          * Queuemaster service
          * RabbitMQ service
          * Orders service
            * Orders App
            * Orders DB
          * User service
            * User App
            * User DB
          * Catalog service
            * Catalog App
            * Catalog DB
          * Carts service
            * Carts App
            * Carts DB

###### LDAP
   * Active Directory (Win19)

###### Automation
   * Ansible (CentOS 7)

###### Tetration Appliances
   * Tetration Data Ingest (AWS VPC Flow Logs & ASAv NAT Stiching)
   * Tetration Edge (ISE TrustSec SGT to Active Directory user mapping)


##### "External/Internet" Subnet (outside firewall)

###### End Users (on internet outside firewall)
   * Employee (Win10 or Ubuntu18 Desktop)
   * SysAdmin (Win10 or Ubuntu18 Desktop)


##### Straddling Internal Corporate & External Internet Subnets

###### Firewall / VPN
   * ASAv

###### Lab Environment Access
   * Apache Guacamole server (CentOS 7)







  

| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module01/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/) |