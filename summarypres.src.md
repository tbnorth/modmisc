{% if not OW_ONLY %}
# Data, modeling, visualization, and sensors <!-- .tags: pf -->

Terry Brown, Post doc.
Brown.TerryN@epa.gov

## Themes <!-- .tags: pf -->

 - Processing / management of large datasets from 
   sensors and simulations
 - Visualization of large, complex datasets  
 - Getting from data to understanding for resource managers

# SNNM <!-- .tags: pf -->

Simple Nearshore Nutrient Model

James Pauer and Tom Hollenhorst

Modeling nutrient movement in the nearshore as a
precursor to Harmful Algal Blooms (HABs).

## Simple == Open <!-- .tags: pf -->

 - Try to avoid calibration
 - Some models have dozens of calibration
   variables and minimal observations.
 - Prefer direct use of real world observations
 - Minimize complexity


## Visualization <!-- .tags: pf -->

 - Web based, *potentially* better for
   collaboration.
 - Complex patterns more easily observed.

<video height="500" controls data-autoplay>
    <source data-src="./vid/0001-0609.mkv"
    type="video/mp4" />
</video>

# Glider

## Data pipeline

## Visualization

 - Web based, *potentially* better for
   collaboration.
 - Complex patterns more easily observed.

## Application

 - Supplement satellite surface / shallow view
 - Sampling for 40-100+ days a year

# Data indexing / mining <!-- .tags: pf -->

Turning 20 years of data into a 20 year data set.

 - Data spider - search by file type, column
 names, dates, number of records, spatial
 footprint.
 - Data index, tags, and full text searching.

