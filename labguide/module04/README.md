# Cisco Tetration - Hands-On Lab

## Module04 - Agent Config Intent
Agent Config Intent defines what features will be enabled for a group of sensors.  The Config Intent can be tied to an Inventory Filter, which provides the capability to apply different configurations to different types of hosts.  For example, you could define a profile enabling a specific set of features to all Windows machines,  and a separate profile enabling a different set of features to all Linux machines.  We will see an example of doing just that in the exercise below.  

In most cases these settings can all be enabled,  however the following should be taken into consideration:
- Enforcement - This agent config intent setting provides the capability to enable/disable the enforcement feature.  This can be useful to prevent a situation where you have a set of machines that you would like to ensure cannot be put into enforcement inadvertently.   

- Auto-Upgrade - If this feature is left in the default enabled state,  then agents will be upgraded automatically when Tetration code is updated.  It is common to disable this feature so that agents can be upgraded in a more controlled manner.  

- Preserve Rules - When enabled,  this setting will preserve any manually configured firewall rules that might be present on the servers when going into enforcement.  It is common to set this to enabled, such as to preserve any rules that might have been previously configured.

<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/02_agent_config.mp4" style="font-weight:bold" title="Agent Config Intent">Click here to view a video of the tasks necessary to configure Tetration Agents for Windows and Linux machines.</a>

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


<div class="step" id="step-001"><a href="#step-001" style="font-weight:bold">Step 001</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_001.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-002"><a href="#step-002" style="font-weight:bold">Step 002</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_002.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_002.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-003"><a href="#step-003" style="font-weight:bold">Step 003</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_003.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_003.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-004"><a href="#step-004" style="font-weight:bold">Step 004</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_004.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_004.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-005"><a href="#step-005" style="font-weight:bold">Step 005</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_005.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_005.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-006"><a href="#step-006" style="font-weight:bold">Step 006</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_006.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_006.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-007"><a href="#step-007" style="font-weight:bold">Step 007</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_007.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_007.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-008"><a href="#step-008" style="font-weight:bold">Step 008</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_008.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-009"><a href="#step-009" style="font-weight:bold">Step 009</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_009.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_009.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-010"><a href="#step-010" style="font-weight:bold">Step 010</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_010.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_010.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-011"><a href="#step-011" style="font-weight:bold">Step 011</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_011.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_011.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-012"><a href="#step-012" style="font-weight:bold">Step 012</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_012.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_012.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-013"><a href="#step-013" style="font-weight:bold">Step 013</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_013.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-014"><a href="#step-014" style="font-weight:bold">Step 014</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_014.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_014.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-015"><a href="#step-015" style="font-weight:bold">Step 015</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_015.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/images/module04_015.png" style="width:100%;height:100%;"></a>  





| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module04/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/) |
