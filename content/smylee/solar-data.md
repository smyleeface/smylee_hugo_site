+++
title = "Solar Data"
date = "2016-07-02T18:00:00-07:00"
toc = false
draft = false
menu = true
+++

<div id="solardata" ng-app="solardata">
    <h2>Latest Output</h2>
    <div ng-controller="TodayCtrl">
    	<div class="todaydata">
	    <div class="todaydate">{{date}}</div> <div class="todaygenerate">{{generated}}</div>
	    </div>
	    <div class="footnote">Readings are updated daily at five minutes before noon, 6pm, and midnight PT.</div>
    </div>
    <br><br>
	<div ng-controller="DailyBarCtrl">
		<h2>Daily Generation for {{ dailyMonth }}</h2>
		<canvas id="bar" class="chart chart-bar" chart-data="data" chart-labels="labels" chart-series="series"></canvas>
	</div>
	<br><br>
	<div ng-controller="MonthlyBarCtrl">
    	<h2>Monthly Generation for {{ yearMonth }}</h2>
		<canvas id="bar" class="chart chart-bar" chart-data="data" chart-labels="labels" chart-series="series"></canvas>
	</div>
	<br><br>
    <div class="poweredby">Powered by&nbsp;&nbsp;<a href="http://enphase.com" target="_blank"><img src="http://cdn.smylee.com/images/20160702_solar/ENPH_logo_scr_RGB_API_sm.png" alt="Enphase Energy" class="no_border"></a></div>
    <div class="clear-all"></div>
</div>
<script type="text/javascript" src="/js/smylee/solar_angular.js"></script>