# Cisco Tetration - Hands-On Lab

## Module03 - Sensor Installation
Tetration sensor installation can be performed manually using a shell script for Linux and a Powershell script (.ps1) for Windows. These scripts can also be leveraged by 3rd party software configuration management systems such as Ansible, Puppet, Microsoft SCCM, etc. to automate deployment across multiple machines.  The installation does not require any modification to run unattended, the scripts run without any interaction required from the administrator. It is important that the scripts be downloaded from the Tetration cluster, as they have specific information embedded to connect to the cluster.  When the script is executed, it will pull down the required software from the Tetration cluster based on the Operating System in use. This means that outbound connectivity from each server to the Tetration cluster is a requirement.

In this module, we'll download the installation scripts for Windows and Linux from the Tetration cluster and use Ansible to perform automated rollout of the sensors.

<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/03_agent_installation.mp4" style="font-weight:bold" title="Collection Rules Title"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video of the tasks being performed to install Tetration sensors.</a>  

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
<a href="#step-011" style="font-weight:bold">Step 011</a>  
<a href="#step-012" style="font-weight:bold">Step 012</a>  
<a href="#step-013" style="font-weight:bold">Step 013</a>  
<a href="#step-014" style="font-weight:bold">Step 014</a>  
<a href="#step-015" style="font-weight:bold">Step 015</a>  
<a href="#step-016" style="font-weight:bold">Step 016</a>  
<a href="#step-017" style="font-weight:bold">Step 017</a>  
<a href="#step-018" style="font-weight:bold">Step 018</a>  


<div class="step" id="step-001"><a href="#step-001" style="font-weight:bold">Step 001</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_001.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-002"><a href="#step-002" style="font-weight:bold">Step 002</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_002.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_002.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-003"><a href="#step-003" style="font-weight:bold">Step 003</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_003.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_003.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-004"><a href="#step-004" style="font-weight:bold">Step 004</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_004.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_004.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-005"><a href="#step-005" style="font-weight:bold">Step 005</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_005.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_005.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-006"><a href="#step-006" style="font-weight:bold">Step 006</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_006.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_006.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-007"><a href="#step-007" style="font-weight:bold">Step 007</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_007.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_007.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-008"><a href="#step-008" style="font-weight:bold">Step 008</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_008.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-009"><a href="#step-009" style="font-weight:bold">Step 009</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_009.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_009.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-010"><a href="#step-010" style="font-weight:bold">Step 010</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_010.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_010.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-011"><a href="#step-011" style="font-weight:bold">Step 011</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_011.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_011.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-012"><a href="#step-012" style="font-weight:bold">Step 012</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_012.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_012.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-013"><a href="#step-013" style="font-weight:bold">Step 013</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_013.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-014"><a href="#step-014" style="font-weight:bold">Step 014</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_014.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_014.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-015"><a href="#step-015" style="font-weight:bold">Step 015</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_015.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_015.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-016"><a href="#step-016" style="font-weight:bold">Step 016</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_016.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_016.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-017"><a href="#step-017" style="font-weight:bold">Step 017</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_017.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_017.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-018"><a href="#step-018" style="font-weight:bold">Step 018</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_018.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/images/module03_018.png" style="width:100%;height:100%;"></a>  





| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module03/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/) |
