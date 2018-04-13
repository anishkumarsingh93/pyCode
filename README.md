# pyCode
Playing around with Python 2.7

Anish : Here we'll learn, use and explore the various python libraries.


Settlement
Monitoring Report 
•	Rank order break at node level for all the segment is showing no result.
•	AAD for all segment is showing no result.
•	Total observation % is 99.99% for reference and 100.01% for validation in SPI tab.
•	SPI value is negative.Executive summary SPI trend not coming

Monitor Model
•	AAD results are not aligned with MRD.
•	Total observation % is 99.99% for reference and 100.01% for validation in SPI tab.
Dashboard Numbers not matching with Monitoring report
The support for negative target rate might be the problem.
monitoring Report:There is Nan in target count of UI in reference and validation.





Recovery Segmentation
•	KPI trends are not getting populated in Excel report from Smart 
•	SPI calculation is not available in Excel report from Smart
•	
•	Sep’17 vintage is not available for PSI in dashboard & monitoring report.This is because PSI most recent is not being calculated right now.
AAD is slightly different in Monitor Model
In Dashboard nothing comes in second last page Time:3:57pm 4/12/2018
Monitoring Report, Segment Level data is not populated for ROB and AAD



Late Stage Segmentation
In Monitoring Report Tab:
•	Mismatch in Target Count and Target Rate with MRD. #Dev simulation
•	In Volume trend overall number is doubled in size due to addition of nodes and overall number.
•	Target rate trend is not correct #Dev simulation
•	SPI trend is also wrong.
•	Reference PSI mark is there in PSI trend, which should number of some quarter.#This is OOT
•	AAD is reaching 100% mark, which is wrong and the trend is also wrong.#Data will be reuploaded

In Monitor Model Tab:
•	AAD at both Segment and Node level is wrong due to wrong validation No
•	SPI Mismatch: 0.47 in MRD, 1.23 in SMART
•	PSI on Most recent vintage validation is 0 , which is wrong.

Dev SPI will be wrong due to simulation of dev data leading to wrong overall target rate





Bucket_1_Segmentation
Model Monitoring:
1.	If the 3segments be 1 should the %population be 0 or 100%? In this case it is displayed as 0%.
2.	What are the numbers mentioned as target count?
3.	Reference total observations is being counted as sum of population in both nodes and segments by the tool.
4.	Overall volumes reported in executive summary tab is wrong(double counted)
5.	SPI reported for segment level cannot be verified.
6.	Trends for AAD at both node and segment level  in tool see quite a large deviation from ones reported in MRD. (The trend changes in node level for 2015Q3 and whereas the trend is maintained in seg level but deviations are large) in 
7.	Trend for ROB at node level is wrong.
8.	Dashboard has no allowance to select multiple vintages. Hence values are non comparable.
9.	Target definition missing in excel report.
10.	The excel export button(3rd button) causes a window to open and hang up.
AAD and ROB is empty in Tool UI at segement level . Switching to and back gives error. Time: 3:43pm 4/12/2018

The dev data is simulated from MRD. Overall Target rate wont match


New Ask:

Node level results in Dashboard

Overall:
Cant download the inner page excel reports
