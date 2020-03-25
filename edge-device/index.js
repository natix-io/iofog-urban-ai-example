const iofog = require('@iofog/nodejs-sdk');
let config = null;

function updateConfig() {
    iofog.getConfig({
      onNewConfig: newConfig => {
        config = newConfig;
      },
      onBadRequest: err => console.error('updateConfig failed: ', err),
      onError: err => console.error('updateConfig failed: ', err)
    });
  }

function main() {
    updateConfig();
    iofog.wsControlConnection({
        onNewConfigSignal: () => {  updateConfig();  },
        onError: err => console.error('Error with Control Connection: ', err)
    });

    const onMessageConnectionOpen = () => {
        console.log('Listening for incoming messages');
    };

    
  iofog.wsMessageConnection(onMessageConnectionOpen, {
      
    onMessages: messages => {
      if (messages) {
        console.log(messages);
      }
    },
    onMessageReceipt: (messageId, timestamp) => {
      console.log('message receipt: ', {
        messageId,
        timestamp
      });
    },
    onError: (err) => {console.error('Message WebSocket error: ', err); clearInterval(intervalObj);}
  });

  const intervalObj = setInterval(()=> {submitLastTimeWindowPowerUsage();},5000);
}

function submitLastTimeWindowPowerUsage(){
    var timeWindow = new Array(30).fill(null);
    for (i=0;i<30;i++){
      //generate normal data
      timeWindow[i]=getRandomValueBetween(config.minUsage,config.maxUsage);
    }

    //generate anomalous datum
    validationData = timeWindow;

    validationData[Math.floor(getRandomValueBetween(1, 29))]=getRandomValueBetween((config.minUsage)*4,(config.maxUsage)*4);
    var ioMsg = iofog.ioMessage({'tag': config.tag ,'groupid':'E455','contentdata':  JSON.stringify({train_data: timeWindow,validation_data: validationData})});
    iofog.wsSendMessage(ioMsg);
}

function getRandomValueBetween(min, max) {
    return Math.random() * (max - min )  + min;
}

iofog.init('iofog', 54321, null, main);
