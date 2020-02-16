# Cisco Tetration - Hands-On Lab

## Module02:  Collection Rules
In this module we will configure Collection Rules.  Collection Rules govern what endpoints will be considered for inclusion in inventory.  Typically this should be any internal IP address space of an organization.  It may also make sense to configure public IP address space that is used by an organization,  such as DMZ or public cloud address space.  

When configuring Collection rules, we must first delete the IPv6 and IPv4 rules that are configured by default in a new Tetration deployment. Then we can create our own specific rules to match the internal IP space. In the lab,  we'll assume the customer uses all RFC1918 private address space inside their organization.

Perform the following tasks to configure Collection Rules. <a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/01_collection_rules.mp4" title="Collection Rules Title">Click here</a> to view a video of the tasks being performed.  

### Steps for this Module  
<a href="#step-001" style="font-weight:bold">Step 001</a>  
<a href="#step-002" style="font-weight:bold">Step 002</a>  
<a href="#step-003" style="font-weight:bold">Step 003</a>  
<a href="#step-004" style="font-weight:bold">Step 004</a>  
<a href="#step-005" style="font-weight:bold">Step 005</a>  
<a href="#step-006" style="font-weight:bold">Step 006</a>  
<a href="#step-007" style="font-weight:bold">Step 007</a>  
<a href="#step-008" style="font-weight:bold">Step 008</a>  
<a href="#step-009" style="font-weight:bold">Step 009</a>  
<a href="#step-010" style="font-weight:bold">Step 010</a>  


<div class="step" id="step-001"><a href="#step-001" style="font-weight:bold">Step 001</a></div>
Click on the gear icon in the upper right hand corner and select Collection Rules.  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_001.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-002"><a href="#step-002" style="font-weight:bold">Step 002</a></div>
Click on Edit.  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_002.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_002.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-003"><a href="#step-003" style="font-weight:bold">Step 003</a></div>  
Click Delete to remove the default ::/0: IPv6 rule.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_003.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_003.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-004"><a href="#step-004" style="font-weight:bold">Step 004</a></div>  
Click Delete to remove the default 0.0.0.0/0 IPv4 rule.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_004.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_004.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-005"><a href="#step-005" style="font-weight:bold">Step 005</a></div>  
Enter ::/0: in the Subnet field,  select "Exclude traffic" and then Add Rule.


<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_005.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_005.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-006"><a href="#step-006" style="font-weight:bold">Step 006</a></div>  
Enter 0.0.0.0/0 in the Subnet field, Select "Exclude traffic" and then Add Rule.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_006.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_006.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-007"><a href="#step-007" style="font-weight:bold">Step 007</a></div>  
Enter 10.0.0.0/8 in the Subnet field,  Select "include traffic" and then Add Rule.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_007.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_007.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-008"><a href="#step-008" style="font-weight:bold">Step 008</a></div>  
Enter 172.16.0.0/12 in the Subnet field,  Select "include traffic" and then Add Rule.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_008.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-009"><a href="#step-009" style="font-weight:bold">Step 009</a></div>  
Enter 192.168.0.0/16 in the Subnet field,  Select "include traffic" and then Add Rule.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_009.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_009.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-010"><a href="#step-010" style="font-weight:bold">Step 010</a></div>  
Below is what the ruleset should look like when finished.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_010.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module02/images/module02_010.png" style="width:100%;height:100%;"></a>  




[Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/)
