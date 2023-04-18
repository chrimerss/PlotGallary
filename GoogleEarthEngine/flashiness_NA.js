// Create a panel to hold the radio buttons
var panel = ui.Panel({style: {width: '300px', position: 'bottom-left'}});
var fvLayer = ui.Map.FeatureViewLayer(
  'users/chrimerss/NAflashiness');
  
// Radio buttons for duration
var selectedDuration = '1';
var selectedFrequency = '2';

function displayFlashiness(frequency,duration) {
  var property=selectedFrequency + 'yr-' + selectedDuration + 'hr';
  var visParams = {
  lineWidth: 2,
  color: {
    property: property,
    mode: 'linear',
    palette: palette,
    min: 1,
    max: 9
  }
};
fvLayer.setVisParams(visParams);
fvLayer.setName('Flashiness '+ selectedFrequency + '-yr ' + selectedDuration + '-hr');
Map.add(fvLayer);

}


var panel = ui.Panel({style: {width: '200px', position: 'bottom-left'}});

var selectedDuration = '1';
var selectedFrequency = '2';

panel.add(ui.Label('Duration:'));
var durationSelect = ui.Select({
  items: ['1', '2', '3', '4', '5', '6'],
  value: selectedDuration,
  onChange: function(value) {
    Map.remove(fvLayer)
    selectedDuration = value;
    displayFlashiness(selectedDuration, selectedFrequency);
  },
});
panel.add(durationSelect);

panel.add(ui.Label('Frequency:'));
var frequencySelect = ui.Select({
  items: ['2', '5', '10'],
  value: selectedFrequency,
  onChange: function(value) {
    selectedFrequency = value;
    Map.remove(fvLayer)
    displayFlashiness(selectedDuration, selectedFrequency);
  },
});
panel.add(frequencySelect);

Map.add(panel);



var palettes = require('users/gena/packages:palettes');

var palette = palettes.colorbrewer.YlOrBr[9];


displayFlashiness(selectedFrequency, selectedDuration)


Map.setCenter(-90, 40, 5);
Map.setOptions('HYBRID');

// Function to create a legend item
function createColorbar(palette, width, height) {
  var colorbar = ui.Panel({
    layout: ui.Panel.Layout.flow('horizontal'),
    style: {width: width + 'px', height: height + 'px'}
  });

  var colorCount = palette.length;

  for (var i = 0; i < colorCount; i++) {
    colorbar.add(ui.Label({
      value: '',
      style: {
        backgroundColor: palette[i],
        width: (100 / colorCount) + '%',
        height: '100%',
        margin: '0px',
        padding: '0px',
        border: '0px'
      }
    }));
  }

  return colorbar;
}

function createValueLabels(numLabels, width) {
  var labelsPanel = ui.Panel({
    layout: ui.Panel.Layout.flow('horizontal'),
    style: {width: width + 'px'}
  });

  for (var i = 1; i <= numLabels; i++) {
    labelsPanel.add(ui.Label({
      value: i.toString(),
      style: {
        width: (100 / numLabels) + '%',
        textAlign: 'center',
        margin: '0px',
        padding: '0px',
        border: '0px'
      }
    }));
  }

  return labelsPanel;
}

// Create the legend panel
var legend = ui.Panel({
  widgets: [
    ui.Label('Flashiness values', {fontWeight: 'bold'}),
    createValueLabels(9, 300),
    createColorbar(palette, 300, 20),
  ],
  style: {position: 'bottom-right', padding: '8px 15px', backgroundColor: 'rgba(255, 255, 255, 0.7)'},
});

Map.add(legend);
