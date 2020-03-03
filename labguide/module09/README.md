# Cisco Tetration - Hands-On Lab

## Module09: Edge Appliance - ISE

---

This diagram depicts the flow of traffic used by various devices to utimately ingest information into the Tetration cluster. The Tetration Edge appliance is used to subscribe to the pxGrid from ISE for SGT and user-based policy. The Tetration Data Ingest appliance is used to collect NetFlow v9 info from the ASAv which is useful in stitching together flows of traffic from outside the firewall all the way through being NAT'd by that ASAv and then traversing to the internal corporate network and making their way to app frontends. This same Tetration Data Ingest appliance is used to collect Flow Logs from an AWS VPC via an S3 bucket. This is useful for collecting traffic from any workload that may not have (or be able to have) a Tetration agent installed on it.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_013.png" style="width:100%;height:100%;"></a>  

---

<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/09a_comissioning_tetration_edge_appliance.mp4" style="font-weight:bold" title="Data Ingest Appliance and ASAv NAT Flow Stiching"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png">Click here to view a video showing the necessary tasks to comission the Tetration Edge appliance to prepare for integration with Cisco ISE (note this is similar to data ingest with nuanced differences).</a>

<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/09b_ise_integration.mp4" style="font-weight:bold" title="Data Ingest Appliance and ASAv NAT Flow Stiching"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video showing the necessary tasks to integrate Cisco ISE with Tetration to prepare to support user-based policy in Module 16.</a>



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
<a href="#step-019" style="font-weight:bold">Step 019</a>  
<a href="#step-020" style="font-weight:bold">Step 020</a>  
<a href="#step-021" style="font-weight:bold">Step 021</a>  
<a href="#step-022" style="font-weight:bold">Step 022</a>  
<a href="#step-023" style="font-weight:bold">Step 023</a>  
<a href="#step-024" style="font-weight:bold">Step 024</a>  
<a href="#step-025" style="font-weight:bold">Step 025</a>  
<a href="#step-026" style="font-weight:bold">Step 026</a>  
<a href="#step-027" style="font-weight:bold">Step 027</a>  
<a href="#step-028" style="font-weight:bold">Step 028</a>  
<a href="#step-029" style="font-weight:bold">Step 029</a>  
<a href="#step-030" style="font-weight:bold">Step 030</a>  
<a href="#step-031" style="font-weight:bold">Step 031</a>  
<a href="#step-032" style="font-weight:bold">Step 032</a>  
<a href="#step-033" style="font-weight:bold">Step 033</a>  
<a href="#step-034" style="font-weight:bold">Step 034</a>  


<div class="step" id="step-001"><a href="#step-001" style="font-weight:bold">Step 001</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_001.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-002"><a href="#step-002" style="font-weight:bold">Step 002</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_002.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_002.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-003"><a href="#step-003" style="font-weight:bold">Step 003</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_003.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_003.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-004"><a href="#step-004" style="font-weight:bold">Step 004</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_004.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_004.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-005"><a href="#step-005" style="font-weight:bold">Step 005</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_005.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_005.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-006"><a href="#step-006" style="font-weight:bold">Step 006</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_006.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_006.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-007"><a href="#step-007" style="font-weight:bold">Step 007</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_007.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_007.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-008"><a href="#step-008" style="font-weight:bold">Step 008</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_008.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-009"><a href="#step-009" style="font-weight:bold">Step 009</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_009.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_009.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-010"><a href="#step-010" style="font-weight:bold">Step 010</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_010.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_010.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-011"><a href="#step-011" style="font-weight:bold">Step 011</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_011.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_011.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-012"><a href="#step-012" style="font-weight:bold">Step 012</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_012.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_012.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-013"><a href="#step-013" style="font-weight:bold">Step 013</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_013.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-014"><a href="#step-014" style="font-weight:bold">Step 014</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_014.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_014.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-015"><a href="#step-015" style="font-weight:bold">Step 015</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_015.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_015.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-016"><a href="#step-016" style="font-weight:bold">Step 016</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_016.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_016.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-017"><a href="#step-017" style="font-weight:bold">Step 017</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_017.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_017.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-018"><a href="#step-018" style="font-weight:bold">Step 018</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_018.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_018.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-019"><a href="#step-019" style="font-weight:bold">Step 019</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_019.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_019.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-020"><a href="#step-020" style="font-weight:bold">Step 020</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_020.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_020.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-021"><a href="#step-021" style="font-weight:bold">Step 021</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_021.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_021.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-022"><a href="#step-022" style="font-weight:bold">Step 022</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_022.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_022.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-023"><a href="#step-023" style="font-weight:bold">Step 023</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_023.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_023.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-024"><a href="#step-024" style="font-weight:bold">Step 024</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_024.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_024.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-025"><a href="#step-025" style="font-weight:bold">Step 025</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_025.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_025.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-026"><a href="#step-026" style="font-weight:bold">Step 026</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_026.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_026.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-027"><a href="#step-027" style="font-weight:bold">Step 027</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_027.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_027.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-028"><a href="#step-028" style="font-weight:bold">Step 028</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_028.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_028.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-029"><a href="#step-029" style="font-weight:bold">Step 029</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_029.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_029.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-030"><a href="#step-030" style="font-weight:bold">Step 030</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_030.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_030.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-031"><a href="#step-031" style="font-weight:bold">Step 031</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_031.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_031.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-032"><a href="#step-032" style="font-weight:bold">Step 032</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_032.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_032.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-033"><a href="#step-033" style="font-weight:bold">Step 033</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_033.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_033.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-034"><a href="#step-034" style="font-weight:bold">Step 034</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_034.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/images/module09_034.png" style="width:100%;height:100%;"></a>  





| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module10/) |
