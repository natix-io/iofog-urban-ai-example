<template>
    <div>
        <!-- Dropdown Trigger -->
        <a class='dropdown-trigger btn' href='#' id="edge-device-select-dropdown" data-target='dropdown1'>Select An Edge</a>
        <!-- Dropdown Structure -->
        <ul id='dropdown1' class='dropdown-content'>
            <li v-on:click="pickDevice('cam1')">cam1</li>
        </ul>
  </div>      
</template>

<script>
import M from 'materialize-css';
import axios from 'axios'
export default {
    name: 'EdgeDeviceSelectDropDown',
    data(){
        return { intervalJob: {} }
    },
    mounted(){      
              var elems = document.querySelectorAll('.dropdown-trigger');
              M.Dropdown.init(elems, null);
              console.log('address is in next line');
              console.log(process.env.VUE_APP_ANOMALY_REPORT_API);
            },
    methods: {
        pickDevice(name) {
            window.JQuery('#edge-device-select-dropdown').html(''+name);
                const options = {
                  method: 'get',
                  url: process.env.VUE_APP_ANOMALY_REPORT_API,
                  headers: {'Content-Type':'application/json'},
                  transformResponse: [(data) => {     return JSON.parse(data); }]
                }; 
                axios(options).then(response => {  this.$emit("SelectedDeviceUpdated",this.selectedDevice,response.data.usage_data,response.data.anomaly_value,response.data.anomaly_step);      });
    }       

  }
}
</script>
