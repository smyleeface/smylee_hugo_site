
var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var today = new Date();

var app = angular.module('solardata', ["chart.js"]);

app.service('SolarService', function($http, $q){
	this.get = function(getType, filter){
		var deferred = $q.defer();

		//create the querystring
		var qs = '?getType='+getType;
		if (filter.length != 0) {
			qs += '&filter='+filter
		}

		//call api gateway to get dynamodb solar data
		$http({
			url : 'https://lthv8ocvtl.execute-api.us-west-2.amazonaws.com/smylee_com_prod/solardata'+qs
		})
		.then(function successCallback(response) {
			return deferred.resolve(response.data);
		}, function errorCallback(response) {
			return deferred.reject(err);
		});

		return deferred.promise;
	};
});

app.controller('ListCtrl', function($scope, SolarService) {
	'use strict';
	SolarService.get('all').then(function(rdata){
	  	var data = JSON.parse(rdata);
	    $scope.years = [];
	    angular.forEach(data.years, function(year, index) {
	      $scope.years.push(year);
	    });
	});
});

app.controller("MonthlyBarCtrl", function ($scope, SolarService) {

	dateStr = today.getFullYear()

	$scope.yearMonth = dateStr

	SolarService.get('month', dateStr).then(function(rdata){
	  	var data = JSON.parse(rdata);
	    $scope.labels = [];
	    $scope.data = [];
    	angular.forEach(data, function(month, index) {
    		// console.log(month.date);
      		$scope.labels.push(month.date);
      		$scope.data.push(month.generated);
   		});

	});
});

app.controller("DailyBarCtrl", function ($scope, SolarService) {

	todayTimeStamp = date.setHours(date.getHours(),date.getMinutes());
	noonTimeStamp = date.setHours(11,55);
	getYear = date.getFullYear();

	if (todayTimeStamp < noonTimeStamp) {
		//use the previous day if it hasn't hit noon yet
		yesterday = new Date();
		yesterday.setDate(date.getDate() - 1);
		getMonth = ('0' + (yesterday.getMonth()+1)).slice(-2);
		dailyMonth = monthNames[date.getMonth()]+' '+getYear
	}
	else {
		//use today, it's past noon
		getMonth = ('0' + (date.getMonth()+1)).slice(-2);
		dailyMonth = monthNames[date.getMonth()]+' '+getYear
	}

	dateStr = getYear+'-'+getMonth;

	$scope.dailyMonth = dailyMonth;

	SolarService.get('day', dateStr).then(function(rdata){
	  	var data = JSON.parse(rdata);
	    $scope.labels = [];
	    $scope.data = [];
    	angular.forEach(data, function(day, index) {
    		// console.log(day.date);
      		$scope.labels.push(day.date);
      		$scope.data.push(day.generated);
   		});
		});
});

app.controller("TodayCtrl", function ($scope, SolarService) {

	todayTimeStamp = today.setHours(today.getHours(),today.getMinutes());
	getYear = today.getFullYear();

	date = new Date();
	noonTimeStamp = date.setHours(11,55);

	if (todayTimeStamp < noonTimeStamp) {
		//use the previous day if it hasn't hit noon yet
		yesterday = new Date();
		yesterday.setDate(today.getDate() - 1);
		getMonth = ('0' + (yesterday.getMonth()+1)).slice(-2);
		getDay = ('0' + (yesterday.getDate())).slice(-2);
		todayDate = monthNames[yesterday.getMonth()]+' '+yesterday.getDate()+', '+getYear
	}
	else {
		//use today, it's past noon
		getMonth = ('0' + (today.getMonth()+1)).slice(-2);
		getDay = ('0' + (today.getDate())).slice(-2);
		todayDate = monthNames[today.getMonth()]+' '+today.getDate()+', '+getYear
	}

	dateStr = getYear+'-'+getMonth+'-'+getDay;

	$scope.date = todayDate

	SolarService.get('day', dateStr).then(function(rdata){
	  	var data = JSON.parse(rdata);
		$scope.generated = data[0].generated + ' kWh'
	});
});