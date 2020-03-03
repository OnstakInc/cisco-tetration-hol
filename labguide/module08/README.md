# Cisco Tetration - Hands-On Lab

## Module08: Ingest Appliance - AWS VPC Flow Logs and ASA NAT Stitching

---


This diagram depicts the flow of traffic used by various devices to utimately ingest information into the Tetration cluster. The Tetration Edge appliance is used to subscribe to the pxGrid from ISE for SGT and user-based policy. The Tetration Data Ingest appliance is used to collect NetFlow v9 info from the ASAv which is useful in stitching together flows of traffic from outside the firewall all the way through being NAT'd by that ASAv and then traversing to the internal corporate network and making their way to app frontends. This same Tetration Data Ingest appliance is used to collect Flow Logs from an AWS VPC via an S3 bucket. This is useful for collecting traffic from any workload that may not have (or be able to have) a Tetration agent installed on it.

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_013.png" style="width:100%;height:100%;"></a>  



---

<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/08a_comissioning_tetration_edge_appliance.mp4" style="font-weight:bold" title="Data Ingest Appliance"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video showing the necessary tasks to comission the Tetration Data Ingest appliance to prepare for integration with ASA and AWS.</a>


<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/08b_tetration_edge_aws_flow_logs.mp4" style="font-weight:bold" title="AWS VPC Flow Logs"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video showing the necessary tasks to configure AWS VPC Flow Logs to be sent to the Tetration Data Ingest appliance and allow Tetration to see traffic in an AWS VPC other than that which has or speaks to a workload with a Tetration Agent.</a>


<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/08c_data_ingest_asav.mp4" style="font-weight:bold" title="ASAv NAT Flow Stiching"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video showing the necessary tasks to configure the ASAv to send NetFlow to the Tetration Data Ingest appliance and allow Tetration stich NAT'd flows together (note the appliance IPs in the video may differ based on env taken from).</a>

---  

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
<a href="#step-035" style="font-weight:bold">Step 035</a>  
<a href="#step-036" style="font-weight:bold">Step 036</a>  
<a href="#step-037" style="font-weight:bold">Step 037</a>  
<a href="#step-038" style="font-weight:bold">Step 038</a>  
<a href="#step-039" style="font-weight:bold">Step 039</a>  
<a href="#step-040" style="font-weight:bold">Step 040</a>  
<a href="#step-041" style="font-weight:bold">Step 041</a>  
<a href="#step-042" style="font-weight:bold">Step 042</a>  
<a href="#step-043" style="font-weight:bold">Step 043</a>  
<a href="#step-044" style="font-weight:bold">Step 044</a>  
<a href="#step-045" style="font-weight:bold">Step 045</a>  
<a href="#step-046" style="font-weight:bold">Step 046</a>  
<a href="#step-047" style="font-weight:bold">Step 047</a>  
<a href="#step-048" style="font-weight:bold">Step 048</a>  
<a href="#step-049" style="font-weight:bold">Step 049</a>  
<a href="#step-050" style="font-weight:bold">Step 050</a>  
<a href="#step-051" style="font-weight:bold">Step 051</a>  
<a href="#step-052" style="font-weight:bold">Step 052</a>  
<a href="#step-053" style="font-weight:bold">Step 053</a>  
<a href="#step-054" style="font-weight:bold">Step 054</a>  
<a href="#step-055" style="font-weight:bold">Step 055</a>  


