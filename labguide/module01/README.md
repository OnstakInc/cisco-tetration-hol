# Cisco Tetration - Hands-On Lab
  
## Module01: Introduction

This lab guide has been developed in close coordination with the Cisco Tetration product team in order to provide you, the learner, with a complete experience of deploying, configuring, and truly getting the most out of Cisco Tetration. 

Cisco Tetration is a powerful tool that allows organizations to easily define and maintain centralized, intent-driven policy, made possible by collecting advanced telemetry with complete visibility of every packet, action, and process happening across every single workload, regardless of floor tile. Whether your workloads live in your own data centers, someone elses such as a CoLo or even public cloud provider, or any combination thereof, Cisco Tetration has you covered. 

### Structure and Layout of this Lab Guide

This lab is structured in a way that allows the learner to follow along 

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
   * Employee (Win10)
   * SysAdmin (Win10)


##### Straddling Internal Corporate & External Internet Subnets

###### Firewall / VPN
   * ASAv

###### Lab Environment Access
   * Apache Guacamole server (CentOS 7)





### Steps for this Module  



  

| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module01/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/) |