[Data inventory
interface](http://v2626umcth926.rtord.epa.gov/data_inventory/)

{% endif %}{# not OW_ONLY #}
{% if OW_ONLY %}
# Modeling transfer from outfalls to intakes in the Great Lakes

Terry Brown, Post doc.  
Brown.TerryN@epa.gov  
Mid-continent Ecology Division  
Watersheds and Water Resources Branch

## OW working on bromide from power stations
{% else %}
# OW working on bromide from power stations <!-- .tags: pf -->
{% endif %}

 - Work for Office of Water, currently rule making
   for bromide release from coal fired power plants.
 - Bromide - commonly found in steam
   electric plant effluent - is a trihalomethane
   precursor.
 - Chemicals in this family are thought to be
   carcinogens.

## Nation wide, minus the Great Lakes

 - OW had already done the analysis for rivers and
   streams, but not the Great Lakes.
 - Great Lakes other than Michigan are half
   Canadian, always a challenge data wise.
 - 30 million people live in the Great Lakes
   basin.

## Considerations

 - Our model is not predicting intake bromide concentration, but
   relative exposure, seasonality etc.
 - We used hydrodynamic model output from NOAA,
 who provide archived flow data for all five Great
 Lakes for the past 15 years.  
 - NOAA's currently
 available data is a generation behind, model
 wise, but its immediate availability made our
 work possible in the time available.

## Nearshore flow

 - There is a nearshore flow or "stream" in the
   Great Lakes that retains inputs.
 - Mixing with the full lake volume is delayed.
 - Contaminants entering the Great Lakes linger in
   the shallower nearshore.
   - Dilution is more limited.
   - The nearshore is where people interact with
     the lakes.

## Nearshore flow <!-- .slide: data-state="hide-head" -->

![Ontario](./img/LakeOntarioArial.png)

## Nearshore flow <!-- .slide: data-state="hide-head" -->

August 11 2012
![Superior](./img/t1.12224.USA3.143.250m.jpg)

## Previous grid based modeling

 - Track fate of P entering the lakes, precursor
   to algal blooms.
 - Interactive web based visualization.

## Previous work

<video height="500" controls data-autoplay>
    <source data-src="./vid/0001-0609.mkv"
    type="video/mp4" />
</video>

## Agent based modeling <!-- .tags: pf -->

 - Able to represent details of complex systems.
 - Captures emergent behavior / features.
 - Works well with a distributed computing
   approach.

## Agents

- Exist at a specific point in space.
- Can have multiple static and varying attributes.
- Can interact with surrounding agents (and
  grid cells) based on distance etc.
- Added and removed from the model over the
  model's run-time.

## Agents as individuals

![fish](img/fish.png)

## Agent Based Models (ABMs) and complexity

- Run ABM with thousands of agents...
- Competition for food / shade.
- Big fish / little fish
  - How does time spent hiding impact time
    spent feeding?
- Test different behaviors / foraging
  strategies.

Complexity more easily represented in ABMs.

## Agents for continuous phenomena

- Historically agent based modeling focused on distinct
  entities (fish in streams, etc.).
- Modern computational power allows large numbers of
  agents to approximate continuous phenomena.
- Often used to model plumes / spills.


## EPA High End Scientific Computing (HESC)

 - 128 nodes (computers) each with 256 Gb RAM and
   32 cores.
 - Large memory node, 1.5 Tb RAM.
 - 4 GPU nodes
 - 1.4 Pb, or 1,400 Tb drive
 - EMVL group provides support, but quite open to
   direct use.

## Model structure, grid data <!-- .tags: pf -->

 - Run for 12 years, 2004-2015, analyze the last
   ten.
 - Bromide very persistent, particles given a two year
   life-span.

## Grid cells <!-- .slide: data-state="hide-head" -->
<!-- .tags: pf -->
<video height="600" controls data-autoplay>
    <source data-src="./vid/noaacells.mp4"
    type="video/mp4" />
</video>

## Intake
<!-- .tags: pf -->
 
![Intake](./img/partintake.png) <!-- .element: style="filter: invert(100%)" width="600" -->

9 billion modeled particle positions

## LM animation <!-- .slide: data-state="hide-head" -->
<!-- .tags: pf -->

<video height="700" controls data-autoplay>
    <source data-src="./vid/outputMap.mp4"
    type="video/mp4" />
</video>

## Seasonal variations
<!-- .tags: pf -->

![one site](img/month_mean.WI2410100_2.png) <!-- .element: style="filter: invert(100%)" -->

## Seasonal variations
<!-- .tags: pf -->

![all sites](img/month_mean2.png) <!-- .element: style="filter: invert(100%)" -->

## Seasonal patterns / Improved model
<!-- .tags: pf -->

 - Seasonal patterns in nearshore currents influence
   intake exposure levels.
 - Office of Water originally using
   <br/>"people within 50 km of plant".
 - Seasonal effects and temperature influence exposure pathways.
 - OW sees this as a basis for further work in the Great Lakes.
 
{% if not OW_ONLY %}
# Drifters
<!-- .slide: data-state="img-left" -->
<!-- .tags: pf -->

![Drifter internals](./img/20180524_114738c.jpg) <!-- .element: height="500" -->

Tom Hollenhorst and Jim Berrill

 - Map currents, conductivity, and temperature.
 - Low cost, deploy en masse.
 - Validate hydrodynamic models.
 - Measure at scales model data is unavailable.

## Drifters - components
<!-- .tags: pf -->

![Drifter internals](./img/drifterside.png) <!-- .element: width="80%" -->

## Drifters - components
<!-- .tags: pf -->

![Drifter internals](./img/drifterotherside.png) <!-- .element: width="80%" -->

## Low cost
<!-- .tags: pf -->

 - Unit cost < $250.
   - cf. a Cyanoscope for $500+
 - Affordable for smaller communities.
 - Outreach opportunity for schools etc.
   - Have students assemble units
   - Deploy units from kayaks etc.

## Application
<!-- .slide: data-state="img-right" -->

![Dropping drifter overboard](./img/IMG_20180524_124736638crop.jpg)

 - Shallow environments, rivers.
 - Detect tributary specific inputs.
   - warm water from *that* outfall
   - road salt from *that* stream
 - Local site specificity gives managers actionable
   information.

## Software components
<!-- .tags: pf -->

 - Software on the drifters, in MicroPython, which
   collects and transmits data.
 - Software on the field laptop, tracking
   drifters.
 - Post-processing and visualisation software.
 - "DrifterOS" - software to download data and
   update software wirelessly.

## Internet of things
<!-- .tags: pf -->

 - AES encrypted transmission.
 - Units relay messages to increase range.
 - Stream network monitoring.

![Collecting data from stream network](./img/streamnw.svg) <!-- .element width="80%" -->

## Visualization
<!-- .tags: pf -->

 - Web based
 - Observe complex patterns
 - Select representative parts of data
 - View relationships between drifters

## PP animation <!-- .slide: data-state="hide-head" -->
<!-- .tags: pf -->

<video height="700" controls data-autoplay>
    <source data-src="./vid/0001-1262.mkv" type="video/mp4" />
</video>

{% endif %}
<!--
vim:tw=50
--->
# Themes <!-- .tags: pf -->

 - Processing / management of large datasets from 
   sensors and simulations
 - Visualization of large, complex datasets  
 - Getting from data to understanding for resource managers

