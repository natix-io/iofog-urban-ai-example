<template>
<div>
  <div class="row">
    <div class="col s9"></div>
    <div class="col s3">
      <EdgeDeviceSelectDropDown v-on:SelectedDeviceUpdated="showSelected"></EdgeDeviceSelectDropDown>
    </div>
  </div>
  <div class="row">
    <div class="col s2"></div>
    <div class="col s8">
      <div class="card white darken-1">
        <div class="card-content ">
          <span class="card-title">{{ selectedDevice }}</span>
          <VueApexCharts type="area" height="350" :options="chartOptions" :series="series"></VueApexCharts>
        </div>
        </div>
    </div>
    <div class="col s2"></div>
  </div>
</div>  
</template>

<script>
import EdgeDeviceSelectDropDown from './components/EdgeDeviceSelectDropDown'
import VueApexCharts from 'vue-apexcharts'
import ApexCharts from 'apexcharts'
export default {
  name: 'App',
  data() { 
    return {
    selectedDevice: ''
    }
  },
  components: {
    EdgeDeviceSelectDropDown,
    VueApexCharts
  },
  methods: {
    showSelected(name,dataSeries,anomalyVal,anomalyTime){
      this.selectedDevice = name;
       var anomalyArray = new Array(30).fill(0);
       anomalyArray[anomalyTime]= anomalyVal;
       ApexCharts.exec("chart1", "updateOptions", {xaxis: {categories:["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]}});
       ApexCharts.exec("chart1", "updateSeries",  [ {name: name,  data: dataSeries}, {name: 'anomaly',data: anomalyArray} ]);
    }
  },
  computed: {
    series() {
        return [
          {
            name: "No Data",
            data: []
          }
        ];
      },
    chartOptions(){
        return {
            chart: {
              id: "chart1",
              height: 350,
              type: 'area'
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'smooth'
            },
            xaxis: {
              type: 'text',
              categories: ["2"]
            }
      };}
  }

}
</script>

<style>

</style>
