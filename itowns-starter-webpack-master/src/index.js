import * as itowns from 'itowns';
import * as dat from 'dat.gui';

// Get our `<div id="viewerId">` element. When creating a `View`, a canvas will
// be appended to this element.
const viewerDiv = document.getElementById('viewerDiv');

// Define an initial camera position
const placement = {
    coord: new itowns.Coordinates('EPSG:4326', 5.3665993, 43.2989838),
    range: 2500,
};

// Create an empty Globe View
const view = new itowns.GlobeView(viewerDiv, placement);

// Declare your data source configuration. In this context, those are the
// parameters used in the WMTS requests.
const orthoConfig = {
    'url': 'https://data.geopf.fr/wmts',
    'crs': 'EPSG:3857',
    'format': 'image/jpeg',
    'name': 'ORTHOIMAGERY.ORTHOPHOTOS',
    'tileMatrixSet': 'PM',
};

// Instantiate the WMTS source of your imagery layer.
const imagerySource = new itowns.WMTSSource(orthoConfig);

// Create your imagery layer
const imageryLayer = new itowns.ColorLayer('imagery', {
    source: imagerySource,
});

// Add it to source view!
view.addLayer(imageryLayer);

///////////////////////////// Building ///////////////////////////////////////////////////////

const buildingsSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_buildings/tileset.json'
});

const buildingsLayer = new itowns.C3DTilesLayer('buildings', {
    source: buildingsSource,
    style: { fill: { color: 'yellow'}},
}, view);
itowns.View.prototype.addLayer.call(view, buildingsLayer);

///////////////////////////// Relief /////////////////////////////////////////////////////////

const style = {
     fill: { color: 'green' },
};

const reliefsSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_reliefs/tileset.json',
});

const reliefsLayer = new itowns.C3DTilesLayer('reliefs', {
    source: reliefsSource,
    style: { fill: { color: 'yellowgreen'}},
}, view);
itowns.View.prototype.addLayer.call(view, reliefsLayer);

///////////////////////////// Traffic ///////////////////////////////////////////////////////

const trafficSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_traffic/tileset.json'
});

const trafficLayer = new itowns.C3DTilesLayer('traffic', {
    source: trafficSource,
    style: { fill: { color: 'lightgrey'}},
}, view);
itowns.View.prototype.addLayer.call(view, trafficLayer);


///////////////////////////// Water /////////////////////////////////////////////////////////

const waterSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_water_bodies/tileset.json'
});

const waterLayer = new itowns.C3DTilesLayer('water_bodies', {
    source: waterSource,
    style: { fill: { color: 'blue'}}
}, view);
itowns.View.prototype.addLayer.call(view, waterLayer);

///////////////////////////// Bridge /////////////////////////////////////////////////////////

const bridgeSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_bridges/tileset.json'
});

const bridgeLayer = new itowns.C3DTilesLayer('bridge', {
    source: bridgeSource,
    style: { fill: { color: 'red'}}
}, view);
itowns.View.prototype.addLayer.call(view, bridgeLayer);

///////////////////////////// Tunnel /////////////////////////////////////////////////////////

const tunnelSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_tunnel/tileset.json'
});

const tunnelLayer = new itowns.C3DTilesLayer('tunnel', {
    source: tunnelSource,
    style: { fill: { color: 'black'}}
}, view);
itowns.View.prototype.addLayer.call(view, tunnelLayer);

///////////////////////////// Plant Covers /////////////////////////////////////////////////////////

const plantSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_plant/tileset.json'
});

const plantLayer = new itowns.C3DTilesLayer('plant', {
    source: plantSource,
    style: { fill: { color: 'darkgreen'}}
}, view);
itowns.View.prototype.addLayer.call(view, plantLayer);

///////////////////////////// City Furnitures /////////////////////////////////////////////////////////

const furnitureSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_furniture/tileset.json'
});

const furnitureLayer = new itowns.C3DTilesLayer('furniture', {
    source: furnitureSource,
    style: { fill: { color: 'pink'}}
}, view);
itowns.View.prototype.addLayer.call(view, furnitureLayer);

///////////////////////////// GUI /////////////////////////////////////////////////////////

const gui = new dat.GUI();

/**//**//**//**//**//**//* Function *//**//**//**//**//**//**//**//**//**//**//**//**//**/

function toggleLayerVisibility(layer, value) {
    if (value) {
        layer.visible = true;
    }else{
        layer.visible = false;
        console.log(value);
    }
    view.notifyChange();
}

/**//**//**//**//**//**//* Dictionnary *//**//**//**//**//**//**//**//**//**//**//**//**//**/

const layers = {
    buildings: true,
    reliefs: true,
    traffic: true,
    water: true,
    bridge: true,
    tunnel: true,
    plant: true,
    furniture: true,
};

/**//**//**//**//**//**//* GUI Folders *//**//**//**//**//**//**//**//**//**//**//**//**//**/

const layersFolder = gui.addFolder('Layers');

const buildingFolder = layersFolder.addFolder('Buildings');
buildingFolder.add(layers, 'buildings').onChange((value) => {
    toggleLayerVisibility(buildingsLayer, value);
});

const trafficFolder = layersFolder.addFolder('Traffic');
trafficFolder.add(layers, 'traffic').onChange((value) => {
    toggleLayerVisibility(trafficLayer, value);
});

const bridgeFolder = layersFolder.addFolder('Bridges');
bridgeFolder.add(layers, 'bridge').onChange((value) => {
    toggleLayerVisibility(bridgeLayer, value);
});

const tunnelFolder = layersFolder.addFolder('Tunnels');
tunnelFolder.add(layers, 'tunnel').onChange((value) => {
    toggleLayerVisibility(tunnelLayer, value);
});

const furnitureFolder = layersFolder.addFolder('City Furnitures');
furnitureFolder.add(layers, 'furniture').onChange((value) => {
    toggleLayerVisibility(furnitureLayer, value);
});

const reliefFolder = layersFolder.addFolder('Reliefs');
reliefFolder.add(layers, 'reliefs').onChange((value) => {
    toggleLayerVisibility(reliefsLayer, value);
});

const plantFolder = layersFolder.addFolder('Plant Covers');
plantFolder.add(layers, 'plant').onChange((value) => {
    toggleLayerVisibility(plantLayer, value);
});

const waterFolder = layersFolder.addFolder('Water Bodies');
waterFolder.add(layers, 'water').onChange((value) => {
    toggleLayerVisibility(waterLayer, value);
});

/**//**//**//**//**//**//* GUI Style *//**//**//**//**//**//**//**//**//**//**//**//**//**/

layersFolder.domElement.style.position = 'absolute';
layersFolder.domElement.style.top = '0';
layersFolder.domElement.style.left = '0';
layersFolder.domElement.style.zIndex = '1000';
document.body.appendChild(layersFolder.domElement);
