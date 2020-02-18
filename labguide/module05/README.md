# Cisco Tetration - Hands-On Lab

## Module05 - Annotations
Annotations are metadata that can be associated with endpoint IP addresses that are stored in Tetration inventory. Traditionally, IP addresses and/or hostnames of devices have been the primary means of identifying devices in an environment. Annotations provide a mechanism by which we can provide more context about the IP addresses, and build search criteria and policy within the platform using language that is much more consumable and meaningful to humans. Each IP address can be annotated with up to 32 fields of metadata.  With annotations we can build policy that is dynamic; by changing an annotation we can potentially affect the policy that is being applied to a particular machine.  Take for an example a machine that has been identified by the security team as running a highly vulnerable version of software.  By creating a policy that matches an annotation of "Quarantine",  we can annotate the workload with the "Quarantine" annotation to cause it to be removed from the network so that the vulnerability can be patched.

In this module,  we'll configure Static Annotations for the endpoints in the lab environment.  Static Annotations are manually configured by the Tetration administrator by uploading a .CSV file,  or alternatively by configuring one at a time using the Assign Annotations wizard from the Inventory Upload screen.  Annotations can also be populated from external sources,  such as tags in VMware and AWS.  External annotations will be covered in <a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module07/">Module 07 - External Orchestrators</a>.


<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/03_static_annotations.mp4" style="font-weight:bold" title="Collection Rules Title">Click here to view the first of two videos highlighting the creation of static Annotations.</a>
</br></br>
<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/04_verify_static_annotations.mp4" style="font-weight:bold" title="Collection Rules Title">Click here to view the second of two videos highlighting the verification of those Annotations.</a>

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


<div class="step" id="step-001"><a href="#step-001" style="font-weight:bold">Step 001</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_001.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-002"><a href="#step-002" style="font-weight:bold">Step 002</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_002.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_002.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-003"><a href="#step-003" style="font-weight:bold">Step 003</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_003.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_003.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-004"><a href="#step-004" style="font-weight:bold">Step 004</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_004.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_004.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-005"><a href="#step-005" style="font-weight:bold">Step 005</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_005.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_005.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-006"><a href="#step-006" style="font-weight:bold">Step 006</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_006.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_006.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-007"><a href="#step-007" style="font-weight:bold">Step 007</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_007.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_007.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-008"><a href="#step-008" style="font-weight:bold">Step 008</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_008.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-009"><a href="#step-009" style="font-weight:bold">Step 009</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_009.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_009.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-010"><a href="#step-010" style="font-weight:bold">Step 010</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_010.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_010.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-011"><a href="#step-011" style="font-weight:bold">Step 011</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_011.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_011.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-012"><a href="#step-012" style="font-weight:bold">Step 012</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_012.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_012.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-013"><a href="#step-013" style="font-weight:bold">Step 013</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/images/module05_013.png" style="width:100%;height:100%;"></a>  





| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module05/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module06/) |