<div class="step" id="step-001"><a href="#step-001" style="font-weight:bold">Step 001</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_001.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_001.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-002"><a href="#step-002" style="font-weight:bold">Step 002</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_002.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_002.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-003"><a href="#step-003" style="font-weight:bold">Step 003</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_003.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_003.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-004"><a href="#step-004" style="font-weight:bold">Step 004</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_004.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_004.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-005"><a href="#step-005" style="font-weight:bold">Step 005</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_005.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_005.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-006"><a href="#step-006" style="font-weight:bold">Step 006</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_006.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_006.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-007"><a href="#step-007" style="font-weight:bold">Step 007</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_007.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_007.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-008"><a href="#step-008" style="font-weight:bold">Step 008</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_008.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-009"><a href="#step-009" style="font-weight:bold">Step 009</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_009.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_009.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-010"><a href="#step-010" style="font-weight:bold">Step 010</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_010.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_010.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-011"><a href="#step-011" style="font-weight:bold">Step 011</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_011.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_011.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-012"><a href="#step-012" style="font-weight:bold">Step 012</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_012.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_012.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-013"><a href="#step-013" style="font-weight:bold">Step 013</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_013.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_013.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-014"><a href="#step-014" style="font-weight:bold">Step 014</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_014.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_014.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-015"><a href="#step-015" style="font-weight:bold">Step 015</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_015.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_015.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-016"><a href="#step-016" style="font-weight:bold">Step 016</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_016.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_016.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-017"><a href="#step-017" style="font-weight:bold">Step 017</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_017.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_017.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-018"><a href="#step-018" style="font-weight:bold">Step 018</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_018.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_018.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-019"><a href="#step-019" style="font-weight:bold">Step 019</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_019.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_019.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-020"><a href="#step-020" style="font-weight:bold">Step 020</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_020.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_020.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-021"><a href="#step-021" style="font-weight:bold">Step 021</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_021.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_021.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-022"><a href="#step-022" style="font-weight:bold">Step 022</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_022.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_022.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-023"><a href="#step-023" style="font-weight:bold">Step 023</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_023.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_023.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-024"><a href="#step-024" style="font-weight:bold">Step 024</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_024.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_024.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-025"><a href="#step-025" style="font-weight:bold">Step 025</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_025.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_025.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-026"><a href="#step-026" style="font-weight:bold">Step 026</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_026.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_026.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-027"><a href="#step-027" style="font-weight:bold">Step 027</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_027.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_027.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-028"><a href="#step-028" style="font-weight:bold">Step 028</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_028.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_028.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-029"><a href="#step-029" style="font-weight:bold">Step 029</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_029.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_029.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-030"><a href="#step-030" style="font-weight:bold">Step 030</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_030.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_030.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-031"><a href="#step-031" style="font-weight:bold">Step 031</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_031.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_031.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-032"><a href="#step-032" style="font-weight:bold">Step 032</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_032.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_032.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-033"><a href="#step-033" style="font-weight:bold">Step 033</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_033.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_033.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-034"><a href="#step-034" style="font-weight:bold">Step 034</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_034.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_034.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-035"><a href="#step-035" style="font-weight:bold">Step 035</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_035.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_035.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-036"><a href="#step-036" style="font-weight:bold">Step 036</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_036.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_036.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-037"><a href="#step-037" style="font-weight:bold">Step 037</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_037.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_037.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-038"><a href="#step-038" style="font-weight:bold">Step 038</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_038.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_038.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-039"><a href="#step-039" style="font-weight:bold">Step 039</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_039.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_039.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-040"><a href="#step-040" style="font-weight:bold">Step 040</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_040.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_040.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-041"><a href="#step-041" style="font-weight:bold">Step 041</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_041.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_041.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-042"><a href="#step-042" style="font-weight:bold">Step 042</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_042.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_042.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-043"><a href="#step-043" style="font-weight:bold">Step 043</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_043.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_043.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-044"><a href="#step-044" style="font-weight:bold">Step 044</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_044.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_044.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-045"><a href="#step-045" style="font-weight:bold">Step 045</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_045.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_045.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-046"><a href="#step-046" style="font-weight:bold">Step 046</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_046.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_046.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-047"><a href="#step-047" style="font-weight:bold">Step 047</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_047.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_047.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-048"><a href="#step-048" style="font-weight:bold">Step 048</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_048.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_048.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-049"><a href="#step-049" style="font-weight:bold">Step 049</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_049.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_049.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-050"><a href="#step-050" style="font-weight:bold">Step 050</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_050.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_050.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-051"><a href="#step-051" style="font-weight:bold">Step 051</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_051.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_051.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-052"><a href="#step-052" style="font-weight:bold">Step 052</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_052.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_052.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-053"><a href="#step-053" style="font-weight:bold">Step 053</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_053.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_053.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-054"><a href="#step-054" style="font-weight:bold">Step 054</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_054.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_054.png" style="width:100%;height:100%;"></a>  



<div class="step" id="step-055"><a href="#step-055" style="font-weight:bold">Step 055</a></div>  

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_055.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/images/module08_055.png" style="width:100%;height:100%;"></a>  





| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module08/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module09/) |
