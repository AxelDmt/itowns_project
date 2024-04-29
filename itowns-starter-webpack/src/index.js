import * as itowns from 'itowns';
import * as dat from 'dat.gui';

// Get our `<div id="viewerId">` element. When creating a `View`, a canvas will
// be appended to this element.
const viewerDiv = document.getElementById('viewerDiv');

// Define an initial camera position
const placement = {
    coord: new itowns.Coordinates('EPSG:4326', 5.363227, 43.2957225),
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

// Create a new 3D tiles layer with batch table hierarchy extension
const extensions = new itowns.C3DTExtensions();

extensions.registerExtension("3DTILES_batch_table_hierarchy",
    { [itowns.C3DTilesTypes.batchtable]:
        itowns.C3DTBatchTableHierarchyExtension });

const promises = [];

///////////////////////////// Building ///////////////////////////////////////////////////////

const buildingsSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_buildings/tileset.json'
});

const buildingsLayer = new itowns.C3DTilesLayer('buildings', {
    source: buildingsSource,
    style: { fill: { color: 'yellow'}},
    registeredExtensions: extensions,
}, view);


promises.push(itowns.View.prototype.addLayer.call(view, buildingsLayer));

///////////////////////////// Building Implicit Geom /////////////////////////////////////////////////////////

const implicitbuildingSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/merged_tileset_building/tileset.json'
});

const implicitbuildingLayer = new itowns.C3DTilesLayer('implicit_building', {
    source: implicitbuildingSource,
    style: { fill: { color: 'red'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, implicitbuildingLayer));

///////////////////////////// Relief /////////////////////////////////////////////////////////

const style = {
     fill: { color: 'green' },
};

const reliefsSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_reliefs/tileset.json',
});

const reliefsLayer = new itowns.C3DTilesLayer('reliefs', {
    source: reliefsSource,
    style: { fill: { color: 'white'}},
    registeredExtensions: extensions,
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, reliefsLayer));

///////////////////////////// Traffic ///////////////////////////////////////////////////////

const trafficSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_traffic/tileset.json'
});

const trafficLayer = new itowns.C3DTilesLayer('traffic', {
    source: trafficSource,
    style: { fill: { color: 'white'}},
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, trafficLayer));


///////////////////////////// Water /////////////////////////////////////////////////////////

const waterSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_water_bodies/tileset.json'
});

const waterLayer = new itowns.C3DTilesLayer('water_bodies', {
    source: waterSource,
    style: { fill: { color: 'blue'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, waterLayer));

///////////////////////////// Bridge /////////////////////////////////////////////////////////

const bridgeSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_bridges/tileset.json'
});

const bridgeLayer = new itowns.C3DTilesLayer('bridge', {
    source: bridgeSource,
    style: { fill: { color: 'red'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, bridgeLayer));

///////////////////////////// Tunnel /////////////////////////////////////////////////////////

const tunnelSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_tunnel/tileset.json'
});

const tunnelLayer = new itowns.C3DTilesLayer('tunnel', {
    source: tunnelSource,
    style: { fill: { color: 'black'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, tunnelLayer));

///////////////////////////// Plant Covers /////////////////////////////////////////////////////////

const plantSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_plant/tileset.json'
});

const plantLayer = new itowns.C3DTilesLayer('plant', {
    source: plantSource,
    style: { fill: { color: 'darkgreen'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, plantLayer));

///////////////////////////// Vegetation Implicit Geom /////////////////////////////////////////////////////////

const implicitvegetationSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/merged_tileset_vege/tileset.json'
});

const implicitvegetationLayer = new itowns.C3DTilesLayer('implicit_vegetation', {
    source: implicitvegetationSource,
    style: { fill: { color: 'red'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, implicitvegetationLayer));

///////////////////////////// City Furnitures /////////////////////////////////////////////////////////

const furnitureSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/junk_furniture/tileset.json'
});

const furnitureLayer = new itowns.C3DTilesLayer('furniture', {
    source: furnitureSource,
    style: { fill: { color: 'pink'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, furnitureLayer));

///////////////////////////// City Furnitures Implicit Geom /////////////////////////////////////////////////////////

const implicitfurnitureSource = new itowns.C3DTilesSource({
    url: 'http://localhost:8000/py3dtilers/merged_tileset_furniture/tileset.json'
});

const implicitfurnitureLayer = new itowns.C3DTilesLayer('implicit_furniture', {
    source: implicitfurnitureSource,
    style: { fill: { color: 'red'}}
}, view);

promises.push(itowns.View.prototype.addLayer.call(view, implicitfurnitureLayer));

///////////////////////////// GUI /////////////////////////////////////////////////////////

const gui = new dat.GUI();

//########################## Function ###################################################//

function toggleLayerVisibility(layer, value) {
    if (value) {
        layer.visible = true;
    }else{
        layer.visible = false;
        console.log(value);
    }
    view.notifyChange();
}

function changeLayerOpacity(layer, value) {
    layer.transparent = true;
    layer.opacity = value;
    console.log(layer.opacity);
    view.notifyChange(true);
}

Promise.all(promises).then(function _(layers) {
    window.addEventListener('mousemove',
        (event) => pickLayersInfo(event, layers),false);
});

var pickingArgs = {};
pickingArgs.htmlDiv = document.getElementById('featureInfo');
pickingArgs.view = view;
pickingArgs.layer = buildingsLayer;

let time;
function pickLayersInfo(event, layers) {
    const currentTime = Date.now();
    if (currentTime - time < 100000) return;
    time = currentTime;

    layers.forEach((l) => pickLayerInfo(event, l));
}

function pickLayerInfo(event, layer) {


    if (!layer.isC3DTilesLayer) {
        console.warn('Function fillHTMLWithPickingInfo only works' +
            ' for C3DTilesLayer layers.');
        return;
    }

    // Get intersected objects
    const intersects = view.pickObjectsAt(event, 5, layer);
    if (intersects.length === 0) { return; }

    // Get information from intersected objects (from the batch table and
    // eventually the 3D Tiles extensions
    const closestC3DTileFeature = layer.getC3DTileFeatureFromIntersectsArray(intersects);

    console.log(closestC3DTileFeature.getInfo().batchTable);
}

//########################## Dictionnary ###################################################//

const layers = {
    buildings: true,
    reliefs: true,
    traffic: true,
    water: true,
    bridge: true,
    tunnel: true,
    plant: true,
    furniture: true,
    implicit_furniture: true,
    implicit_building: true,
    implicit_vegetation: true,
};

//########################## GUI Folders ###################################################//

const layersFolder = gui.addFolder('Layers');

const buildingFolder = layersFolder.addFolder('Buildings');
buildingFolder.add(layers, 'buildings').onChange((value) => {
    toggleLayerVisibility(buildingsLayer, value);
});
buildingFolder.add(buildingsLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(buildingsLayer, value);
});

const implicitbuildingFolder = layersFolder.addFolder('Implicit Building');
implicitbuildingFolder.add(layers, 'implicit_building').onChange((value) => {
    toggleLayerVisibility(implicitbuildingLayer, value);
});
implicitbuildingFolder.add(implicitbuildingLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(implicitbuildingLayer, value);
});

const trafficFolder = layersFolder.addFolder('Traffic');
trafficFolder.add(layers, 'traffic').onChange((value) => {
    toggleLayerVisibility(trafficLayer, value);
});
trafficFolder.add(trafficLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(trafficLayer, value);
});

const bridgeFolder = layersFolder.addFolder('Bridges');
bridgeFolder.add(layers, 'bridge').onChange((value) => {
    toggleLayerVisibility(bridgeLayer, value);
});
bridgeFolder.add(bridgeLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(bridgeLayer, value);
});

const tunnelFolder = layersFolder.addFolder('Tunnels');
tunnelFolder.add(layers, 'tunnel').onChange((value) => {
    toggleLayerVisibility(tunnelLayer, value);
});
tunnelFolder.add(tunnelLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(tunnelLayer, value);
});

const furnitureFolder = layersFolder.addFolder('City Furnitures');
furnitureFolder.add(layers, 'furniture').onChange((value) => {
    toggleLayerVisibility(furnitureLayer, value);
});
furnitureFolder.add(furnitureLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(furnitureLayer, value);
});

const implicitfurnitureFolder = layersFolder.addFolder('Implicit City Furnitures');
implicitfurnitureFolder.add(layers, 'implicit_furniture').onChange((value) => {
    toggleLayerVisibility(implicitfurnitureLayer, value);
});
implicitfurnitureFolder.add(implicitfurnitureLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(implicitfurnitureLayer, value);
});

const reliefFolder = layersFolder.addFolder('Reliefs');
reliefFolder.add(layers, 'reliefs').onChange((value) => {
    toggleLayerVisibility(reliefsLayer, value);
});
reliefFolder.add(reliefsLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(reliefsLayer, value);
});

const plantFolder = layersFolder.addFolder('Plant Covers');
plantFolder.add(layers, 'plant').onChange((value) => {
    toggleLayerVisibility(plantLayer, value);
});
plantFolder.add(plantLayer, 'opacity').min(0.0).max(1.0).step(0.1).onChange((value) => {
    changeLayerOpacity(plantLayer, value);
});

const implicitvegetationFolder = layersFolder.addFolder('Implicit Vegetation');
implicitvegetationFolder.add(layers, 'implicit_vegetation').onChange((value) => {
    toggleLayerVisibility(implicitvegetationLayer, value);
});
implicitvegetationFolder.add(implicitvegetationLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(implicitvegetationLayer, value);
});

const waterFolder = layersFolder.addFolder('Water Bodies');
waterFolder.add(layers, 'water').onChange((value) => {
    toggleLayerVisibility(waterLayer, value);
});
waterFolder.add(waterLayer, 'opacity').min(0.0).max(1.0).step(0.01).onChange((value) => {
    changeLayerOpacity(waterLayer, value);
});

//########################## GUI Style ###################################################//

layersFolder.domElement.style.position = 'absolute';
layersFolder.domElement.style.top = '0';
layersFolder.domElement.style.left = '0';
layersFolder.domElement.style.zIndex = '100000';
document.body.appendChild(layersFolder.domElement);
